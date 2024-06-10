from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Dog, Walk, Breed, Training, Health, Food, FriendlySpot, Microchip, DogBreedPrediction, UserProfile, \
    Adoption, Groomer, Grooming, Trainer, Sitter, Walker
from .models import Owner, Shelter, Doctor, Appointment, VaccinationRecord, Event


class DogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dog
        fields = '__all__'


class WalkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Walk
        fields = '__all__'


class BreedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Breed
        fields = '__all__'


class TrainingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Training
        fields = '__all__'


class HealthSerializer(serializers.ModelSerializer):
    class Meta:
        model = Health
        fields = '__all__'


class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = '__all__'


class FriendlySpotSerializer(serializers.ModelSerializer):
    class Meta:
        model = FriendlySpot
        fields = '__all__'


class OwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Owner
        fields = '__all__'


class ShelterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shelter
        fields = '__all__'


class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = '__all__'


class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = '__all__'


class VaccinationRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = VaccinationRecord
        fields = '__all__'


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'


class MicrochipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Microchip
        fields = '__all__'


class DogBreedPredictionSerializer(serializers.ModelSerializer):
    class Meta:
        model = DogBreedPrediction
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name']


class UserProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = UserProfile
        fields = '__all__'


class AdoptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Adoption
        fields = '__all__'


class GroomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Groomer
        fields = '__all__'


class GroomingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grooming
        fields = '__all__'


class TrainerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trainer
        fields = '__all__'


class WalkerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Walker
        fields = '__all__'


class SitterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sitter
        fields = '__all__'