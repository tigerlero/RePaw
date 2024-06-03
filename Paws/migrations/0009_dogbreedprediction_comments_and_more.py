# Generated by Django 5.0.6 on 2024-06-03 18:59

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Paws', '0008_health_allergies_health_blood_pressure_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='dogbreedprediction',
            name='comments',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='dogbreedprediction',
            name='confidence_threshold',
            field=models.FloatField(default=0.5),
        ),
        migrations.AddField(
            model_name='dogbreedprediction',
            name='image_processing_details',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='dogbreedprediction',
            name='location',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='dogbreedprediction',
            name='metadata',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='dogbreedprediction',
            name='model_used',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='dogbreedprediction',
            name='rating',
            field=models.IntegerField(blank=True, choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], null=True),
        ),
        migrations.AddField(
            model_name='dogbreedprediction',
            name='status',
            field=models.CharField(choices=[('pending', 'Pending'), ('verified', 'Verified'), ('disputed', 'Disputed')], default='pending', max_length=20),
        ),
        migrations.AddField(
            model_name='dogbreedprediction',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='dogbreedprediction',
            name='validation_status',
            field=models.BooleanField(default=False),
        ),
    ]
