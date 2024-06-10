from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Breed(models.Model):
    SHEDDING_CHOICES = [
        ('low', 'Low'),
        ('moderate', 'Moderate'),
        ('high', 'High'),
        ('none', 'None'),
    ]
    name = models.CharField(max_length=100, unique=True)
    characteristics = models.TextField()
    temperament = models.CharField(max_length=200, blank=True, null=True)
    origin = models.CharField(max_length=200, blank=True, null=True)
    lifespan = models.CharField(max_length=50, blank=True, null=True)
    size = models.CharField(max_length=50, blank=True, null=True)
    coat_length = models.CharField(max_length=50, blank=True, null=True)
    shedding = models.CharField(max_length=20, choices=SHEDDING_CHOICES, default='low')
    exercise_needs = models.CharField(max_length=100, blank=True, null=True)
    trainability = models.CharField(max_length=100, blank=True, null=True)
    health_issues = models.TextField(blank=True, null=True)
    special_needs = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='breed_images/', default='breed_images/default.jpg', null=True, blank=True)  # Specify default image path


    def __str__(self):
        return self.name


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


class Event(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateTimeField()
    location = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Command(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100, default="")
    last_name = models.CharField(max_length=100, default="")
    email = models.EmailField(unique=False, null=True)
    phone_number = models.CharField(max_length=15, default="")
    profile_image = models.ImageField(upload_to='profile_images/', null=True, blank=True)  # Add this line

    is_owner = models.BooleanField(default=False)
    is_shelter = models.BooleanField(default=False)
    is_doctor = models.BooleanField(default=False)
    is_walker = models.BooleanField(default=False)
    is_sitter = models.BooleanField(default=False)
    is_groomer = models.BooleanField(default=False)
    is_trainer = models.BooleanField(default=False)

    owner = models.OneToOneField('Owner', on_delete=models.SET_NULL, null=True, blank=True,
                                 related_name='owner_profile')
    shelter = models.OneToOneField('Shelter', on_delete=models.SET_NULL, null=True, blank=True,
                                   related_name='shelter_profile')
    doctor = models.OneToOneField('Doctor', on_delete=models.SET_NULL, null=True, blank=True,
                                  related_name='doctor_profile')
    walker = models.OneToOneField('Walker', on_delete=models.SET_NULL, null=True, blank=True,
                                  related_name='walker_profile')
    sitter = models.OneToOneField('Sitter', on_delete=models.SET_NULL, null=True, blank=True,
                                  related_name='sitter_profile')
    groomer = models.OneToOneField('Groomer', on_delete=models.SET_NULL, null=True, blank=True,
                                   related_name='groomer_profile')
    trainer = models.OneToOneField('Trainer', on_delete=models.SET_NULL, null=True, blank=True,
                                   related_name='trainer_profile')

    def __str__(self):
        return f"{self.user} - {self.first_name} {self.last_name}"


class Adoption(models.Model):
    # Personal Information
    name = models.CharField(max_length=100)
    birth_date = models.DateField()
    email = models.EmailField()
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=10)
    home_phone = models.CharField(max_length=15, blank=True, null=True)
    work_phone = models.CharField(max_length=15, blank=True, null=True)
    mobile_phone = models.CharField(max_length=15)
    facebook_profile = models.URLField(blank=True, null=True)
    instagram_profile = models.URLField(blank=True, null=True)

    # Family Information
    adults_in_home = models.PositiveIntegerField()
    children_info = models.TextField()  # Example: "2 children, ages 5 and 8"
    allergies = models.BooleanField()

    # Home Information
    home_type = models.CharField(max_length=50,
                                 choices=[('House', 'Μονοκατοικία'), ('Apartment', 'Πολυκατοικία'), ('Other', 'Άλλο')])
    fence_height = models.FloatField()
    escape_possibility = models.BooleanField()

    # Pet Information
    current_pets = models.TextField(blank=True, null=True)
    past_pets = models.TextField(blank=True, null=True)
    abandoned_pet = models.BooleanField()
    adopted_before = models.BooleanField()

    # Desired Pet Information
    adoption_reason = models.CharField(max_length=255)
    family_agreement = models.BooleanField()
    caretaker_info = models.TextField()
    plan_to_neuter = models.BooleanField()
    if_not_neuter_reason = models.TextField(blank=True, null=True)
    pet_location_day_home = models.CharField(max_length=255)
    pet_location_day_away = models.CharField(max_length=255)
    pet_location_night = models.CharField(max_length=255)
    pet_location_long_absence = models.CharField(max_length=255)
    walk_time = models.CharField(max_length=255)
    alone_time = models.PositiveIntegerField()
    moving_plan = models.TextField()
    bad_behavior_response = models.TextField()

    # Desired Pet Characteristics
    preferences = models.TextField(blank=True, null=True)
    pet_character = models.TextField()
    willing_to_host_special_needs = models.TextField()
    additional_info = models.TextField(blank=True, null=True)

    accepted_terms = models.BooleanField()

    def __str__(self):
        return self.name


