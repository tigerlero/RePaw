# Generated by Django 5.0.6 on 2024-06-10 18:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Paws', '0020_alter_trainer_experience_years'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shelter',
            name='email',
        ),
        migrations.RemoveField(
            model_name='shelter',
            name='phone_number',
        ),
    ]