# Generated by Django 5.0 on 2023-12-16 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0024_rename_month_teacher_teach_month_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='teach_name',
            field=models.CharField(max_length=155, verbose_name='Имя учителя'),
        ),
    ]
