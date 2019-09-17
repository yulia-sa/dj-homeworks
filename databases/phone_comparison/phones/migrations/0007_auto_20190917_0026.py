# Generated by Django 2.1.5 on 2019-09-17 00:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phones', '0006_auto_20190917_0005'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applefeatures',
            name='barometer',
            field=models.BooleanField(verbose_name='Барометр'),
        ),
        migrations.AlterField(
            model_name='applefeatures',
            name='face_id',
            field=models.BooleanField(verbose_name='Face ID'),
        ),
        migrations.AlterField(
            model_name='applefeatures',
            name='three_axis_gyroscope',
            field=models.BooleanField(verbose_name='Трёхосевой гироскоп'),
        ),
        migrations.AlterField(
            model_name='applefeatures',
            name='unblock_by_face',
            field=models.BooleanField(verbose_name='Разблокировка по лицу'),
        ),
        migrations.AlterField(
            model_name='ginzzufeatures',
            name='built_in_flashlight',
            field=models.BooleanField(verbose_name='Встроенный фонарик'),
        ),
        migrations.AlterField(
            model_name='ginzzufeatures',
            name='geomagnetic_sensor',
            field=models.BooleanField(verbose_name='Геомагнитный датчик'),
        ),
        migrations.AlterField(
            model_name='ginzzufeatures',
            name='shockproof_case',
            field=models.BooleanField(verbose_name='Ударопрочный корпус'),
        ),
        migrations.AlterField(
            model_name='ginzzufeatures',
            name='voice_recorder',
            field=models.BooleanField(verbose_name='Диктофон'),
        ),
        migrations.AlterField(
            model_name='motorolafeatures',
            name='headphone_jack_3_5',
            field=models.BooleanField(verbose_name='Разъем для подключения наушников 3.5 мм'),
        ),
        migrations.AlterField(
            model_name='phone',
            name='front_camera',
            field=models.IntegerField(verbose_name='Фронтальная камера (Мп)'),
        ),
        migrations.AlterField(
            model_name='phone',
            name='main_сamera',
            field=models.IntegerField(verbose_name='Основная камера (Мп)'),
        ),
        migrations.AlterField(
            model_name='phone',
            name='price',
            field=models.IntegerField(verbose_name='Стоимость (руб.)'),
        ),
        migrations.AlterField(
            model_name='phone',
            name='screen_size',
            field=models.FloatField(verbose_name='Размер дисплея (в дюймах)'),
        ),
        migrations.AlterField(
            model_name='phone',
            name='weight',
            field=models.IntegerField(verbose_name='Вес (г)'),
        ),
    ]
