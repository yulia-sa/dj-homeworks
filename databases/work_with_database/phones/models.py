from django.db import models
from django.utils.text import slugify


class Phone(models.Model):
    id = models.IntegerField(verbose_name="ID", primary_key=True)
    name = models.CharField(max_length=200, verbose_name="Модель")
    image = models.URLField(verbose_name="Ссылка на изображение")
    price = models.DecimalField(verbose_name="Стоимость", max_digits=10, decimal_places=0)
    release_date = models.DateField(verbose_name="Дата выхода")
    lte_exists = models.BooleanField(verbose_name="Наличие LTE")
    slug = models.SlugField(unique=True, default=name)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Phone, self).save(*args, **kwargs)
