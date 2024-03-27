# Generated by Django 5.0.3 on 2024-03-27 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_product_manufactured_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='manufactured_at',
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='products/%Y/%m/%d', verbose_name='Изображение'),
        ),
    ]
