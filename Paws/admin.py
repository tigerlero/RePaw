from django.contrib import admin
from .models import Dog, Walk, Breed, Training, Health, Food, FriendlySpot, Owner, Shelter, Doctor, Appointment, \
    VaccinationRecord, Event, Microchip, DogBreedPrediction, UserProfile, Grooming, Adoption, Groomer, Walker, Sitter, \
    Service, Availability, Booking

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
admin.site.register(UserProfile)
admin.site.register(Grooming)
admin.site.register(Adoption)
admin.site.register(Groomer)
admin.site.register(Sitter)
admin.site.register(Walker)
admin.site.register(Service)
admin.site.register(Availability)
admin.site.register(Booking)

# @admin.register(Service)
# class ServiceAdmin(admin.ModelAdmin):
#     list_display = ('service_type', 'description', 'price_per_hour')
#     list_filter = ('service_type',)
#
# @admin.register(Availability)
# class AvailabilityAdmin(admin.ModelAdmin):
#     list_display = ('service', 'date', 'start_time', 'end_time')
#     list_filter = ('service', 'date')
#
# @admin.register(Booking)
# class BookingAdmin(admin.ModelAdmin):
#     list_display = ('user', 'service', 'date', 'start_time', 'end_time', 'status')
#     list_filter = ('service', 'date', 'status')