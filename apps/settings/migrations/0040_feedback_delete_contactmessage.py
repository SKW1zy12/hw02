# Generated by Django 5.0 on 2023-12-19 00:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0039_contactmessage'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('message', models.TextField()),
            ],
            options={
                'verbose_name': 'Обратная связь',
                'verbose_name_plural': 'Обратная связь',
            },
        ),
        migrations.DeleteModel(
            name='ContactMessage',
        ),
    ]
