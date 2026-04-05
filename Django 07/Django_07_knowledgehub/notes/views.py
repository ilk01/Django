from django.http import HttpResponse, HttpRequest
from django.middleware.csrf import get_token
from django.shortcuts import render
from django.utils.html import  escape
from django.urls import reverse

from notes import data


# Create your views here.

def _html_shell(title: str, body: str)-> str:
    safe_title = escape(title)
    return f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>{safe_title}</title>
        <style>
            body{{font-family: system-ui, sans-serif; margin: 2rem; line-height: 1.5; }}
            a{{color: #0b57d0}}
            code{{background: #f4f4f4; padding: 0.1rem 0.35rem;  border-radius: 4px; }}
            .muted{{color: #555;}}
            ul.notes {{list-style: disc; padding-left: 1.25rem;}}
            form label{{display: block; margin-top: 0.75rem; }}
            input[type="text"], textarea{{width: min(520px, 100%); padding: 0.35rem }}
            .nav {{margin-bottom: 1.5rem; }}
        </style>
    </head>
    <body>
        <nav class="nav">
            <a href = "{escape(reverse("home"))}">Home</a>
            <a href = "{escape(reverse("about"))}">About</a>            
            <a href = "{escape(reverse("notes_list"))}">Notes</a>
        </nav>
        {body}   
    </body>
    </html>
"""

def _csrf_field(request: HttpRequest) -> str:
    token = get_token(request)
    return f'<input type="hidden" name="csrfmiddlewaretoken" value="{escape(token)}">'

def home(request: HttpRequest) -> HttpResponse:
    body = f"""
        <h1> Knowledge Hub </h1>
        <p>Welcome! This is home page</p>
        <p class="muted">Get to <a href="{escape(reverse("notes_list"))}"> notes_list</a></p>
    """
    return HttpResponse(_html_shell("Knowledge Hub - home page", body))


def about(request: HttpRequest)-> HttpResponse:
    body = f"""
            <h1> About this project </h1>
            <p>Knowledge Hub - project for Django course</p>
            <p class="muted">Lesson 7 - views and routes</p>
        """
    return HttpResponse(_html_shell("Knowledge Hub - about page", body))

def notes_list(request: HttpRequest)-> HttpResponse:
    raw_tag = request.GET.get('tag')
    raw_category = request.GET.get('category')

    notes = data.list_notes()

    if raw_tag:
        tag_filter = raw_tag.strip().lower()
        notes = [n for n in notes if n['tag'.lower()] == tag_filter]

    if raw_tag:
        category_filter = raw_category.strip().lower()
        notes = [n for n in notes if n['category'.lower()] == category_filter]

    items: list[str] = []
    for note in notes:
        url = reverse('notes_detail', kwargs={'note_id': note['id']})
        items.append(f"""
        <li><a href={escape(url)}>{escape(note['title'])}</a></li>
        <span class="muted">(tag: {escape(note["tag"])} category: {escape(note["category"])})</span>
""")

    items_html = "\n    ".join(items) if items else "<li class=muted>Notes not found</li>"

    filter_hint = f"""
        <p class="muted"> Filter example from query string:
        <a href="?tag=python><code>?tag=python</code></a>
        <a href="?category=django><code>?category=django</code></a>
        <a href="{escape(reverse("notes_list"))}>Reset filters</a?
        </p>
    """
    body =f"""
    <h1> Notes </h1>
    <ul class="notes">{items_html}</ul>
    """

    return HttpResponse(_html_shell("Notes list", body))
