from django.db import migrations

def create_default_categories(apps, schema_editor):
    Category = apps.get_model('articles', 'Category')
    categories = [
        ('Посты', 'posts'),
        ('Новости', 'news'),
        ('Бэкенд', 'backend'),
        ('Фронтенд', 'frontend'),
        ('Мобильная разработка', 'mobile-development'),
        ('Геймдев', 'gamedev'),
        ('Тестирование', 'testing'),
        ('AI и ML', 'ai'),
        ('Промышленная инженерия', 'industrial-engineering'),
        ('Киберспорт', 'cybersport'),
    ]
    for name, slug in categories:
        # Используем update_or_create чтобы избежать конфликтов UNIQUE при повторном запуске
        Category.objects.update_or_create(
            slug=slug,
            defaults={'name': name}
        )

def remove_default_categories(apps, schema_editor):
    pass

class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_article_view_count'),
    ]

    operations = [
        migrations.RunPython(create_default_categories, remove_default_categories),
    ]
