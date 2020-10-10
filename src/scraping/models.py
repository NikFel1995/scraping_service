from django.db import models

from scraping.utils import from_cyrillic_to_eng


class City(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name='Название')
    slug = models.CharField(max_length=50, unique=True, blank=True)

    class Meta:
        verbose_name = 'Город'  # Название модели, в единственном числе
        verbose_name_plural = 'Города'  # Название модели в множественном числе

    def __str__(self):
        return '%s' % self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = from_cyrillic_to_eng(self.name)
        super().save(*args, **kwargs)


class Language(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name='Язык программирования')
    slug = models.CharField(max_length=50, unique=True, blank=True)

    class Meta:
        verbose_name = 'Язык программирования'  # Название модели, в единственном числе
        verbose_name_plural = 'Языки программирования'  # Название модели в множественном числе

    def __str__(self):
        return '%s' % self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = from_cyrillic_to_eng(self.name)
        super().save(*args, **kwargs)


class Vacancy(models.Model):
    url = models.URLField(unique=True)
    title = models.CharField(max_length=250, verbose_name='Вакансия')
    company = models.CharField(max_length=250, verbose_name='Компания')
    description = models.TextField(verbose_name='Описание')
    city = models.ForeignKey(City, on_delete=models.CASCADE, verbose_name='Город')
    language = models.ForeignKey(Language, on_delete=models.CASCADE, verbose_name='Язык программирования')
    timestamp = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = 'Вакансия'  # Название модели, в единственном числе
        verbose_name_plural = 'Вакансии'  # Название модели в множественном числе

    def __str__(self):
        return '%s' % self.title
