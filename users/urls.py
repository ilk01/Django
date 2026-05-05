from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('banned/', views.banned_view, name='banned'),
    path('staff/users/', views.admin_users_list, name='admin_users_list'),
    path('authors/', views.authors_list, name='authors_list'),
    path('@<str:username>/toggle-admin/', views.toggle_admin_status, name='toggle_admin'),
    path('@<str:username>/toggle-ban/', views.toggle_ban_status, name='toggle_ban'),
    path('@<str:username>/', views.profile_view, name='profile'),
]
