# Generated by Django 2.0.5 on 2019-09-16 22:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Apple',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('face_id', models.BooleanField()),
                ('unblock_by_face', models.BooleanField()),
                ('barometer', models.BooleanField()),
                ('three_axis_gyroscope', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Ginzzu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('voice_recorder', models.BooleanField()),
                ('geomagnetic_sensor', models.BooleanField()),
                ('shockproof_case', models.BooleanField()),
                ('built_in_flashlight', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Motorola',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('headphone_jack_3_5', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('price', models.IntegerField()),
                ('operating_system', models.TextField()),
                ('operating_memory_capacity', models.IntegerField()),
                ('storage_capacity', models.IntegerField()),
                ('chip', models.TextField()),
                ('screen_size', models.IntegerField()),
                ('screen_resolution', models.TextField()),
                ('main_сamera', models.IntegerField()),
                ('flash', models.BooleanField()),
                ('autofocus', models.BooleanField()),
                ('front_camera', models.IntegerField()),
                ('sim_cards_quantity', models.IntegerField()),
                ('sim_card_type', models.TextField()),
                ('mp3_player', models.BooleanField()),
                ('fm_radio', models.BooleanField()),
                ('usb', models.BooleanField()),
                ('water_dust_resistance', models.BooleanField()),
                ('wireless_charging', models.BooleanField()),
                ('weight', models.IntegerField()),
                ('country', models.TextField()),
            ],
        ),
    ]
