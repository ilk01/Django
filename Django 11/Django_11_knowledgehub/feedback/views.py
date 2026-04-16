from django.http import HttpResponse, HttpRequest
from django.shortcuts import render, redirect
from datetime import date

from feedback.forms import ContactForm, NoteForm
from notes import data


def contact_view(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            return redirect('contact_success')
    else:
        form = ContactForm()
    return render(request, 'feedback/contact.html', {'form': form})


def contact_success_view(request: HttpRequest) -> HttpResponse:
    return render(request, 'feedback/contact_success.html')


def create_note_view(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            # Получаем максимальный id и добавляем 1
            max_id = max(note["id"] for note in data.TEMP_NOTES) if data.TEMP_NOTES else 0
            
            # Создаём новую заметку
            new_note = {
                "id": max_id + 1,
                "title": form.cleaned_data['title'],
                "category": form.cleaned_data['category'],
                "content": form.cleaned_data['content'],
                "created_at": str(date.today()),
                "tags": [tag.strip() for tag in form.cleaned_data['tags'].split(',') if tag.strip()] if form.cleaned_data['tags'] else [],
            }
            
            # Добавляем в список
            data.TEMP_NOTES.append(new_note)
            
            return redirect('notes:notes_list')
    else:
        form = NoteForm()
    return render(request, 'feedback/create_note.html', {'form': form})
