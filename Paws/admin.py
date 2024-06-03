from django.contrib import admin
from .models import Dog, Walk, Breed, Training, Health, Food, FriendlySpot, Owner, Shelter, Doctor, Appointment, \
    VaccinationRecord, Event, Microchip, DogBreedPrediction, UserProfile, PredictionRating

admin.site.register(Dog)
admin.site.register(Walk)
admin.site.register(Breed)
admin.site.register(Training)
admin.site.register(Health)
admin.site.register(Food)
admin.site.register(FriendlySpot)
admin.site.register(Owner)
admin.site.register(Shelter)
admin.site.register(Doctor)
admin.site.register(Appointment)
admin.site.register(VaccinationRecord)
admin.site.register(Event)
admin.site.register(Microchip)
admin.site.register(DogBreedPrediction)
admin.site.register(PredictionRating)
admin.site.register(UserProfile)