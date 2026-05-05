from django.urls import path
from . import views

urlpatterns = [
    path('', views.ArticleListView.as_view(), name='article_list'),
    path('article/new/', views.ArticleCreateView.as_view(), name='article_create'),
    path('article/<slug:slug>/', views.ArticleDetailView.as_view(), name='article_detail'),
    path('article/<slug:slug>/comment/', views.add_comment, name='add_comment'),
    path('article/<slug:slug>/edit/', views.ArticleUpdateView.as_view(), name='article_update'),
    path('article/<slug:slug>/vote/<str:value>/', views.vote_article, name='vote_article'),
    path('article/<slug:slug>/bookmark/', views.bookmark_article, name='bookmark_article'),
    path('article/<slug:slug>/rate/<int:score>/', views.rate_article, name='rate_article'),
    path('staff/articles/', views.admin_article_list, name='admin_article_list'),
    path('article/<slug:slug>/toggle-approval/', views.toggle_article_approval, name='toggle_article_approval'),
    path('notifications/read/', views.mark_notifications_read, name='mark_notifications_read'),
]
