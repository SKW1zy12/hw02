# Generated by Django 5.0 on 2023-12-15 15:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0018_rename_friend2_frie'),
    ]

    operations = [
        migrations.RenameField(
            model_name='frie',
            old_name='friend_direction1',
            new_name='direction1',
        ),
        migrations.RenameField(
            model_name='frie',
            old_name='friend_image1',
            new_name='mage1',
        ),
        migrations.RenameField(
            model_name='frie',
            old_name='friend_name1',
            new_name='name1',
        ),
        migrations.RenameField(
            model_name='frie',
            old_name='friend_quote1',
            new_name='quote1',
        ),
    ]
