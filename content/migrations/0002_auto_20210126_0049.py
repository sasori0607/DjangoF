# Generated by Django 3.1.5 on 2021-01-25 22:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='news',
            options={'verbose_name': 'Новость', 'verbose_name_plural': 'Новости'},
        ),
        migrations.AddField(
            model_name='news',
            name='text',
            field=models.TextField(default=-1, verbose_name='Основной текст'),
            preserve_default=False,
        ),
    ]
