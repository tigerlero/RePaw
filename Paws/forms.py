from django import forms
from django.contrib.auth.models import User

from .models import Dog, Breed, Food, FriendlySpot, Owner, Shelter, Doctor, Event, Microchip, Walk, Training, Health, \
    Appointment, VaccinationRecord, DogBreedPrediction, Grooming


class DogForm(forms.ModelForm):
    class Meta:
        model = Dog
        fields = '__all__'


class BreedForm(forms.ModelForm):
    class Meta:
        model = Breed
        fields = '__all__'


class FoodForm(forms.ModelForm):
    class Meta:
        model = Food
        fields = '__all__'


class FriendlySpotForm(forms.ModelForm):
    class Meta:
        model = FriendlySpot
        fields = '__all__'


class OwnerForm(forms.ModelForm):
    class Meta:
        model = Owner
        fields = '__all__'


class ShelterForm(forms.ModelForm):
    class Meta:
        model = Shelter
        fields = '__all__'


class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = '__all__'


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = '__all__'


class MicrochipForm(forms.ModelForm):
    class Meta:
        model = Microchip
        fields = '__all__'


class WalkForm(forms.ModelForm):
    class Meta:
        model = Walk
        fields = '__all__'


class TrainingForm(forms.ModelForm):
    class Meta:
        model = Training
        fields = '__all__'


class HealthForm(forms.ModelForm):
    class Meta:
        model = Health
        fields = '__all__'


class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = '__all__'


class VaccinationRecordForm(forms.ModelForm):
    class Meta:
        model = VaccinationRecord
        fields = '__all__'


class DogBreedPredictionForm(forms.ModelForm):
    class Meta:
        model = DogBreedPrediction
        fields = '__all__'


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']


class GroomingForm(forms.ModelForm):
    class Meta:
        model = Grooming
        fields = '__all__'
