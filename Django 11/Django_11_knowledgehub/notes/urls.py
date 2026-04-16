from django.urls import path

from . import views
from .views import AboutPageView
from feedback.views import create_note_view

app_name = 'notes'
urlpatterns = [
    path("", views.notes_list, name="notes_list"),
    path("<int:note_id>/", views.note_detail, name="note_detail"),
    path("create/", create_note_view, name="create_note"),
    # path('about/', views.about, name='about'),

    path("about/", AboutPageView.as_view(), name="about"),

]