# Generated by Django 5.0.6 on 2024-06-13 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Paws', '0022_trainer_postal_code_userprofile_city'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='city',
            field=models.CharField(default='', max_length=100, null=True),
        ),
    ]