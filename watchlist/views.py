from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from .models import Movie
from .forms import MovieForm, RegisterForm

from django.db import IntegrityError

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            try:
                user = form.save()
                login(request, user)
                return redirect('movie_list')
            except IntegrityError:
                form.add_error('username', 'Пользователь с таким именем уже существует.')
    else:
        form = RegisterForm()
    return render(request, 'registration/register.html', {'form': form})

from django.core.paginator import Paginator

@login_required
def movie_list(request):
    status_filter = request.GET.get('status')
    genre_filter = request.GET.get('genre')
    
    movies_queryset = Movie.objects.filter(owner=request.user)
    
    if status_filter:
        movies_queryset = movies_queryset.filter(status=status_filter)
    if genre_filter:
        movies_queryset = movies_queryset.filter(genre__icontains=genre_filter)
        
    paginator = Paginator(movies_queryset, 6) # По 6 фильмов на страницу
    page_number = request.GET.get('page')
    movies = paginator.get_page(page_number)
    
    genres = Movie.objects.filter(owner=request.user).values_list('genre', flat=True).distinct()
    
    return render(request, 'watchlist/movie_list.html', {
        'movies': movies,
        'genres': genres,
        'status_choices': Movie.STATUS_CHOICES
    })

@login_required
def movie_create(request):
    if request.method == 'POST':
        form = MovieForm(request.POST)
        if form.is_valid():
            movie = form.save(commit=False)
            movie.owner = request.user
            movie.save()
            return redirect('movie_list')
    else:
        form = MovieForm()
    return render(request, 'watchlist/movie_form.html', {'form': form, 'title': 'Добавить фильм'})

@login_required
def movie_update(request, pk):
    movie = get_object_or_404(Movie, pk=pk, owner=request.user)
    if request.method == 'POST':
        form = MovieForm(request.POST, instance=movie)
        if form.is_valid():
            form.save()
            return redirect('movie_list')
    else:
        form = MovieForm(instance=movie)
    return render(request, 'watchlist/movie_form.html', {'form': form, 'title': 'Редактировать фильм'})

@login_required
def movie_delete(request, pk):
    movie = get_object_or_404(Movie, pk=pk, owner=request.user)
    if request.method == 'POST':
        movie.delete()
        return redirect('movie_list')
    return render(request, 'watchlist/movie_confirm_delete.html', {'movie': movie})
