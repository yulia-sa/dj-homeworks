# Generated by Django 2.1.5 on 2019-10-01 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='img',
        ),
        migrations.AddField(
            model_name='article',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='image/%Y/%m/%d/', verbose_name='Изображение'),
        ),
    ]
