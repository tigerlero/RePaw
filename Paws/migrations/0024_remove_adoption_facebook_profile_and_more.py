# Generated by Django 5.0.6 on 2024-06-13 16:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Paws', '0023_alter_userprofile_city'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='adoption',
            name='facebook_profile',
        ),
        migrations.RemoveField(
            model_name='adoption',
            name='home_phone',
        ),
        migrations.RemoveField(
            model_name='adoption',
            name='instagram_profile',
        ),
        migrations.RemoveField(
            model_name='adoption',
            name='work_phone',
        ),
    ]
