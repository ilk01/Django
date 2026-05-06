

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_profile_bio_profile_birth_date_profile_location_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='location',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='website',
        ),
    ]
