# Generated by Django 5.0.3 on 2024-04-04 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_blogpost_content_alter_blogpost_created_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='is_published',
            field=models.BooleanField(default=True, verbose_name='Признак публикации'),
        ),
    ]
