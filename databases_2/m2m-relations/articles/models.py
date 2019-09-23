from django.db import models


class Article(models.Model):

    title = models.CharField(max_length=256, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    published_at = models.DateTimeField(verbose_name='Дата публикации')
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение')

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def __str__(self):
        return self.title


class Scope(models.Model):

    name = models.CharField(max_length=100, verbose_name='Название Раздела')

    class Meta:
        verbose_name = 'Раздел'
        verbose_name_plural = 'Разделы'
        ordering = ['name']  

    def __str__(self):
        return self.name


class ArticleScope(models.Model):

    article = models.ForeignKey('Article', on_delete=models.CASCADE)
    scope = models.ForeignKey('Scope', verbose_name='Раздел', on_delete=models.CASCADE)
    is_main = models.BooleanField(verbose_name='Основная категория')

    class Meta:
        verbose_name = 'Тематика статьи'
        verbose_name_plural = 'Тематики статьи'
        ordering = ['-is_main', 'scope']
