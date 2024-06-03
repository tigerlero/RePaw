from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

# Create your views here.
from rest_framework import viewsets

from .forms import DogForm
from .models import Dog, Walk, Breed, Training, Health, Food, FriendlySpot, Microchip, DogBreedPrediction, UserProfile, \
    PredictionRating
from .serializers import DogSerializer, WalkSerializer, BreedSerializer, TrainingSerializer, HealthSerializer, \
    FoodSerializer, FriendlySpotSerializer, MicrochipSerializer, DogBreedPredictionSerializer, UserProfileSerializer, \
    PredictionRatingSerializer

from .models import Owner, Shelter, Doctor, Appointment, VaccinationRecord, Event
from .serializers import OwnerSerializer, ShelterSerializer, DoctorSerializer, AppointmentSerializer, \
    VaccinationRecordSerializer, EventSerializer


class OwnerViewSet(viewsets.ModelViewSet):
    queryset = Owner.objects.all()
    serializer_class = OwnerSerializer


class ShelterViewSet(viewsets.ModelViewSet):
    queryset = Shelter.objects.all()
    serializer_class = ShelterSerializer


class DoctorViewSet(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer


class DogViewSet(viewsets.ModelViewSet):
    queryset = Dog.objects.all()
    serializer_class = DogSerializer


class WalkViewSet(viewsets.ModelViewSet):
    queryset = Walk.objects.all()
    serializer_class = WalkSerializer


class BreedViewSet(viewsets.ModelViewSet):
    queryset = Breed.objects.all()
    serializer_class = BreedSerializer


class TrainingViewSet(viewsets.ModelViewSet):
    queryset = Training.objects.all()
    serializer_class = TrainingSerializer


class HealthViewSet(viewsets.ModelViewSet):
    queryset = Health.objects.all()
    serializer_class = HealthSerializer


class FoodViewSet(viewsets.ModelViewSet):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer


class FriendlySpotViewSet(viewsets.ModelViewSet):
    queryset = FriendlySpot.objects.all()
    serializer_class = FriendlySpotSerializer


class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer


class VaccinationRecordViewSet(viewsets.ModelViewSet):
    queryset = VaccinationRecord.objects.all()
    serializer_class = VaccinationRecordSerializer


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer


class MicrochipViewSet(viewsets.ModelViewSet):
    queryset = Microchip.objects.all()
    serializer_class = MicrochipSerializer


class DogBreedPredictionViewSet(viewsets.ModelViewSet):
    queryset = DogBreedPrediction.objects.all()
    serializer_class = DogBreedPredictionSerializer


class PredictionRatingViewSet(viewsets.ModelViewSet):
    queryset = PredictionRating.objects.all()
    serializer_class = PredictionRatingSerializer


class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer


def dog_detail(request, dog_id):
    dog = get_object_or_404(Dog, pk=dog_id)
    return render(request, 'dog_detail.html', {'dog': dog})


def dogs_list(request):
    dogs = Dog.objects.all()
    return render(request, 'dogs_list.html', {'dogs': dogs})


def create_dog(request):
    if request.method == 'POST':
        form = DogForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('dogs_list'))
    else:
        form = DogForm()
    return render(request, 'create_dog.html', {'form': form})


def update_dog(request, dog_id):
    dog = get_object_or_404(Dog, pk=dog_id)
    if request.method == 'POST':
        form = DogForm(request.POST, instance=dog)
        if form.is_valid():
            form.save()
            return redirect(reverse('dog_detail', args=[dog.id]))
    else:
        form = DogForm(instance=dog)
    return render(request, 'update_dog.html', {'form': form})
