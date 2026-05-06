from django import forms
from .models import Movie
from django.contrib.auth.forms import UserCreationForm

class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ['title', 'genre', 'release_year', 'status', 'rating']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Например: Интерстеллар'}),
            'genre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Например: Фантастика'}),
            'release_year': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': '2014', 'min': 1888, 'max': 2026}),
            'status': forms.Select(attrs={'class': 'form-select'}),
            'rating': forms.NumberInput(attrs={'class': 'form-control', 'min': 1, 'max': 10, 'placeholder': 'Оценка от 1 до 10'}),
        }

class RegisterForm(UserCreationForm):
    pass
