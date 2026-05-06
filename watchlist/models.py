from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

class Movie(models.Model):
    STATUS_CHOICES = [
        ('watchlist', 'Хочу посмотреть'),
        ('watching', 'Смотрю'),
        ('watched', 'Посмотрел'),
    ]

    title = models.CharField(max_length=255, verbose_name="Название фильма")
    genre = models.CharField(max_length=100, verbose_name="Жанр")
    release_year = models.PositiveIntegerField(verbose_name="Год выпуска")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='watchlist', verbose_name="Статус")
    rating = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(10)],
        null=True, blank=True,
        verbose_name="Личная оценка (1-10)"
    )
    date_added = models.DateTimeField(auto_now_add=True, verbose_name="Дата добавления")
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='movies', verbose_name="Пользователь-владелец")

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-date_added']
