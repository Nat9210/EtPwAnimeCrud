# Generated by Django 5.0.7 on 2024-07-19 04:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('taskcrud', '0003_media_numero_episodios'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='media',
            name='capitulo',
        ),
    ]