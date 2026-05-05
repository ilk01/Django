import time
import json
from django.db import models
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from django.utils.text import slugify
from django.db.models import Avg, Count
from django.http import JsonResponse
from .models import Article, Category, Vote, Bookmark, Rating, Comment, Notification
from .forms import ArticleForm, CommentForm
from django.contrib import messages
from django.urls import reverse_lazy

class ArticleListView(ListView):
    model = Article
    template_name = 'articles/article_list.html'
    context_object_name = 'articles'
    paginate_by = 10
    def get_queryset(self):
        queryset = Article.objects.filter(is_approved=True)
        search_query = self.request.GET.get('q')
        if search_query:
            queryset = queryset.filter(
                models.Q(title__icontains=search_query) |
                models.Q(content__icontains=search_query) |
                models.Q(author__username__icontains=search_query)
            )
        feed_type = self.request.GET.get('feed', 'my')
        article_type = self.request.GET.get('type', 'article')
        sort = self.request.GET.get('sort', 'new')
        if any([self.request.GET.get('show_articles') == 'on', 
                self.request.GET.get('show_posts') == 'on', 
                self.request.GET.get('show_news') == 'on']):
            q_objects = models.Q()
            if self.request.GET.get('show_posts') == 'on':
                q_objects |= models.Q(category__slug='posts')
            if self.request.GET.get('show_news') == 'on':
                q_objects |= models.Q(category__slug='news')
            if self.request.GET.get('show_articles') == 'on':
                q_objects |= ~models.Q(category__slug__in=['posts', 'news'])
            queryset = queryset.filter(q_objects)
        else:
            if article_type == 'post':
                queryset = queryset.filter(category__slug='posts')
            elif article_type == 'news':
                queryset = queryset.filter(category__slug='news')
            elif article_type == 'article':
                queryset = queryset.exclude(category__slug__in=['posts', 'news'])
        if feed_type == 'favorites' and self.request.user.is_authenticated:
            queryset = queryset.filter(bookmarks__user=self.request.user)
        category_slug = self.request.GET.get('category')
        if category_slug:
            queryset = queryset.filter(category__slug=category_slug)
        if sort == 'popular':
            queryset = queryset.annotate(avg_rating=Avg('ratings__score')).filter(avg_rating__gte=4)
        return queryset.order_by('-created_at')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['current_sort'] = self.request.GET.get('sort', 'new')
        base_qs = Article.objects.filter(is_approved=True)
        context['articles_count'] = base_qs.exclude(category__slug__in=['posts', 'news']).count()
        context['posts_count'] = base_qs.filter(category__slug='posts').count()
        context['news_count'] = base_qs.filter(category__slug='news').count()
        if self.request.user.is_authenticated:
            context['unread_notifications_count'] = Notification.objects.filter(user=self.request.user, is_read=False).count()
            context['notifications'] = Notification.objects.filter(user=self.request.user)[:5]
        return context

@login_required
def mark_notifications_read(request):
    Notification.objects.filter(user=request.user, is_read=False).update(is_read=True)
    return JsonResponse({'status': 'success'})

@login_required
def admin_article_list(request):
    if not request.user.is_staff:
        messages.error(request, 'У вас нет прав для доступа к этой странице.')
        return redirect('article_list')
    
    articles = Article.objects.all().select_related('author', 'category').order_by('-created_at')
    return render(request, 'articles/admin_article_list.html', {'articles_list': articles})

@login_required
def toggle_article_approval(request, slug):
    if not request.user.is_staff:
        messages.error(request, 'У вас нет прав для этого действия.')
        return redirect('article_list')
    
    article = get_object_or_404(Article, slug=slug)
    article.is_approved = not article.is_approved
    article.save()
    
    status = 'одобрена' if article.is_approved else 'отправлена на модерацию'
    
    # Create notification for the author
    Notification.objects.create(
        user=article.author,
        message=f'Ваша статья "{article.title}" {status}.'
    )
    
    messages.success(request, f'Статья "{article.title}" {status}.')
    return redirect('admin_article_list')

