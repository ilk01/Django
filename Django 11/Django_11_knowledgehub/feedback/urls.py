from django.urls import path

from feedback import views

app_name = 'feedback'
urlpatterns = [
    path('contact/', views.contact_view, name='contact'),
    path('contact/success/', views.contact_success_view, name='contact_success'),
    path('create-note/', views.create_note_view, name='create_note'),
]
