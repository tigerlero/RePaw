# Generated by Django 5.0.6 on 2024-06-08 23:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Paws', '0007_userprofile_profile_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='breed',
            name='coat_length',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='breed',
            name='exercise_needs',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='breed',
            name='health_issues',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='breed',
            name='lifespan',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='breed',
            name='origin',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='breed',
            name='shedding',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='breed',
            name='size',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='breed',
            name='special_needs',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='breed',
            name='temperament',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='breed',
            name='trainability',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
