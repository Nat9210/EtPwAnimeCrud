# Generated by Django 5.0.7 on 2024-07-19 03:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taskcrud', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Episodio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('numero', models.IntegerField()),
                ('descripcion', models.TextField(blank=True, null=True)),
                ('archivo', models.FileField(blank=True, null=True, upload_to='episodios/')),
                ('duracion', models.DurationField(blank=True, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='media',
            name='episodios',
            field=models.ManyToManyField(blank=True, to='taskcrud.episodio'),
        ),
    ]
