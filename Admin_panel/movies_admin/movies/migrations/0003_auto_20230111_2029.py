# Generated by Django 3.2 on 2023-01-11 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_auto_20221225_1937'),
    ]

    operations = [
        migrations.AddIndex(
            model_name='genrefilmwork',
            index=models.Index(fields=['created'], name='genre_film_work_created_idx'),
        ),
        migrations.AddIndex(
            model_name='personfilmwork',
            index=models.Index(fields=['created'], name='person_film_work_created_idx'),
        ),
    ]
