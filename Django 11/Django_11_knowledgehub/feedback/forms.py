from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        label='Ваше имя',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите ваше имя'})
    )
    email = forms.EmailField(
        label='Email',
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Введите ваш email'})
    )
    message = forms.CharField(
        label='Сообщение',
        widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Введите ваше сообщение', 'rows': 5})
    )


class NoteForm(forms.Form):
    title = forms.CharField(
        max_length=200,
        label='Заголовок',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите заголовок'})
    )
    content = forms.CharField(
        label='Содержание',
        widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Введите содержание', 'rows': 5})
    )
    category = forms.CharField(
        max_length=100,
        label='Категория',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите название категории'})
    )
    tags = forms.CharField(
        max_length=200,
        label='Теги',
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите теги через запятую'})
    )

    def clean_title(self):
        title = self.cleaned_data.get('title', '').strip()
        if title.lower().startswith('test'):
            raise forms.ValidationError('Заголовок не должен начинаться со слова "test"')
        return title
