# Generated by Django 5.0 on 2023-12-13 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Slide',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
                ('descriptions', models.CharField(max_length=255, verbose_name='Описание')),
                ('image', models.ImageField(upload_to='slide_image')),
            ],
        ),
    ]
