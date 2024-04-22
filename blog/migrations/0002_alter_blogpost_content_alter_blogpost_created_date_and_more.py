# Generated by Django 5.0.3 on 2024-04-04 18:06

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='content',
            field=models.TextField(verbose_name='Содержимое'),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата создания'),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='is_published',
            field=models.BooleanField(default=False, verbose_name='Признак публикации'),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='preview',
            field=models.ImageField(upload_to='previews/', verbose_name='Изображение'),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='slug',
            field=models.CharField(max_length=200, verbose_name='slug'),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='title',
            field=models.CharField(max_length=200, verbose_name='Заголовок'),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='views_count',
            field=models.IntegerField(default=0, verbose_name='Количество просмотров'),
        ),
    ]