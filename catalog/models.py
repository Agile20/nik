from django.db import models

class Car(models.Model):
    name = models.CharField(max_length=127, verbose_name='Модель машины')
    available = models.CharField(max_length=127, verbose_name='Наличие/Под заказ')
    torque = models.CharField(max_length=127,verbose_name='Крутящий момент Нм')
    max_speed = models.CharField(max_length=127, verbose_name='Максимальная скорость')
    type_kuz = models.CharField(max_length=127, verbose_name='Тип кузова')
    type_priv= models.CharField(max_length=127, verbose_name='Тип привода')
    mileage = models.CharField(max_length=127,verbose_name='Пробег')
    year_release = models.CharField(max_length=127,verbose_name='Год выпуска')
    battery_capacity = models.CharField(max_length=127,verbose_name='Емкость батареи')
    price = models.CharField(max_length=127, verbose_name='Цена')
    description = models.TextField(verbose_name='Описание')


class Bike(models.Model):
    name = models.CharField(max_length=127, verbose_name='Модель байка')
    available = models.CharField(max_length=127, verbose_name='Наличие/Под заказ')
    torque = models.CharField(max_length=127,verbose_name='Крутящий момент Нм')
    max_speed = models.CharField(max_length=127, verbose_name='Максимальная скорость')
    mileage = models.CharField(max_length=127,verbose_name='Пробег')
    year_release = models.CharField(max_length=127,verbose_name='Год выпуска')
    battery_capacity = models.CharField(max_length=127,verbose_name='Емкость батареи')
    price = models.CharField(max_length=127, verbose_name='Цена')
    description = models.TextField(verbose_name='Описание')


class OtherTransport(models.Model):
    name = models.CharField(max_length=127, verbose_name='Модель эл.транспорта')
    available = models.CharField(max_length=127, verbose_name='Наличие/Под заказ')
    torque = models.CharField(max_length=127,verbose_name='Крутящий момент Нм')
    max_speed = models.CharField(max_length=127, verbose_name='Максимальная скорость')
    mileage = models.CharField(max_length=127,verbose_name='Пробег')
    year_release = models.CharField(max_length=127,verbose_name='Год выпуска')
    battery_capacity = models.CharField(max_length=127,verbose_name='Емкость батареи')
    price = models.CharField(max_length=127, verbose_name='Цена')
    description = models.TextField(verbose_name='Описание')