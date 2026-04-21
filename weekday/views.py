from django.http import HttpResponse
from datetime import datetime


def current_day(request):
    days = ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресенье']
    today = days[datetime.now().weekday()]
    return HttpResponse(f"Сегодня: {today}")
