# Generated by Django 5.0.6 on 2024-06-06 12:23

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Paws', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Command',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('specialty', models.CharField(max_length=100)),
                ('clinic_address', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('date', models.DateTimeField()),
                ('location', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Microchip',
            fields=[
                ('dog', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='Paws.dog')),
                ('microchip_number', models.CharField(max_length=15, unique=True)),
                ('implant_date', models.DateField()),
                ('location', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Owner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number_of_dogs', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Shelter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=200)),
                ('phone_number', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='dog',
            name='color',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='dog',
            name='eye_color',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='dog',
            name='height',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='dog',
            name='last_known_location',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='dog',
            name='weight',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='food',
            name='dental_health',
            field=models.BooleanField(default=False, help_text='Is this food beneficial for dental health?'),
        ),
        migrations.AddField(
            model_name='food',
            name='dietary_restrictions',
            field=models.TextField(blank=True, help_text='Any dietary restrictions this food addresses'),
        ),
        migrations.AddField(
            model_name='food',
            name='digestion_health',
            field=models.BooleanField(default=False, help_text='Is this food beneficial for digestion health?'),
        ),
        migrations.AddField(
            model_name='food',
            name='nutritional_content',
            field=models.TextField(default='Not specified', help_text='Detailed nutritional content of the food'),
        ),
        migrations.AddField(
            model_name='food',
            name='skin_and_coat_health',
            field=models.BooleanField(default=False, help_text='Is this food beneficial for skin and coat health?'),
        ),
        migrations.AddField(
            model_name='food',
            name='suitable_for_age_groups',
            field=models.CharField(default='All', help_text='Age groups like puppy, adult, senior', max_length=100),
        ),
        migrations.AddField(
            model_name='food',
            name='weight_management',
            field=models.BooleanField(default=False, help_text='Is this food suitable for weight management?'),
        ),
        migrations.AddField(
            model_name='health',
            name='allergies',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='health',
            name='blood_pressure',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='health',
            name='dental_health',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='health',
            name='digestive_health',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='health',
            name='hearing',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='health',
            name='heart_rate',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='health',
            name='is_sick',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='health',
            name='musculoskeletal_health',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='health',
            name='respiratory_rate',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='health',
            name='skin_condition',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='health',
            name='temperature',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AddField(
            model_name='health',
            name='vision',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='health',
            name='weight',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AddField(
            model_name='training',
            name='trainer_name',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='walk',
            name='sitter_required',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='health',
            name='notes',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='walk',
            name='walker',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='training',
            name='commands',
            field=models.ManyToManyField(blank=True, to='Paws.command'),
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('reason', models.TextField()),
                ('dog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Paws.dog')),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Paws.doctor')),
            ],
        ),
        migrations.CreateModel(
            name='DogBreedPrediction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='predictions/')),
                ('predicted_breed', models.CharField(max_length=100)),
                ('confidence', models.FloatField()),
                ('prediction_date', models.DateTimeField(auto_now_add=True)),
                ('rating', models.IntegerField(blank=True, choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], null=True)),
                ('comments', models.TextField(blank=True)),
                ('model_used', models.CharField(blank=True, max_length=100, null=True)),
                ('image_processing_details', models.TextField(blank=True)),
                ('validation_status', models.BooleanField(default=False)),
                ('location', models.CharField(blank=True, max_length=100, null=True)),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('verified', 'Verified'), ('disputed', 'Disputed')], default='pending', max_length=20)),
                ('confidence_threshold', models.FloatField(default=0.5)),
                ('metadata', models.TextField(blank=True)),
                ('related_dog', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Paws.dog')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Groomer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('address', models.CharField(max_length=255)),
                ('groomer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Grooming',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('notes', models.TextField()),
                ('dog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Paws.dog')),
                ('groomer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Paws.groomer')),
            ],
        ),
        migrations.AddField(
            model_name='dog',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Paws.owner'),
        ),
        migrations.AddField(
            model_name='dog',
            name='shelter',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Paws.shelter'),
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(default='', max_length=100)),
                ('last_name', models.CharField(default='', max_length=100)),
                ('email', models.EmailField(max_length=254, null=True, unique=True)),
                ('phone_number', models.CharField(default='', max_length=15)),
                ('role', models.CharField(choices=[('owner', 'Owner'), ('shelter', 'Shelter'), ('general', 'General')], max_length=10)),
                ('owner', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Paws.owner')),
                ('shelter', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Paws.shelter')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='VaccinationRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vaccine_name', models.CharField(max_length=100)),
                ('date_given', models.DateField()),
                ('next_due_date', models.DateField()),
                ('dog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Paws.dog')),
            ],
        ),
    ]