from django.db import models


class Car(models.Model):
    brand = models.CharField(max_length=50, verbose_name='Марка')
    model = models.CharField(max_length=50, verbose_name='Модель')

    def __str__(self):
        return f'{self.brand} {self.model}'

    def review_count(self):
        return Review.objects.filter(car=self).count()
    review_count.short_description = 'Количество отзывов'

    class Meta:
        verbose_name = 'Машина'
        verbose_name_plural = 'Машины'


class Review(models.Model):
    car = models.ForeignKey(Car, verbose_name='Машина', on_delete=models.CASCADE)
    title = models.CharField(max_length=100, verbose_name='Заголовок обзора')
    text = models.TextField()

    def __str__(self):
        return str(self.car) + ' ' + self.title

    class Meta:
        verbose_name = 'Обзор'
        verbose_name_plural = 'Обзоры'
