# Generated by Django 5.0.6 on 2024-06-09 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Paws', '0016_rename_adoption_status_dog_is_not_adopted'),
    ]

    operations = [
        migrations.AddField(
            model_name='shelter',
            name='iban',
            field=models.CharField(blank=True, max_length=34, null=True),
        ),
    ]
