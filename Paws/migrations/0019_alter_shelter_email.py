# Generated by Django 5.0.6 on 2024-06-10 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Paws', '0018_alter_userprofile_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shelter',
            name='email',
            field=models.EmailField(max_length=254),
        ),
    ]