from django.contrib import admin
from .models import Category, Article, Rating, Vote, Bookmark, Notification

@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ('user', 'message', 'is_read', 'created_at')
    list_filter = ('is_read', 'created_at')

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'category', 'status', 'is_approved', 'created_at')
    list_filter = ('status', 'is_approved', 'category', 'created_at')
    search_fields = ('title', 'content')
    prepopulated_fields = {'slug': ('title',)}
    actions = ['approve_articles', 'reject_articles']
    def approve_articles(self, request, queryset):
        for article in queryset:
            if not article.is_approved:
                article.is_approved = True
                article.status = 'published'
                article.save()
                Notification.objects.create(
                    user=article.author,
                    message=f'Ваша статья "{article.title}" была одобрена и опубликована!'
                )
    approve_articles.short_description = "Одобрить выбранные статьи"
    def reject_articles(self, request, queryset):
        for article in queryset:
            if article.is_approved:
                article.is_approved = False
                article.status = 'draft'
                article.save()
                Notification.objects.create(
                    user=article.author,
                    message=f'Ваша статья "{article.title}" была отклонена и переведена в черновики.'
                )
    reject_articles.short_description = "Отклонить выбранные статьи"

@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ('article', 'user', 'score')

@admin.register(Vote)
class VoteAdmin(admin.ModelAdmin):
    list_display = ('article', 'user', 'value')

@admin.register(Bookmark)
class BookmarkAdmin(admin.ModelAdmin):
    list_display = ('article', 'user', 'created_at')
