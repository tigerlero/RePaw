# Generated by Django 5.0.6 on 2024-06-09 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Paws', '0011_breed_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Testimonial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('author', models.CharField(max_length=100)),
            ],
        ),
    ]