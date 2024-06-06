from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Breed(models.Model):
    name = models.CharField(max_length=100)
    characteristics = models.TextField()


class Food(models.Model):
    name = models.CharField(max_length=100)
    ingredients = models.TextField()
    recommended_breeds = models.ManyToManyField(Breed)
    nutritional_content = models.TextField(default='Not specified',
                                           help_text="Detailed nutritional content of the food")
    suitable_for_age_groups = models.CharField(max_length=100, default='All',
                                               help_text="Age groups like puppy, adult, senior")
    dietary_restrictions = models.TextField(blank=True, help_text="Any dietary restrictions this food addresses")
    weight_management = models.BooleanField(default=False, help_text="Is this food suitable for weight management?")
    dental_health = models.BooleanField(default=False, help_text="Is this food beneficial for dental health?")
    skin_and_coat_health = models.BooleanField(default=False,
                                               help_text="Is this food beneficial for skin and coat health?")
    digestion_health = models.BooleanField(default=False, help_text="Is this food beneficial for digestion health?")

    def __str__(self):
        return self.name


class FriendlySpot(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    description = models.TextField()
    dog_friendly = models.BooleanField(default=True)


class Owner(models.Model):
    number_of_dogs = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.number_of_dogs}"


class Shelter(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name


class Doctor(models.Model):
    specialty = models.CharField(max_length=100)
    clinic_address = models.CharField(max_length=200)

    def __str__(self):
        return f"Speciality and address. {self.specialty} {self.clinic_address}"


class Event(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateTimeField()
    location = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Dog(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    breed = models.CharField(max_length=100)
    description = models.TextField()
    adoption_status = models.BooleanField(default=False)
    owner = models.ForeignKey(Owner, on_delete=models.SET_NULL, null=True, blank=True)
    shelter = models.ForeignKey(Shelter, on_delete=models.SET_NULL, null=True, blank=True)
    weight = models.FloatField(null=True, blank=True)
    height = models.FloatField(null=True, blank=True)
    color = models.CharField(max_length=100, null=True, blank=True)
    eye_color = models.CharField(max_length=50, null=True, blank=True)
    last_known_location = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.name


class Microchip(models.Model):
    dog = models.OneToOneField(Dog, on_delete=models.CASCADE, primary_key=True)
    microchip_number = models.CharField(max_length=15, unique=True)
    implant_date = models.DateField()
    location = models.CharField(max_length=100)  # Location where the chip was implanted (e.g., vet clinic)

    def __str__(self):
        return f"Microchip {self.microchip_number} for {self.dog.name}"


class Walk(models.Model):
    dog = models.ForeignKey(Dog, on_delete=models.CASCADE)
    walker = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    date = models.DateTimeField()
    duration = models.DurationField()
    sitter_required = models.BooleanField(default=False)

    def __str__(self):
        return f"Walk for {self.dog.name} on {self.date}"


class Command(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Training(models.Model):
    dog = models.ForeignKey(Dog, on_delete=models.CASCADE)
    training_type = models.CharField(max_length=100)
    trainer_name = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    date = models.DateTimeField()
    notes = models.TextField()
    commands = models.ManyToManyField(Command, blank=True)

    def __str__(self):
        return f"{self.training_type} training for {self.dog.name} on {self.date}"


class Health(models.Model):
    dog = models.ForeignKey(Dog, on_delete=models.CASCADE)
    is_sick = models.BooleanField(default=False)
    checkup_date = models.DateTimeField()
    weight = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    temperature = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    heart_rate = models.PositiveIntegerField(null=True, blank=True)
    blood_pressure = models.CharField(max_length=20, null=True, blank=True)
    respiratory_rate = models.PositiveIntegerField(null=True, blank=True)
    dental_health = models.CharField(max_length=100, null=True, blank=True)
    skin_condition = models.TextField(blank=True)
    digestive_health = models.TextField(blank=True)
    musculoskeletal_health = models.TextField(blank=True)
    vision = models.CharField(max_length=100, null=True, blank=True)
    hearing = models.CharField(max_length=100, null=True, blank=True)
    allergies = models.TextField(blank=True)
    notes = models.TextField(blank=True)
    veterinarian = models.CharField(max_length=100)

    def __str__(self):
        return f"Health record of {self.dog.name}"


class Appointment(models.Model):
    dog = models.ForeignKey(Dog, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    date = models.DateTimeField()
    reason = models.TextField()

    def __str__(self):
        return f"{self.dog.name} with {self.doctor}"


class VaccinationRecord(models.Model):
    dog = models.ForeignKey(Dog, on_delete=models.CASCADE)
    vaccine_name = models.CharField(max_length=100)
    date_given = models.DateField()
    next_due_date = models.DateField()

    def __str__(self):
        return f"{self.dog.name} - {self.vaccine_name}"


class DogBreedPrediction(models.Model):
    image = models.ImageField(upload_to='predictions/')
    predicted_breed = models.CharField(max_length=100)
    confidence = models.FloatField()
    prediction_date = models.DateTimeField(auto_now_add=True)
    related_dog = models.ForeignKey(Dog, on_delete=models.SET_NULL, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)], null=True, blank=True)
    comments = models.TextField(blank=True)
    model_used = models.CharField(max_length=100, null=True, blank=True)
    image_processing_details = models.TextField(blank=True)
    validation_status = models.BooleanField(default=False)
    location = models.CharField(max_length=100, null=True, blank=True)
    status = models.CharField(max_length=20,
                              choices=[('pending', 'Pending'), ('verified', 'Verified'), ('disputed', 'Disputed')],
                              default='pending')
    confidence_threshold = models.FloatField(default=0.5)
    metadata = models.TextField(blank=True)

    def __str__(self):
        return f"Prediction for {self.related_dog.name} ({self.prediction_date})"


class UserProfile(models.Model):
    ROLE_CHOICES = (
        ('owner', 'Owner'),
        ('shelter', 'Shelter'),
        ('general', 'General'),
    )
    first_name = models.CharField(max_length=100, default="")
    last_name = models.CharField(max_length=100, default="")
    email = models.EmailField(unique=True, null=True)
    phone_number = models.CharField(max_length=15, default="")

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    owner = models.OneToOneField(Owner, on_delete=models.SET_NULL, null=True, blank=True)

    shelter = models.OneToOneField(Shelter, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.user.username} - {self.role}"


class Groomer(models.Model):
    groomer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    address = models.CharField(max_length=255)


class Grooming(models.Model):
    dog = models.ForeignKey(Dog, on_delete=models.CASCADE)
    groomer = models.ForeignKey(Groomer, on_delete=models.CASCADE)
    date = models.DateTimeField()
    notes = models.TextField()
