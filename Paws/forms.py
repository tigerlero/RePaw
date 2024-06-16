from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Dog, Breed, Food, FriendlySpot, Owner, Shelter, Doctor, Event, Microchip, Walk, Training, Health, \
    Appointment, VaccinationRecord, DogBreedPrediction, Grooming, Adoption, UserProfile, Trainer, DoctorBooking, \
    TrainerBooking, WalkerBooking, SitterBooking, GroomerBooking


class DogForm(forms.ModelForm):
    class Meta:
        model = Dog
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'input'}),
            'age': forms.NumberInput(attrs={'class': 'input'}),
            'sex': forms.Select(attrs={'class': 'select'}),
            'breed': forms.TextInput(attrs={'class': 'input'}),
            'description': forms.Textarea(attrs={'class': 'textarea'}),
            'owner': forms.Select(attrs={'class': 'select'}),
            'shelter': forms.Select(attrs={'class': 'select'}),
            'weight': forms.NumberInput(attrs={'class': 'input'}),
            'height': forms.NumberInput(attrs={'class': 'input'}),
            'color': forms.TextInput(attrs={'class': 'input'}),
            'eye_color': forms.TextInput(attrs={'class': 'input'}),
            'last_known_location': forms.TextInput(attrs={'class': 'input'}),
            'image': forms.ClearableFileInput(attrs={'class': 'file-input'}),
        }


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
        fields = ['number_of_dogs']


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
        fields = '__all__'


class GroomingForm(forms.ModelForm):
    class Meta:
        model = Grooming
        fields = '__all__'


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(required=True, max_length=100)
    last_name = forms.CharField(required=True, max_length=100)
    phone_number = forms.CharField(required=True, max_length=15)
    is_shelter = forms.BooleanField(required=False)
    is_owner = forms.BooleanField(required=False)
    is_doctor = forms.BooleanField(required=False)
    is_walker = forms.BooleanField(required=False)
    is_sitter = forms.BooleanField(required=False)
    is_groomer = forms.BooleanField(required=False)
    is_trainer = forms.BooleanField(required=False)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'phone_number', 'password1', 'password2',
                  'is_shelter', 'is_owner', 'is_doctor', 'is_walker', 'is_sitter', 'is_groomer', 'is_trainer']

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        self.fields['username'].required = True  # Make username required

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        if commit:
            user.save()
        return user


class TrainerForm(forms.ModelForm):
    class Meta:
        model = Trainer
        fields = '__all__'


class AdoptionForm(forms.ModelForm):
    class Meta:
        model = Adoption
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'input'}),
            'birth_date': forms.DateInput(attrs={'class': 'input'}),
            'email': forms.EmailInput(attrs={'class': 'input'}),
            'address': forms.TextInput(attrs={'class': 'input'}),
            'city': forms.TextInput(attrs={'class': 'input'}),
            'postal_code': forms.TextInput(attrs={'class': 'input'}),
            'mobile_phone': forms.TextInput(attrs={'class': 'input'}),
            'adults_in_home': forms.NumberInput(attrs={'class': 'input'}),
            'children_info': forms.TextInput(attrs={'class': 'input'}),
            'allergies': forms.CheckboxInput(attrs={'class': 'checkbox'}),
            'home_type': forms.Select(attrs={'class': 'select'}),
            'fence_height': forms.NumberInput(attrs={'class': 'input'}),
            'escape_possibility': forms.CheckboxInput(attrs={'class': 'checkbox'}),
            'current_pets': forms.TextInput(attrs={'class': 'input'}),
            'past_pets': forms.TextInput(attrs={'class': 'input'}),
            'abandoned_pet': forms.CheckboxInput(attrs={'class': 'checkbox'}),
            'adopted_before': forms.CheckboxInput(attrs={'class': 'checkbox'}),
            'adoption_reason': forms.TextInput(attrs={'class': 'input'}),
            'family_agreement': forms.CheckboxInput(attrs={'class': 'checkbox'}),
            'caretaker_info': forms.TextInput(attrs={'class': 'input'}),
            'plan_to_neuter': forms.CheckboxInput(attrs={'class': 'checkbox'}),
            'if_not_neuter_reason': forms.TextInput(attrs={'class': 'input'}),
            'pet_location_day_home': forms.TextInput(attrs={'class': 'input'}),
            'pet_location_day_away': forms.TextInput(attrs={'class': 'input'}),
            'pet_location_night': forms.TextInput(attrs={'class': 'input'}),
            'pet_location_long_absence': forms.TextInput(attrs={'class': 'input'}),
            'walk_time': forms.TextInput(attrs={'class': 'input'}),
            'alone_time': forms.NumberInput(attrs={'class': 'input'}),
            'moving_plan': forms.TextInput(attrs={'class': 'input'}),
            'bad_behavior_response': forms.TextInput(attrs={'class': 'input'}),
            'preferences': forms.TextInput(attrs={'class': 'input'}),
            'pet_character': forms.TextInput(attrs={'class': 'input'}),
            'willing_to_host_special_needs': forms.TextInput(attrs={'class': 'input'}),
            'additional_info': forms.TextInput(attrs={'class': 'input'}),
            'accepted_terms': forms.CheckboxInput(attrs={'class': 'checkbox'}),
        }

    #
    # def __init__(self, *args, **kwargs):
    #     super(AdoptionForm, self).__init__(*args, **kwargs)
    #     for field_name, field in self.fields.items():
    #         field.widget.attrs['class'] = 'form-control'


class DoctorBookingForm(forms.ModelForm):
    class Meta:
        model = DoctorBooking
        fields = ['doctor', 'date', 'reason']


class TrainerBookingForm(forms.ModelForm):
    class Meta:
        model = TrainerBooking
        fields = ['trainer', 'date', 'reason']


class WalkerBookingForm(forms.ModelForm):
    class Meta:
        model = WalkerBooking
        fields = ['walker', 'date', 'reason']


class SitterBookingForm(forms.ModelForm):
    class Meta:
        model = SitterBooking
        fields = ['sitter', 'date', 'reason']


class GroomerBookingForm(forms.ModelForm):
    class Meta:
        model = GroomerBooking
        fields = ['groomer', 'date', 'reason']
