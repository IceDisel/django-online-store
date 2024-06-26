from django.db import models

from users.models import User


class Category(models.Model):
    name = models.CharField(max_length=200, verbose_name='Наименование')
    description = models.TextField(verbose_name='Описание')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['name']

    def __str__(self):
        return self.name


NULLABLE = {'blank': True, 'null': True}


class Product(models.Model):
    name = models.CharField(max_length=200, verbose_name='Наименование')
    description = models.TextField(verbose_name='Описание')
    image = models.ImageField(upload_to='products/%Y/%m/%d', verbose_name='Изображение', **NULLABLE)
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE, verbose_name='Категория')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена за покупку')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата последнего изменения')
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, verbose_name='Владелец', **NULLABLE)
    is_published = models.BooleanField(default=False, verbose_name='Опубликовано')

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ['name']

        permissions = [
            ('set_published_status', 'Can edit product published status',),
            ('can_edit_description', 'Can edit product description',),
            ('can_edit_category', 'Can edit product category',),
        ]

    def __str__(self):
        return self.name


class Version(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Продукт')
    number_ver = models.CharField(max_length=50, **NULLABLE, verbose_name='Номер версии')
    name_ver = models.CharField(max_length=100, verbose_name='Название версии')
    activ_ver = models.BooleanField(default=False, verbose_name='Активная версия')

    def __str__(self):
        return self.name_ver

    class Meta:
        verbose_name = 'Версия'
        verbose_name_plural = 'Версии'
