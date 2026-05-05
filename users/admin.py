from django.contrib import admin
from .models import Profile

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'is_banned')
    list_filter = ('is_banned',)
    search_fields = ('user__username', 'user__email')
    actions = ['ban_users', 'unban_users']

    def ban_users(self, request, queryset):
        queryset.update(is_banned=True)
    ban_users.short_description = "Забанить выбранных пользователей"

    def unban_users(self, request, queryset):
        queryset.update(is_banned=False)
    unban_users.short_description = "Разбанить выбранных пользователей"
