from django.db import models


class Modell(models.Model):
    name = models.CharField(max_length=127, verbose_name='Название')
    price = models.CharField(max_length=127,  verbose_name='Цена')
    description = models.TextField(verbose_name='Описание')
    available = models.CharField(max_length=123, verbose_name='Наличие')
    
    class Meta:
        abstract =  True


class SpareParts(Modell):
    class Meta:
        verbose_name = 'Запчасть'
        verbose_name_plural = 'Запчасти' 



class PowerPlant(Modell):
    class Meta:
        verbose_name = 'Электростанция'
        verbose_name_plural = 'Электростанции'