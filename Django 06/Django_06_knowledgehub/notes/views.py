from django.http import HttpResponse, HttpRequest
from django.shortcuts import render

# Create your views here.

def home(request: HttpRequest) -> HttpResponse:
    return HttpResponse("Knowledge Hub Home Page.")


def notes_list(request: HttpRequest)-> HttpResponse:
    return HttpResponse("Notes List (coming soon).")
