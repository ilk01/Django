from django import forms
from django.contrib.auth.models import User
from .models import Profile

class UserRegistrationForm(forms.ModelForm):
    email = forms.EmailField(label="Email", widget=forms.EmailInput(attrs={'placeholder': ''}))
    username = forms.CharField(label="Никнейм", widget=forms.TextInput(attrs={'placeholder': ''}))
    password = forms.CharField(label="Пароль", widget=forms.PasswordInput(attrs={'placeholder': ''}))
    password_confirm = forms.CharField(label="Пароль ещё раз", widget=forms.PasswordInput(attrs={'placeholder': ''}))
    class Meta:
        model = User
        fields = ['email', 'username', 'password']
    def clean_password_confirm(self):
        password = self.cleaned_data.get('password')
        password_confirm = self.cleaned_data.get('password_confirm')
        if password and password_confirm and password != password_confirm:
            raise forms.ValidationError("Passwords do not match")
        return password_confirm
