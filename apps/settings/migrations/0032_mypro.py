# Generated by Django 5.0 on 2023-12-16 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0031_delete_mypro_rename_created_at_blogpost_created'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mypro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('projects', models.CharField(max_length=255, verbose_name='Число проектов')),
                ('hours_work', models.CharField(max_length=255, verbose_name='Число время работ')),
                ('ofiices', models.CharField(max_length=255, verbose_name='Число офицов')),
                ('clients', models.CharField(max_length=255, verbose_name='Число клиентов')),
            ],
            options={
                'verbose_name': 'Мои проекты',
                'verbose_name_plural': 'Мои проекты',
            },
        ),
    ]
