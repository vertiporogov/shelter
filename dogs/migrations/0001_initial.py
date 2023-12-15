# Generated by Django 5.0 on 2023-12-15 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Кличка')),
                ('category', models.CharField(max_length=200, verbose_name='Кличка')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='dogs/', verbose_name='фото')),
                ('birth_day', models.DateField(blank=True, null=True, verbose_name='Дата рождения')),
            ],
            options={
                'verbose_name': 'собака',
                'verbose_name_plural': 'собаки',
            },
        ),
    ]