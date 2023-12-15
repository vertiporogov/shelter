from django.db import models

NULLABLE = {'blank': True, 'null': True}

class Dog(models.Model):
    name = models.CharField(max_length=200, verbose_name='Кличка')
    category = models.CharField(max_length=200, verbose_name='Кличка')
    photo = models.ImageField(upload_to='dogs/', **NULLABLE, verbose_name='фото')
    birth_day = models.DateField(**NULLABLE, verbose_name='Дата рождения')


    def __str__(self):
        return f'{self.name} ({self.category})'


    class Meta:
        verbose_name = 'собака'
        verbose_name_plural = 'собаки'
