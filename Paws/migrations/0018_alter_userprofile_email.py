# Generated by Django 5.0.6 on 2024-06-10 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Paws', '0017_shelter_iban'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
    ]
