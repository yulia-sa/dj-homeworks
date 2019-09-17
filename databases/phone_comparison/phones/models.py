from django.db import models


class Phone(models.Model):
    name = models.CharField(max_length=200, verbose_name="Модель")
    price = models.IntegerField(verbose_name="Стоимость (руб.)")
    operating_system = models.CharField(max_length=200, verbose_name="Операционная система")
    operating_memory_capacity = models.IntegerField(verbose_name="Объем оперативной памяти (Гб)")
    storage_capacity = models.IntegerField(verbose_name="Объем встроенной памяти (Гб)")
    chip = models.CharField(max_length=200, verbose_name="Процессор")
    screen_size = models.FloatField(verbose_name="Размер дисплея (в дюймах)")
    screen_resolution = models.CharField(max_length=200, verbose_name="Разрешение дисплея")
    main_сamera = models.IntegerField(verbose_name="Основная камера (Мп)")
    flash = models.BooleanField(verbose_name="Вспышка")
    autofocus = models.BooleanField(verbose_name="Автофокусировка")
    front_camera = models.IntegerField(verbose_name="Фронтальная камера (Мп)")
    sim_cards_quantity = models.IntegerField(verbose_name="Количество SIM-карт")
    sim_card_type = models.CharField(max_length=200, verbose_name="Тип SIM-карты")
    mp3_player = models.BooleanField(verbose_name="MP3 плеер")
    fm_radio = models.BooleanField(verbose_name="FM-радио")
    usb = models.BooleanField(verbose_name="Интерфейс USB")
    water_dust_resistance = models.BooleanField(verbose_name="Защита от пыли и влаги")
    wireless_charging = models.BooleanField(verbose_name="Функция беспроводной зарядки")
    weight = models.IntegerField(verbose_name="Вес (г)")
    country = models.CharField(max_length=200, verbose_name="Страна")


class AppleFeatures(models.Model):
    feature = models.CharField(max_length=200, default=None, blank=True, null=True)


class GinzzuFeatures(models.Model):
    feature = models.CharField(max_length=200, default=None, blank=True, null=True)


class MotorolaFeatures(models.Model):
    feature = models.CharField(max_length=200, default=None, blank=True, null=True)
