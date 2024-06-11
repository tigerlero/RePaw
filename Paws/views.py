from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
# Create your views here.
from rest_framework import viewsets, status, generics
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .forms import DogForm, BreedForm, FoodForm, FriendlySpotForm, OwnerForm, ShelterForm, DoctorForm, EventForm, \
    MicrochipForm, WalkForm, TrainingForm, HealthForm, AppointmentForm, VaccinationRecordForm, DogBreedPredictionForm, \
    UserProfileForm, GroomingForm, AdoptionForm, RegisterForm, TrainerForm
from .models import Dog, Walk, Breed, Training, Health, Food, FriendlySpot, Microchip, DogBreedPrediction, UserProfile, \
    Adoption, Grooming, Groomer, Walker, Sitter, Testimonial, Resource, Trainer
from .serializers import DogSerializer, WalkSerializer, BreedSerializer, TrainingSerializer, HealthSerializer, \
    FoodSerializer, FriendlySpotSerializer, MicrochipSerializer, DogBreedPredictionSerializer, UserProfileSerializer, \
    AdoptionSerializer, GroomingSerializer, GroomerSerializer, TrainerSerializer

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


class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer


class TrainerListCreateAPIView(generics.ListCreateAPIView):
    queryset = Trainer.objects.all()
    serializer_class = TrainerSerializer

class TrainerRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Trainer.objects.all()
    serializer_class = TrainerSerializer


