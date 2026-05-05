from django import forms
from .models import Article, Category, Comment

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'content', 'image', 'category']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'w-full px-3 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500'}),
            'content': forms.Textarea(attrs={'class': 'w-full px-3 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500', 'rows': 10}),
            'category': forms.Select(attrs={'class': 'w-full px-3 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500'}),
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={
                'class': 'w-full px-4 py-3 border border-gray-100 rounded-sm focus:outline-none focus:border-[#548eaa] resize-none',
                'placeholder': 'Напишите комментарий...',
                'rows': 4
            }),
        }

