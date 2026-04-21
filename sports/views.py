from django.shortcuts import render


def home(request):
    """Главная страница"""
    return render(request, 'sports/home.html', {'title': 'Главная'})


def football(request):
    """Раздел Футбол"""
    return render(request, 'sports/football.html', {'title': 'Футбол'})


def hockey(request):
    """Раздел Хоккей"""
    return render(request, 'sports/hockey.html', {'title': 'Хоккей'})


def basketball(request):
    """Раздел Баскетбол"""
    return render(request, 'sports/basketball.html', {'title': 'Баскетбол'})
