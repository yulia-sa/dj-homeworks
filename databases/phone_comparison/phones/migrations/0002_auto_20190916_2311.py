# Generated by Django 2.0.5 on 2019-09-16 23:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phones', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Apple',
            new_name='AppleFeatures',
        ),
        migrations.RenameModel(
            old_name='Ginzzu',
            new_name='GinzzuFeatures',
        ),
        migrations.RenameModel(
            old_name='Motorola',
            new_name='MotorolaFeatures',
        ),
        migrations.AlterField(
            model_name='phone',
            name='usb',
            field=models.TextField(),
        ),
    ]