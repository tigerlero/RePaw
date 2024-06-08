from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Dog, Breed, Food, FriendlySpot, Owner, Shelter, Doctor, Event, Microchip, Walk, Training, Health, \
    Appointment, VaccinationRecord, DogBreedPrediction, Grooming, Adoption, UserProfile


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


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=100, required=True)
    last_name = forms.CharField(max_length=100, required=True)
    phone_number = forms.CharField(max_length=15, required=True)
    is_shelter = forms.BooleanField(required=False)
    is_owner = forms.BooleanField(required=False)
    is_doctor = forms.BooleanField(required=False)
    is_walker = forms.BooleanField(required=False)
    is_sitter = forms.BooleanField(required=False)
    is_groomer = forms.BooleanField(required=False)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'phone_number', 'password1', 'password2',
                  'is_shelter', 'is_owner', 'is_doctor', 'is_walker', 'is_sitter', 'is_groomer']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        if commit:
            user.save()
            user_profile = UserProfile.objects.create(
                user=user,
                phone_number=self.cleaned_data['phone_number'],
                is_shelter=self.cleaned_data['is_shelter'],
                is_owner=self.cleaned_data['is_owner'],
                is_doctor=self.cleaned_data['is_doctor'],
                is_walker=self.cleaned_data['is_walker'],
                is_sitter=self.cleaned_data['is_sitter'],
                is_groomer=self.cleaned_data['is_groomer'],
            )
            user_profile.save()
        return user


class AdoptionForm(forms.ModelForm):
    class Meta:
        model = Adoption
        fields = [
            'name', 'birth_date', 'email', 'address', 'city', 'postal_code', 'home_phone',
            'work_phone', 'mobile_phone', 'facebook_profile', 'instagram_profile',
            'adults_in_home', 'children_info', 'allergies', 'home_type', 'fence_height',
            'escape_possibility', 'current_pets', 'past_pets', 'abandoned_pet',
            'adopted_before', 'adoption_reason', 'family_agreement', 'caretaker_info',
            'plan_to_neuter', 'if_not_neuter_reason', 'pet_location_day_home',
            'pet_location_day_away', 'pet_location_night', 'pet_location_long_absence',
            'walk_time', 'alone_time', 'moving_plan', 'bad_behavior_response', 'preferences',
            'pet_character', 'willing_to_host_special_needs', 'additional_info', 'accepted_terms'
        ]
        widgets = {
            'birth_date': forms.DateInput(attrs={'type': 'date'}),
            'email': forms.EmailInput(),
            'home_phone': forms.TextInput(attrs={'type': 'tel'}),
            'work_phone': forms.TextInput(attrs={'type': 'tel'}),
            'mobile_phone': forms.TextInput(attrs={'type': 'tel'}),
            'facebook_profile': forms.URLInput(),
            'instagram_profile': forms.URLInput(),
            'adults_in_home': forms.NumberInput(),
            'fence_height': forms.NumberInput(),
            'current_pets': forms.Textarea(attrs={'rows': 3}),
            'past_pets': forms.Textarea(attrs={'rows': 3}),
            'adoption_reason': forms.Textarea(attrs={'rows': 3}),
            'caretaker_info': forms.Textarea(attrs={'rows': 3}),
            'if_not_neuter_reason': forms.Textarea(attrs={'rows': 3}),
            'pet_location_day_home': forms.Textarea(attrs={'rows': 3}),
            'pet_location_day_away': forms.Textarea(attrs={'rows': 3}),
            'pet_location_night': forms.Textarea(attrs={'rows': 3}),
            'pet_location_long_absence': forms.Textarea(attrs={'rows': 3}),
            'walk_time': forms.Textarea(attrs={'rows': 3}),
            'alone_time': forms.NumberInput(),
            'moving_plan': forms.Textarea(attrs={'rows': 3}),
            'bad_behavior_response': forms.Textarea(attrs={'rows': 3}),
            'preferences': forms.Textarea(attrs={'rows': 3}),
            'pet_character': forms.Textarea(attrs={'rows': 3}),
            'willing_to_host_special_needs': forms.Textarea(attrs={'rows': 3}),
            'additional_info': forms.Textarea(attrs={'rows': 3}),
            'accepted_terms': forms.CheckboxInput(),
        }