@api_view(['GET', 'POST'])
def adoption_list(request):
    if request.method == 'GET':
        adoptions = Adoption.objects.all()
        serializer = AdoptionSerializer(adoptions, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = AdoptionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def groomer_list(request):
    if request.method == 'GET':
        groomers = Groomer.objects.all()
        serializer = GroomerSerializer(groomers, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = GroomerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def grooming_list(request):
    if request.method == 'GET':
        groomings = Grooming.objects.all()
        serializer = GroomingSerializer(groomings, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = GroomingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#  Web views

def dog_detail(request, dog_id):
    dog = get_object_or_404(Dog, pk=dog_id)
    return render(request, 'dog_detail.html', {'dog': dog})


def dogs_list(request):
    dogs_for_adoption = Dog.objects.filter(is_not_adopted=True)
    adopted_dogs = Dog.objects.filter(is_not_adopted=False)
    dogs_needing_walks_or_sitters = Dog.objects.filter(walk__sitter_required=True).distinct()
    sick_dogs = Dog.objects.filter(health__is_sick=True)
    modeling_dogs = Dog.objects.filter(health__is_sick=False)
    most_trained_dogs = Dog.objects.filter(health__is_sick=False)
    trainers_dogs = Dog.objects.filter(health__is_sick=False)

    context = {
        'dogs_for_adoption': dogs_for_adoption,
        'adopted_dogs': adopted_dogs,
        'dogs_needing_walks_or_sitters': dogs_needing_walks_or_sitters,
        'sick_dogs': sick_dogs,
        'modeling_dogs': modeling_dogs,
        'most_trained_dogs': most_trained_dogs,
        'trainers_dogs': trainers_dogs,
    }
    return render(request, 'dogs_list.html', context)


def create_dog(request):
    if request.method == 'POST':
        form = DogForm(request.POST, request.FILES,)
        if form.is_valid():
            form.save()
            return redirect(reverse('dogs_list'))
    else:
        form = DogForm()
    return render(request, 'create_dog.html', {'form': form})


def update_dog(request, dog_id):
    dog = get_object_or_404(Dog, pk=dog_id)
    if request.method == 'POST':
        form = DogForm(request.POST, request.FILES, instance=dog)
        if form.is_valid():
            form.save()
            return redirect(reverse('dog_detail', args=[dog.id]))
    else:
        form = DogForm(instance=dog)
    return render(request, 'update_dog.html', {'form': form})


def delete_dog(request, dog_id):
    dog = get_object_or_404(Dog, pk=dog_id)
    if request.method == 'POST':
        dog.delete()
        return redirect(reverse('dogs_list'))
    return render(request, 'delete_dog.html', {'dog': dog})


def breeds_list(request):
    breeds = Breed.objects.all()
    # create_breeds()
    return render(request, 'breeds_list.html', {'breeds': breeds})


def breed_detail(request, breed_name):
    breed = get_object_or_404(Breed, name=breed_name)
    return render(request, 'breed_detail.html', {'breed': breed})


def delete_breed(request, breed_name):
    breed = get_object_or_404(Breed, name=breed_name)
    if request.method == 'POST':
        breed.delete()
        return redirect(reverse('breeds_list'))
    return render(request, 'delete_breed.html', {'breed': breed})


def update_breed(request, breed_name):
    breed = get_object_or_404(Breed, name=breed_name)
    if request.method == 'POST':
        form = BreedForm(request.POST, request.FILES, instance=breed)  # Add request.FILES to handle file uploads
        if form.is_valid():
            form.save()
            return redirect(reverse('breed_detail', args=[breed.name]))
    else:
        form = BreedForm(instance=breed)
    return render(request, 'update_breed.html', {'form': form, 'breed': breed})


def food_list(request):
    foods = Food.objects.all()
    return render(request, 'food_list.html', {'foods': foods})


def food_detail(request, food_id):
    food = get_object_or_404(Food, pk=food_id)
    return render(request, 'food_detail.html', {'food': food})


def food_delete(request, food_id):
    food = get_object_or_404(Food, pk=food_id)
    if request.method == 'POST':
        food.delete()
        return redirect(reverse('food_list'))
    return render(request, 'food_delete.html', {'food': food})


def food_update(request, food_id):
    food = get_object_or_404(Food, pk=food_id)
    if request.method == 'POST':
        form = FoodForm(request.POST, instance=food)
        if form.is_valid():
            form.save()
            return redirect('food_detail', food_id=food.id)
    else:
        form = FoodForm(instance=food)
    return render(request, 'food_update.html', {'form': form, 'food': food})


def friendlyspot_list(request):
    spots = FriendlySpot.objects.all()
    return render(request, 'friendlyspot_list.html', {'spots': spots})


def friendlyspot_detail(request, spot_id):
    spot = get_object_or_404(FriendlySpot, pk=spot_id)
    return render(request, 'friendlyspot_detail.html', {'spot': spot})


def friendlyspot_update(request, spot_id):
    spot = get_object_or_404(FriendlySpot, pk=spot_id)
    if request.method == 'POST':
        form = FriendlySpotForm(request.POST, instance=spot)
        if form.is_valid():
            form.save()
            return redirect('friendlyspot_detail', spot_id=spot.id)
    else:
        form = FriendlySpotForm(instance=spot)
    return render(request, 'friendlyspot_update.html', {'form': form, 'spot': spot})


def friendlyspot_delete(request, spot_id):
    spot = get_object_or_404(FriendlySpot, pk=spot_id)
    if request.method == 'POST':
        spot.delete()
        return redirect('friendlyspot_list')
    return render(request, 'friendlyspot_delete.html', {'spot': spot})


def owner_list(request):
    owners = UserProfile.objects.filter(is_owner=True).prefetch_related('owner_profile')
    return render(request, 'owner_list.html', {'owners': owners})


def owner_detail(request, owner_id):
    owner = get_object_or_404(Owner, pk=owner_id)
    return render(request, 'owner_detail.html', {'owner': owner})


def owner_update(request, owner_id):
    owner = get_object_or_404(Owner, pk=owner_id)
    if request.method == 'POST':
        form = OwnerForm(request.POST, instance=owner)
        if form.is_valid():
            form.save()
            return redirect('owner_detail', owner_id=owner.id)
    else:
        form = OwnerForm(instance=owner)
    return render(request, 'owner_update.html', {'form': form, 'owner': owner})


def owner_delete(request, owner_id):
    owner = get_object_or_404(Owner, pk=owner_id)
    if request.method == 'POST':
        owner.delete()
        return redirect('owner_list')
    return render(request, 'owner_delete.html', {'owner': owner})


def shelter_list(request):
    shelters = UserProfile.objects.filter(is_shelter=True).prefetch_related('shelter_profile')
    return render(request, 'shelter_list.html', {'shelters': shelters})


def shelter_detail(request, shelter_id):
    shelter = get_object_or_404(Shelter, pk=shelter_id)
    return render(request, 'shelter_detail.html', {'shelter': shelter})


def shelter_update(request, shelter_id):
    shelter = get_object_or_404(Shelter, pk=shelter_id)
    if request.method == 'POST':
        form = ShelterForm(request.POST, instance=shelter)
        if form.is_valid():
            form.save()
            return redirect('shelter_detail', shelter_id=shelter.id)
    else:
        form = ShelterForm(instance=shelter)
    return render(request, 'shelter_update.html', {'form': form, 'shelter': shelter})


def shelter_delete(request, shelter_id):
    shelter = get_object_or_404(Shelter, pk=shelter_id)
    if request.method == 'POST':
        shelter.delete()
        return redirect('shelter_list')
    return render(request, 'shelter_delete.html', {'shelter': shelter})


def doctor_list(request):
    doctors = UserProfile.objects.filter(is_doctor=True)
    return render(request, 'doctor_list.html', {'doctors': doctors})


def doctor_detail(request, doctor_id):
    doctor = get_object_or_404(Doctor, pk=doctor_id)
    return render(request, 'doctor_detail.html', {'doctor': doctor})


def doctor_update(request, doctor_id):
    doctor = get_object_or_404(Doctor, pk=doctor_id)
    if request.method == 'POST':
        form = DoctorForm(request.POST, instance=doctor)
        if form.is_valid():
            form.save()
            return redirect('doctor_detail', doctor_id=doctor.id)
    else:
        form = DoctorForm(instance=doctor)
    return render(request, 'doctor_update.html', {'form': form, 'doctor': doctor})


def doctor_delete(request, doctor_id):
    doctor = get_object_or_404(Doctor, pk=doctor_id)
    if request.method == 'POST':
        doctor.delete()
        return redirect('doctor_list')
    return render(request, 'doctor_delete.html', {'doctor': doctor})


def event_list(request):
    events = Event.objects.all()
    return render(request, 'event_list.html', {'events': events})


def event_detail(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    return render(request, 'event_detail.html', {'event': event})


def event_update(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    if request.method == 'POST':
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            form.save()
            return redirect('event_detail', event_id=event.id)
    else:
        form = EventForm(instance=event)
    return render(request, 'event_update.html', {'form': form, 'event': event})


def event_delete(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    if request.method == 'POST':
        event.delete()
        return redirect('event_list')
    return render(request, 'event_delete.html', {'event': event})


def microchip_list(request):
    microchips = Microchip.objects.all()
    return render(request, 'microchip_list.html', {'microchips': microchips})


def microchip_detail(request, microchip_id):
    microchip = get_object_or_404(Microchip, pk=microchip_id)
    return render(request, 'microchip_detail.html', {'microchip': microchip})


def microchip_update(request, microchip_id):
    microchip = get_object_or_404(Microchip, pk=microchip_id)
    if request.method == 'POST':
        form = MicrochipForm(request.POST, instance=microchip)
        if form.is_valid():
            form.save()
            return redirect('microchip_detail', microchip_id=microchip.id)
    else:
        form = MicrochipForm(instance=microchip)
    return render(request, 'microchip_update.html', {'form': form, 'microchip': microchip})


def microchip_delete(request, microchip_id):
    microchip = get_object_or_404(Microchip, pk=microchip_id)
    if request.method == 'POST':
        microchip.delete()
        return redirect('microchip_list')
    return render(request, 'microchip_delete.html', {'microchip': microchip})


def walks_list(request):
    walks = Walk.objects.all()
    return render(request, 'walk_list.html', {'walks': walks})


def walk_detail(request, walk_id):
    walk = get_object_or_404(Walk, pk=walk_id)
    return render(request, 'walk_detail.html', {'walk': walk})


def walk_update(request, walk_id):
    walk = get_object_or_404(Walk, pk=walk_id)
    if request.method == 'POST':
        form = WalkForm(request.POST, instance=walk)
        if form.is_valid():
            form.save()
            return redirect('walk_detail', walk_id=walk.id)
    else:
        form = WalkForm(instance=walk)
    return render(request, 'walk_update.html', {'form': form, 'walk': walk})


def walk_delete(request, walk_id):
    walk = get_object_or_404(Walk, pk=walk_id)
    if request.method == 'POST':
        walk.delete()
        return redirect('walk_list')
    return render(request, 'walk_delete.html', {'walk': walk})


def training_list(request):
    trainings = Training.objects.all()
    return render(request, 'training_list.html', {'trainings': trainings})


def training_detail(request, training_id):
    training = get_object_or_404(Training, pk=training_id)
    return render(request, 'training_detail.html', {'training': training})


def training_update(request, training_id):
    training = get_object_or_404(Training, pk=training_id)
    if request.method == 'POST':
        form = TrainingForm(request.POST, instance=training)
        if form.is_valid():
            form.save()
            return redirect('training_detail', training_id=training.id)
    else:
        form = TrainingForm(instance=training)
    return render(request, 'training_update.html', {'form': form, 'training': training})


def training_delete(request, training_id):
    training = get_object_or_404(Training, pk=training_id)
    if request.method == 'POST':
        training.delete()
        return redirect('training_list')
    return render(request, 'training_delete.html', {'training': training})


def health_list(request):
    health_records = Health.objects.all()
    return render(request, 'health_list.html', {'health_records': health_records})


def health_detail(request, health_id):
    health_record = get_object_or_404(Health, pk=health_id)
    return render(request, 'health_detail.html', {'health_record': health_record})


def health_update(request, health_id):
    health_record = get_object_or_404(Health, pk=health_id)
    if request.method == 'POST':
        form = HealthForm(request.POST, instance=health_record)
        if form.is_valid():
            form.save()
            return redirect('health_detail', health_id=health_record.id)
    else:
        form = HealthForm(instance=health_record)
    return render(request, 'health_update.html', {'form': form, 'health_record': health_record})


def health_delete(request, health_id):
    health_record = get_object_or_404(Health, pk=health_id)
    if request.method == 'POST':
        health_record.delete()
        return redirect('health_list')
    return render(request, 'health_delete.html', {'health_record': health_record})


def appointment_list(request):
    appointments = Appointment.objects.all()
    return render(request, 'appointment_list.html', {'appointments': appointments})


def appointment_detail(request, appointment_id):
    appointment = get_object_or_404(Appointment, pk=appointment_id)
    return render(request, 'appointment_detail.html', {'appointment': appointment})


def appointment_update(request, appointment_id):
    appointment = get_object_or_404(Appointment, pk=appointment_id)
    if request.method == 'POST':
        form = AppointmentForm(request.POST, instance=appointment)
        if form.is_valid():
            form.save()
            return redirect('appointment_detail', appointment_id=appointment.id)
    else:
        form = AppointmentForm(instance=appointment)
    return render(request, 'appointment_update.html', {'form': form, 'appointment': appointment})


def appointment_delete(request, appointment_id):
    appointment = get_object_or_404(Appointment, pk=appointment_id)
    if request.method == 'POST':
        appointment.delete()
        return redirect('appointment_list')
    return render(request, 'appointment_delete.html', {'appointment': appointment})


def vaccination_record_list(request):
    vaccination_records = VaccinationRecord.objects.all()
    return render(request, 'vaccination_record_list.html', {'vaccination_records': vaccination_records})


def vaccination_record_detail(request, vaccination_record_id):
    vaccination_record = get_object_or_404(VaccinationRecord, pk=vaccination_record_id)
    return render(request, 'vaccination_record_detail.html', {'vaccination_record': vaccination_record})


def vaccination_record_update(request, vaccination_record_id):
    vaccination_record = get_object_or_404(VaccinationRecord, pk=vaccination_record_id)
    if request.method == 'POST':
        form = VaccinationRecordForm(request.POST, instance=vaccination_record)
        if form.is_valid():
            form.save()
            return redirect('vaccination_record_detail', vaccination_record_id=vaccination_record.id)
    else:
        form = VaccinationRecordForm(instance=vaccination_record)
    return render(request, 'vaccination_record_update.html', {'form': form, 'vaccination_record': vaccination_record})


def vaccination_record_delete(request, vaccination_record_id):
    vaccination_record = get_object_or_404(VaccinationRecord, pk=vaccination_record_id)
    if request.method == 'POST':
        vaccination_record.delete()
        return redirect('vaccination_record_list')
    return render(request, 'vaccination_record_delete.html', {'vaccination_record': vaccination_record})


def dog_breed_prediction_list(request):
    predictions = DogBreedPrediction.objects.all()
    return render(request, 'dog_breed_prediction_list.html', {'predictions': predictions})


def dog_breed_prediction_detail(request, prediction_id):
    prediction = get_object_or_404(DogBreedPrediction, pk=prediction_id)
    return render(request, 'dog_breed_prediction_detail.html', {'prediction': prediction})


def dog_breed_prediction_update(request, prediction_id):
    prediction = get_object_or_404(DogBreedPrediction, pk=prediction_id)
    if request.method == 'POST':
        form = DogBreedPredictionForm(request.POST, request.FILES, instance=prediction)
        if form.is_valid():
            form.save()
            return redirect('dog_breed_prediction_detail', prediction_id=prediction.id)
    else:
        form = DogBreedPredictionForm(instance=prediction)
    return render(request, 'dog_breed_prediction_update.html', {'form': form, 'prediction': prediction})


def dog_breed_prediction_delete(request, prediction_id):
    prediction = get_object_or_404(DogBreedPrediction, pk=prediction_id)
    if request.method == 'POST':
        prediction.delete()
        return redirect('dog_breed_prediction_list')
    return render(request, 'dog_breed_prediction_delete.html', {'prediction': prediction})


@login_required
def user_profile(request):
    user = request.user
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = UserProfileForm(instance=user)
    return render(request, 'user_profile.html', {'form': form})


@login_required
def user_profile_list(request):
    profiles = User.objects.all()
    return render(request, 'user_profile_list.html', {'profiles': profiles})


@login_required
def user_profile_update(request, profile_id):
    profile = get_object_or_404(User, pk=profile_id)
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('user_profile_list')
    else:
        form = UserProfileForm(instance=profile)
    return render(request, 'user_profile_update.html', {'form': form, 'profile': profile})


@login_required
def user_profile_delete(request, profile_id):
    profile = get_object_or_404(User, pk=profile_id)
    if request.method == 'POST':
        profile.delete()
        return redirect('user_profile_list')
    return render(request, 'user_profile_delete.html', {'profile': profile})


def create_walk(request):
    if request.method == 'POST':
        form = WalkForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('walk_list')
    else:
        form = WalkForm()
    return render(request, 'create_walk.html', {'form': form})


def create_breed(request):
    if request.method == 'POST':
        form = BreedForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('breeds_list')
    else:
        form = BreedForm()
    return render(request, 'create_breed.html', {'form': form})


def create_grooming(request):
    if request.method == 'POST':
        form = GroomingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dogs_list')
    else:
        form = GroomingForm()
    return render(request, 'create_grooming.html', {'form': form})


def create_training(request):
    if request.method == 'POST':
        form = TrainingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dogs_list')
    else:
        form = TrainingForm()
    return render(request, 'create_training.html', {'form': form})


def adoption_form(request):
    if request.method == 'POST':
        form = AdoptionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('adoptionSuccess')
    else:
        form = AdoptionForm()
    return render(request, 'adoption_form.html', {'form': form})


def adoptionSuccess(request):
    return render(request, 'adoptionSuccess.html')


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST, request.FILES,)
        if form.is_valid():
            user = form.save()

            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            userprofile = UserProfile.objects.create(
                user=user,
                first_name=form.cleaned_data.get('first_name'),
                last_name=form.cleaned_data.get('last_name'),
                city=form.cleaned_data.get('city'),
                email=form.cleaned_data.get('email'),
                is_shelter=form.cleaned_data.get('is_shelter'),
                is_owner=form.cleaned_data.get('is_owner'),
                is_doctor=form.cleaned_data.get('is_doctor'),
                is_walker=form.cleaned_data.get('is_walker'),
                is_sitter=form.cleaned_data.get('is_sitter'),
                is_groomer=form.cleaned_data.get('is_groomer'),
                is_trainer=form.cleaned_data.get('is_trainer'),
            )
            userprofile.save()
            if userprofile.is_doctor:
                Doctor.objects.create(userprofile=userprofile)
            if userprofile.is_owner:
                Owner.objects.create(userprofile=userprofile)
            if userprofile.is_shelter:
                Shelter.objects.create(userprofile=userprofile)
            if userprofile.is_walker:
                Walker.objects.create(userprofile=userprofile)
            if userprofile.is_sitter:
                Sitter.objects.create(userprofile=userprofile)
            if userprofile.is_groomer:
                Groomer.objects.create(userprofile=userprofile)
            if userprofile.is_trainer:
                Trainer.objects.create(userprofile=userprofile)
            return redirect('/')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')  # Change 'home' to the name of your home page
        else:
            error_message = "Username and password don't match. Please try again."
            return render(request, 'login.html', {'form': form, 'error_message': error_message})
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


def custom_logout(request):
    logout(request)
    return redirect(reverse('home'))


def walkers_list(request):
    walkers = UserProfile.objects.filter(is_walker=True).prefetch_related('walker_profile')
    return render(request, 'walkers_list.html', {'walkers': walkers})


def groomers_list(request):
    groomers = UserProfile.objects.filter(is_groomer=True).prefetch_related('groomer_profile')
    return render(request, 'groomers_list.html', {'groomers': groomers})


def sitters_list(request):
    sitters = UserProfile.objects.filter(is_sitter=True).prefetch_related('sitter_profile')
    return render(request, 'sitters_list.html', {'sitters': sitters})


def home(request):
    dogs = Dog.objects.all()
    events = Event.objects.all()
    testimonials = Testimonial.objects.all()

    context = {
        'dogs': dogs,
        'events': events,
        'testimonials': testimonials,
    }

    return render(request, 'homepage.html', context)


def resource_detail(request, slug):
    resource = get_object_or_404(Resource, slug=slug)
    return render(request, 'resource_detail.html', {'resource': resource})


def trainers_list(request):
    trainers = UserProfile.objects.filter(is_trainer=True).prefetch_related('trainer_profile')
    return render(request, 'trainers_list.html', {'trainers': trainers})


def trainer_detail(request, trainer_id):
    trainer = get_object_or_404(Trainer, id=trainer_id)
    return render(request, 'trainer_detail.html', {'trainer': trainer})


def create_trainer(request):
    if request.method == 'POST':
        form = TrainerForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('trainers_list')
    else:
        form = TrainerForm()
    return render(request, 'create_trainer.html', {'form': form})


def update_trainer(request, trainer_id):
    trainer = get_object_or_404(Trainer, id=trainer_id)
    if request.method == 'POST':
        form = TrainerForm(request.POST, request.FILES, instance=trainer)
        if form.is_valid():
            form.save()
            return redirect('trainer_detail', trainer_id=trainer.id)
    else:
        form = TrainerForm(instance=trainer)
    return render(request, 'update_trainer.html', {'form': form, 'trainer': trainer})


def delete_trainer(request, trainer_id):
    trainer = get_object_or_404(Trainer, id=trainer_id)
    if request.method == 'POST':
        trainer.delete()
        return redirect('trainers_list')
    return render(request, 'delete_trainer.html', {'trainer': trainer})


def create_breeds():
    # Create instances of the Breed model
    breeds_data = [
        {
            'name': 'Labrador Retriever',
            'characteristics': 'Friendly, Outgoing, Even Tempered',
            'temperament': 'Friendly, Intelligent, Outgoing',
            'origin': 'Canada',
            'lifespan': '10-12 years',
            'size': 'Large',
            'coat_length': 'Short',
            'shedding': 'High',
            'exercise_needs': 'High',
            'trainability': 'High',
            'health_issues': 'Common health issues include hip dysplasia, elbow dysplasia, and obesity.',
            'special_needs': 'Regular exercise and mental stimulation are essential.'
        },
        {
            'name': 'German Shepherd',
            'characteristics': 'Smart, Confident, Courageous',
            'temperament': 'Confident, Courageous, Smart',
            'origin': 'Germany',
            'lifespan': '9-13 years',
            'size': 'Large',
            'coat_length': 'Medium',
            'shedding': 'Moderate',
            'exercise_needs': 'High',
            'trainability': 'High',
            'health_issues': 'Common health issues include hip dysplasia, elbow dysplasia, and degenerative myelopathy.',
            'special_needs': 'Regular exercise and early socialization and training are important.'
        },
        {
            'name': 'Golden Retriever',
            'characteristics': 'Intelligent, Friendly, Devoted',
            'temperament': 'Intelligent, Friendly, Devoted',
            'origin': 'Scotland',
            'lifespan': '10-12 years',
            'size': 'Large',
            'coat_length': 'Medium',
            'shedding': 'Moderate',
            'exercise_needs': 'High',
            'trainability': 'High',
            'health_issues': 'Common health issues include hip dysplasia, elbow dysplasia, and obesity.',
            'special_needs': 'Regular exercise, mental stimulation, and proper diet are important.'
        },
        {
            'name': 'Bulldog',
            'characteristics': 'Docile, Willful, Friendly',
            'temperament': 'Docile, Willful, Friendly',
            'origin': 'England',
            'lifespan': '8-10 years',
            'size': 'Medium',
            'coat_length': 'Short',
            'shedding': 'Low',
            'exercise_needs': 'Low',
            'trainability': 'Low',
            'health_issues': 'Common health issues include hip dysplasia, brachycephalic syndrome, and skin problems.',
            'special_needs': 'Avoid excessive heat and vigorous exercise due to their brachycephalic anatomy.'
        },
        {
            'name': 'Beagle',
            'characteristics': 'Friendly, Curious, Merry',
            'temperament': 'Friendly, Curious, Merry',
            'origin': 'England',
            'lifespan': '12-15 years',
            'size': 'Small to Medium',
            'coat_length': 'Short',
            'shedding': 'Moderate',
            'exercise_needs': 'Moderate',
            'trainability': 'Moderate',
            'health_issues': 'Common health issues include epilepsy, hypothyroidism, and hip dysplasia.',
            'special_needs': 'Regular exercise and a balanced diet are important.'
        },
        {
            'name': 'Poodle',
            'characteristics': 'Intelligent, Active, Alert',
            'temperament': 'Intelligent, Active, Alert',
            'origin': 'Germany',
            'lifespan': '10-18 years',
            'size': 'Toy, Miniature, Standard',
            'coat_length': 'Curly',
            'shedding': 'Low',
            'exercise_needs': 'Moderate to High',
            'trainability': 'High',
            'health_issues': 'Common health issues include hip dysplasia, progressive retinal atrophy, and bloat.',
            'special_needs': 'Regular grooming and exercise are essential.'
        },
        {
            'name': 'French Bulldog',
            'characteristics': 'Adaptable, Playful, Smart',
            'temperament': 'Adaptable, Playful, Smart',
            'origin': 'France',
            'lifespan': '10-12 years',
            'size': 'Small',
            'coat_length': 'Short',
            'shedding': 'Low',
            'exercise_needs': 'Low',
            'trainability': 'Low',
            'health_issues': 'Common health issues include brachycephalic syndrome, hip dysplasia, and allergies.',
            'special_needs': 'Avoid excessive heat and rigorous exercise due to their brachycephalic anatomy.'
        },
        {
            'name': 'Rottweiler',
            'characteristics': 'Confident, Courageous, Calm',
            'temperament': 'Confident, Courageous, Calm',
            'origin': 'Germany',
            'lifespan': '8-10 years',
            'size': 'Large',
            'coat_length': 'Short',
            'shedding': 'Moderate',
            'exercise_needs': 'High',
            'trainability': 'High',
            'health_issues': 'Common health issues include hip dysplasia, osteosarcoma, and bloat.',
            'special_needs': 'Early socialization and training are important for a well-behaved Rottweiler.'
        },
        {
            'name': 'Yorkshire Terrier',
            'characteristics': 'Affectionate, Spirited, Intelligent',
            'temperament': 'Affectionate, Spirited, Intelligent',
            'origin': 'England',
            'lifespan': '13-16 years',
            'size': 'Toy',
            'coat_length': 'Long',
            'shedding': 'Low',
            'exercise_needs': 'Low',
            'trainability': 'Moderate',
            'health_issues': 'Common health issues include patellar luxation, tracheal collapse, and dental problems.',
            'special_needs': 'Regular grooming and dental care are essential for Yorkshire Terriers.'
        },
    ]

    # Loop through the data and create Breed objects
    for breed_data in breeds_data:
        Breed.objects.create(**breed_data)
