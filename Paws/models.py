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


class FriendlySpot(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    description = models.TextField()
    dog_friendly = models.BooleanField(default=True)


class Owner(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Shelter(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name


class Doctor(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    specialty = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    clinic_address = models.CharField(max_length=200)

    def __str__(self):
        return f"Dr. {self.first_name} {self.last_name}"


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
    walker = models.CharField(max_length=100)
    date = models.DateTimeField()
    duration = models.DurationField()


class Training(models.Model):
    dog = models.ForeignKey(Dog, on_delete=models.CASCADE)
    training_type = models.CharField(max_length=100)
    date = models.DateTimeField()
    notes = models.TextField()


class Health(models.Model):
    dog = models.ForeignKey(Dog, on_delete=models.CASCADE)
    checkup_date = models.DateTimeField()
    notes = models.TextField()
    veterinarian = models.CharField(max_length=100)


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

    def __str__(self):
        return f"Prediction: {self.predicted_breed} with confidence {self.confidence}"


class PredictionRating(models.Model):
    prediction = models.ForeignKey(DogBreedPrediction, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField()  # Assuming rating is an integer, e.g., 1-5
    feedback = models.TextField(blank=True, null=True)  # Optional feedback

    def __str__(self):
        return f"Rating by {self.user.username} for prediction {self.prediction.id}: {self.rating}"


class UserProfile(models.Model):
    ROLE_CHOICES = (
        ('owner', 'Owner'),
        ('shelter', 'Shelter'),
        ('general', 'General'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    owner = models.OneToOneField(Owner, on_delete=models.SET_NULL, null=True, blank=True)

    shelter = models.OneToOneField(Shelter, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.user.username} - {self.role}"





