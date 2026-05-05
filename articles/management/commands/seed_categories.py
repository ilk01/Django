from django.core.management.base import BaseCommand
from articles.models import Category
from django.utils.text import slugify

class Command(BaseCommand):
    help = 'Seeds initial categories'

    def handle(self, *args, **options):
        categories = ['Backend', 'Frontend', 'AI', 'Cyber security', 'Cyber sport', 'Game Development']
        for cat_name in categories:
            Category.objects.get_or_create(
                name=cat_name,
                defaults={'slug': slugify(cat_name)}
            )
        self.stdout.write(self.style.SUCCESS('Successfully seeded categories'))
