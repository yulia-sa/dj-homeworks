# Generated by Django 2.1.1 on 2019-09-18 00:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phones', '0002_phone_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phone',
            name='price',
            field=models.DecimalField(decimal_places=0, max_digits=10, verbose_name='Стоимость'),
        ),
    ]