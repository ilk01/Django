from django.shortcuts import render, redirect

from forms_example import forms
from forms_example.forms import ContactForm, FeedbackForm, NoteDraftForm


# Create your views here.

def contact_page(request):
    if request.method == "POST":
        form = ContactForm()
        if form.is_valid():
            return redirect("contact_success")
    else:
        form = ContactForm()
    return render(request, "contact.html", {"form": form})


def  feedback_page(request):
    form = FeedbackForm(request.POST or None)
    submitted_data = None
    if request.method == "POST" and form.is_valid():
        submitted_data = form.cleaned_data
    return render(request, "feedback.html", {"form": form, "submitted_data": submitted_data})

def  note_draft(request):
    if request.method == "POST":
        form = NoteDraftForm(request.POST)
        if form.is_valid():
            return redirect("feedback_page")
    else:
        form = NoteDraftForm()
    return render(request, "noteDraft.html", {"form": form})