class Doctor(models.Model):
    userprofile = models.OneToOneField(UserProfile, on_delete=models.CASCADE, related_name='doctor_profile')
    speciality = models.CharField(max_length=100, blank=True, null=True)
    clinic_address = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Dr. {self.userprofile.first_name} {self.userprofile.last_name}"


class Groomer(models.Model):
    userprofile = models.OneToOneField(UserProfile, on_delete=models.CASCADE, related_name='groomer_profile')
    grooming_experience_years = models.IntegerField(blank=True, null=True)

    # Add any other fields relevant to groomers

    def __str__(self):
        return f"{self.userprofile.first_name} {self.userprofile.last_name}"


class Walker(models.Model):
    userprofile = models.OneToOneField(UserProfile, on_delete=models.CASCADE, related_name='walker_profile')
    walking_experience_years = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return f"{self.userprofile.first_name} {self.userprofile.last_name}"


class Sitter(models.Model):
    userprofile = models.OneToOneField(UserProfile, on_delete=models.CASCADE, related_name='sitter_profile')
    experience_years = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return f"{self.userprofile.first_name} {self.userprofile.last_name}"


class Owner(models.Model):
    userprofile = models.OneToOneField(UserProfile, on_delete=models.CASCADE, related_name='owner_profile')
    number_of_dogs = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.userprofile.first_name} {self.userprofile.last_name}"


class Shelter(models.Model):
    userprofile = models.OneToOneField(UserProfile, on_delete=models.CASCADE, related_name='shelter_profile')
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=200)
    capacity = models.IntegerField(blank=True, null=True)
    iban = models.CharField(max_length=34, null=True, blank=True)  # Assuming IBAN is a string of maximum 34 characters

    def __str__(self):
        return self.name


class Dog(models.Model):
    SEX_CHOICES = [("M", "Male"), ("F", "Female")]
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    sex = models.CharField(choices=SEX_CHOICES, max_length=1, blank=True)
    breed = models.CharField(max_length=100)
    description = models.TextField()
    is_not_adopted = models.BooleanField(default=False)
    owner = models.ForeignKey(Owner, on_delete=models.SET_NULL, null=True, blank=True)
    shelter = models.ForeignKey(Shelter, on_delete=models.SET_NULL, null=True, blank=True)
    weight = models.FloatField(null=True, blank=True)
    height = models.FloatField(null=True, blank=True)
    color = models.CharField(max_length=100, null=True, blank=True)
    eye_color = models.CharField(max_length=50, null=True, blank=True)
    last_known_location = models.CharField(max_length=200, null=True, blank=True)
    image = models.ImageField(upload_to='dog_images/', default='breed_images/default.jpg', null=True, blank=True)  # Specify default image path

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


class Grooming(models.Model):
    dog = models.ForeignKey(Dog, on_delete=models.CASCADE)
    groomer = models.ForeignKey(Groomer, on_delete=models.CASCADE)
    date = models.DateTimeField()
    notes = models.TextField()


class Testimonial(models.Model):
    content = models.TextField()
    author = models.CharField(max_length=100)


class Resource(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    content = models.TextField()

    def __str__(self):
        return self.title


class Trainer(models.Model):
    userprofile = models.OneToOneField(UserProfile, on_delete=models.CASCADE, related_name='trainer_profile')
    experience_years = models.IntegerField(blank=True, null=True)
    specialties = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.experience_years
