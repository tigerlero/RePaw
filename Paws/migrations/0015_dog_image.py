# Generated by Django 5.0.6 on 2024-06-09 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Paws', '0014_userprofile_is_trainer_trainer_userprofile_trainer'),
    ]

    operations = [
        migrations.AddField(
            model_name='dog',
            name='image',
            field=models.ImageField(blank=True, default='breed_images/default.jpg', null=True, upload_to='dog_images/'),
        ),
    ]