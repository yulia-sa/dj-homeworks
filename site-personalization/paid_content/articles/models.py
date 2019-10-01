from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    name = models.CharField('Имя', max_length=100)
    is_subscribed = models.BooleanField(default=False, verbose_name='Есть подписка?')

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return str(self.name)


class Article(models.Model):
    title = models.CharField(verbose_name='Заголовок', max_length=200)
    image = models.FileField(null=True, blank=True, verbose_name='Изображение', upload_to='media/')
    text = models.TextField(verbose_name='Текст статьи')
    is_paid = models.BooleanField(default=False, verbose_name='Платная статья')

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def __str__(self):
        return self.title
