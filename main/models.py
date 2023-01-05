from django.db import models


class MainPicture(models.Model):
    image = models.ImageField(upload_to='mainpictures/', verbose_name='Изображение')

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Фото на главную страницу'



class MainCatalog(models.Model):
    categoty = models.URLField(max_length=300, verbose_name='Категория транспорта')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class AboutUs(models.Model):
    title = models.CharField(max_length=127,verbose_name='Заголовок')
    description = models.TextField(verbose_name='Описание')

    class Meta:
        verbose_name = 'Про нас'
        verbose_name_plural = 'Про нас'


class Connection(models.Model):
    number = models.CharField(max_length=14, verbose_name='номер телефона')
    adress = models.CharField(max_length=127, verbose_name='Наш адресс')
    email = models.EmailField(max_length=127, verbose_name='Электронная почта')
    social_network = models.URLField(max_length=500, verbose_name='Соц. сети')

    class Meta:
        verbose_name = 'Контакт/Связь'
        verbose_name_plural = 'Контакты/Связи'

