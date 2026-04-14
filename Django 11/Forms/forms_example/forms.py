from django import  forms
from django.core.exceptions import ValidationError
from django.template.defaultfilters import first


class ContactForm(forms.Form):
    name = forms.CharField(label='Name', max_length=100, min_length=5)
    email = forms.EmailField(label='Email')

class FeedbackForm(forms.Form):
    subject = forms.CharField(max_length=100, min_length=5, required=True)
    message = forms.CharField(widget=forms.Textarea,min_length=5)

class NoteDraftForm(forms.Form):
    title = forms.CharField(max_length=100)
    content = forms.CharField(widget=forms.Textarea)
    secret_word = forms.CharField()
    confirm_secret_word = forms.CharField()

    def clean_title(self):
        title = self.cleaned_data['title'].strip()
        if len(title) < 3:
            raise ValidationError("Title must be at least 5 characters")
        banned_words = ["spam", "virus", "niga"]
        if any(word in title.lower() for word in banned_words):
            raise ValidationError("Title contains banned words")
        return title

    def clean(self):
        cleaned_data = super().clean()
        first = cleaned_data.get("secret_word")
        second = cleaned_data.get("confirm_secret_word")
        if first and second and first != second:
            raise ValidationError("Secret word and confirm secret word must match")
        return cleaned_data