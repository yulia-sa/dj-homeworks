# Generated by Django 2.1.1 on 2019-09-17 23:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phones', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='phone',
            name='slug',
            field=models.SlugField(default=models.CharField(max_length=200, verbose_name='Модель'), unique=True),
        ),
    ]