class ArticleDetailView(DetailView):
    model = Article
    template_name = 'articles/article_detail.html'

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        obj.view_count += 1
        obj.save(update_fields=['view_count'])
        return obj
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        article = self.object
        
        content_blocks = []
        try:
            content_json = json.loads(article.content)
            if isinstance(content_json, dict) and 'blocks' in content_json:
                content_blocks = content_json['blocks']
        except (json.JSONDecodeError, TypeError):
            content_blocks = [{'type': 'paragraph', 'data': {'text': article.content}}]
            
        
        if self.request.user.is_authenticated:
            context['user_vote'] = Vote.objects.filter(article=self.object, user=self.request.user).first()
            context['is_bookmarked'] = Bookmark.objects.filter(article=self.object, user=self.request.user).exists()
            context['user_rating'] = Rating.objects.filter(article=self.object, user=self.request.user).first()
            context['comment_form'] = CommentForm()
        context['comments'] = article.comments.all().select_related('author')
        return context
@login_required
def add_comment(request, slug):
    article = get_object_or_404(Article, slug=slug)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.article = article
            comment.author = request.user
            comment.save()
            
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                return JsonResponse({
                    'status': 'success',
                    'username': comment.author.username,
                    'content': comment.content,
                    'created_at': comment.created_at.strftime("%d.%m.%Y в %H:%M"),
                    'avatar_letter': comment.author.username[0].upper()
                })
            
            messages.success(request, 'Ваш комментарий добавлен!')
    return redirect('article_detail', slug=slug)

class ArticleCreateView(LoginRequiredMixin, CreateView):
    model = Article
    form_class = ArticleForm
    template_name = 'articles/article_form.html'
    success_url = reverse_lazy('article_list')
    def form_valid(self, form):
        form.instance.author = self.request.user
        base_slug = slugify(form.instance.title)
        if not base_slug:
            base_slug = "article"
        form.instance.slug = f"{base_slug}-{int(time.time())}"
        if self.request.user.is_staff:
            form.instance.is_approved = True
        return super().form_valid(form)

class ArticleUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Article
    form_class = ArticleForm
    template_name = 'articles/article_form.html'
    success_url = reverse_lazy('article_list')

    def form_valid(self, form):
        if not self.request.user.is_staff:
            form.instance.is_approved = False
        return super().form_valid(form)

    def test_func(self):
        article = self.get_object()
        return self.request.user == article.author or self.request.user.is_staff

@login_required
def vote_article(request, slug, value):
    article = get_object_or_404(Article, slug=slug)
    value = int(value)
    vote, created = Vote.objects.get_or_create(article=article, user=request.user, defaults={'value': value})
    if not created:
        if vote.value == value:
            vote.delete()
        else:
            vote.value = value
            vote.save()
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        return JsonResponse({
            'total_likes': article.total_likes,
            'total_dislikes': article.total_dislikes,
            'balance': article.total_likes + article.total_dislikes,
            'user_vote': value if not created or (not created and vote.value == value) else 0
        })
    return redirect('article_detail', slug=slug)

@login_required
def bookmark_article(request, slug):
    article = get_object_or_404(Article, slug=slug)
    bookmark, created = Bookmark.objects.get_or_create(article=article, user=request.user)
    if not created:
        bookmark.delete()
        is_bookmarked = False
    else:
        is_bookmarked = True
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        return JsonResponse({
            'is_bookmarked': is_bookmarked,
            'count': article.bookmarks.count()
        })
    return redirect('article_detail', slug=slug)

@login_required
def rate_article(request, slug, score):
    article = get_object_or_404(Article, slug=slug)
    rating, created = Rating.objects.update_or_create(
        article=article, user=request.user, 
        defaults={'score': int(score)}
    )
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        return JsonResponse({
            'average_rating': round(article.average_rating, 1),
            'user_score': int(score)
        })
    return redirect('article_detail', slug=slug)
