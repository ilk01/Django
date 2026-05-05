from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm
from django.contrib import messages
from django.contrib.auth.models import User
from articles.models import Article

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            messages.success(request, f'Account created for {user.username}!')
            login(request, user)
            return redirect('article_list')
    else:
        form = UserRegistrationForm()
    return render(request, 'users/register.html', {'form': form})

def profile_view(request, username):
    user = get_object_or_404(User, username=username)
    tab = request.GET.get('tab', 'profile')
    context = {
        'profile_user': user,
        'tab': tab,
    }
    if tab == 'articles':
        context['articles'] = Article.objects.filter(author=user, is_approved=True)
    elif tab == 'bookmarks':
        context['articles'] = Article.objects.filter(bookmarks__user=user, is_approved=True)
    return render(request, 'users/profile.html', context)

def banned_view(request):
    return render(request, 'users/banned.html')

@login_required
def toggle_admin_status(request, username):
    if not request.user.is_superuser:
        messages.error(request, 'У вас нет прав для этого действия.')
        return redirect('profile', username=username)
    
    target_user = get_object_or_404(User, username=username)
    if target_user.is_superuser:
        messages.error(request, 'Нельзя изменить статус суперадмина.')
    else:
        target_user.is_staff = not target_user.is_staff
        target_user.save()
        status = 'назначен админом' if target_user.is_staff else 'снят с должности админа'
        messages.success(request, f'Пользователь {target_user.username} {status}.')
    
    return redirect('profile', username=username)

@login_required
def toggle_ban_status(request, username):
    if not request.user.is_staff:
        messages.error(request, 'У вас нет прав для этого действия.')
        return redirect('profile', username=username)
    
    target_user = get_object_or_404(User, username=username)
    if target_user.is_superuser:
        messages.error(request, 'Нельзя забанить суперадмина.')
    else:
        profile = target_user.profile
        profile.is_banned = not profile.is_banned
        profile.save()
        status = 'заблокирован' if profile.is_banned else 'разблокирован'
        messages.success(request, f'Пользователь {target_user.username} {status}.')
    
    return redirect('profile', username=username)

from django.db.models import Count, Q

@login_required
def admin_users_list(request):
    if not request.user.is_staff:
        messages.error(request, 'У вас нет прав для доступа к этой странице.')
        return redirect('article_list')
    
    users = User.objects.annotate(
        articles_count=Count('articles'),
        comments_count=Count('comments')
    ).order_by('-date_joined')
    
    return render(request, 'users/admin_users_list.html', {'users_list': users})

def authors_list(request):
    from django.db.models import Count
    authors = User.objects.annotate(
        articles_count=Count('articles', filter=models.Q(articles__is_approved=True))
    ).filter(articles_count__gt=0).order_by('-articles_count')
    return render(request, 'users/authors_list.html', {'authors': authors})
