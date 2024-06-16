from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from rest_framework.routers import DefaultRouter


from .views import DogViewSet, WalkViewSet, BreedViewSet, TrainingViewSet, HealthViewSet, FoodViewSet, \
    FriendlySpotViewSet, MicrochipViewSet, DogBreedPredictionViewSet, UserProfileViewSet, \
    dogs_list, dog_detail, create_dog, update_dog, delete_dog, breeds_list, breed_detail, delete_breed, update_breed, \
    food_list, food_detail, food_delete, food_update, friendlyspot_list, friendlyspot_detail, friendlyspot_update, \
    friendlyspot_delete, owner_list, owner_detail, owner_update, owner_delete, shelter_list, shelter_detail, \
    shelter_update, shelter_delete, doctor_list, doctor_detail, doctor_update, doctor_delete, event_list, event_detail, \
    event_update, event_delete, microchip_list, microchip_detail, microchip_update, microchip_delete, \
    walk_detail, walk_update, walk_delete, training_list, training_detail, training_update, training_delete, \
    health_list, health_detail, health_update, health_delete, appointment_list, appointment_detail, appointment_update, \
    appointment_delete, vaccination_record_list, vaccination_record_detail, vaccination_record_update, \
    vaccination_record_delete, dog_breed_prediction_list, dog_breed_prediction_detail, dog_breed_prediction_update, \
    dog_breed_prediction_delete, user_profile, user_profile_list, user_profile_update, user_profile_delete, walks_list, \
    create_walk, adoption_form, adoptionSuccess, adoption_list, groomer_list, grooming_list, register, login_view, \
    custom_logout, walkers_list, groomers_list, sitters_list, home, resource_detail, trainers_list, create_trainer, \
    trainer_detail, update_trainer, delete_trainer, doctor_booking_list, doctor_booking_create, doctor_booking_update, \
    doctor_booking_delete, trainer_booking_list, trainer_booking_create, trainer_booking_update, trainer_booking_delete, \
    walker_booking_list, walker_booking_create, walker_booking_update, walker_booking_delete, sitter_booking_list, \
    sitter_booking_create, sitter_booking_update, sitter_booking_delete, groomer_booking_list, groomer_booking_create, \
    groomer_booking_update, groomer_booking_delete, ServiceViewSet, AvailabilityViewSet, BookingViewSet
from .views import OwnerViewSet, ShelterViewSet, DoctorViewSet, AppointmentViewSet, VaccinationRecordViewSet, EventViewSet
from django.views.generic import TemplateView

router = DefaultRouter()
router.register(r'dogs', DogViewSet)
router.register(r'walks', WalkViewSet)
router.register(r'breeds', BreedViewSet)
router.register(r'trainings', TrainingViewSet)
router.register(r'healths', HealthViewSet)
router.register(r'foods', FoodViewSet)
router.register(r'friendly_spots', FriendlySpotViewSet)
router.register(r'owners', OwnerViewSet)
router.register(r'shelters', ShelterViewSet)
router.register(r'doctors', DoctorViewSet)
router.register(r'appointments', AppointmentViewSet)
router.register(r'vaccination_records', VaccinationRecordViewSet)
router.register(r'events', EventViewSet)
router.register(r'microchips', MicrochipViewSet)
router.register(r'predictions', DogBreedPredictionViewSet)
router.register(r'userprofiles', UserProfileViewSet)
router.register(r'services', ServiceViewSet)
router.register(r'availabilities', AvailabilityViewSet)
router.register(r'bookings', BookingViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),  # This line adds authentication URLs

    path('', home, name='home'),

    path('dogs/', dogs_list, name='dogs_list'),
    path('dogs/<int:dog_id>/', dog_detail, name='dog_detail'),
    path('dogs/create/', create_dog, name='create_dog'),
    path('dogs/update/<int:dog_id>/', update_dog, name='update_dog'),
    path('dogs/delete/<int:dog_id>/', delete_dog, name='delete_dog'),

    path('breeds/', breeds_list, name='breeds_list'),
    path('breeds/<str:breed_name>/', breed_detail, name='breed_detail'),
    path('breeds/delete/<str:breed_name>/', delete_breed, name='delete_breed'),
    path('breeds/update/<str:breed_name>/', update_breed, name='update_breed'),

    path('foods/', food_list, name='food_list'),
    path('foods/<int:food_id>/', food_detail, name='food_detail'),
    path('foods/<int:food_id>/delete/', food_delete, name='food_delete'),
    path('foods/<int:food_id>/update/', food_update, name='food_update'),

    path('friendlyspots/', friendlyspot_list, name='friendlyspots_list'),
    path('friendlyspots/<int:spot_id>/', friendlyspot_detail, name='friendlyspot_detail'),
    path('friendlyspots/<int:spot_id>/update/', friendlyspot_update, name='friendlyspot_update'),
    path('friendlyspots/<int:spot_id>/delete/', friendlyspot_delete, name='friendlyspot_delete'),

    path('owners/', owner_list, name='owners_list'),
    path('owners/<int:owner_id>/', owner_detail, name='owner_detail'),
    path('owners/<int:owner_id>/update/', owner_update, name='owner_update'),
    path('owners/<int:owner_id>/delete/', owner_delete, name='owner_delete'),

    path('shelters/', shelter_list, name='shelters_list'),
    path('shelters/<int:shelter_id>/', shelter_detail, name='shelter_detail'),
    path('shelters/<int:shelter_id>/update/', shelter_update, name='shelter_update'),
    path('shelters/<int:shelter_id>/delete/', shelter_delete, name='shelter_delete'),

    path('doctors/', doctor_list, name='doctors_list'),
    path('doctors/<int:doctor_id>/', doctor_detail, name='doctor_detail'),
    path('doctors/<int:doctor_id>/update/', doctor_update, name='doctor_update'),
    path('doctors/<int:doctor_id>/delete/', doctor_delete, name='doctor_delete'),

    path('events/', event_list, name='events_list'),
    path('events/<int:event_id>/', event_detail, name='event_detail'),
    path('events/<int:event_id>/update/', event_update, name='event_update'),
    path('events/<int:event_id>/delete/', event_delete, name='event_delete'),

    path('microchips/', microchip_list, name='microchips_list'),
    path('microchips/<int:microchip_id>/', microchip_detail, name='microchip_detail'),
    path('microchips/<int:microchip_id>/update/', microchip_update, name='microchip_update'),
    path('microchips/<int:microchip_id>/delete/', microchip_delete, name='microchip_delete'),

    path('walks/', walks_list, name='walks_list'),
    path('walks/create/', create_walk, name='create_walk'),
    path('walks/<int:walk_id>/', walk_detail, name='walk_detail'),
    path('walks/<int:walk_id>/update/', walk_update, name='walk_update'),
    path('walks/<int:walk_id>/delete/', walk_delete, name='walk_delete'),
    path('walkers/', walkers_list, name='walkers_list'),

    path('trainings/', training_list, name='trainings_list'),
    path('trainings/<int:training_id>/', training_detail, name='training_detail'),
    path('trainings/<int:training_id>/update/', training_update, name='training_update'),
    path('trainings/<int:training_id>/delete/', training_delete, name='training_delete'),

    path('health/', health_list, name='healths_list'),
    path('health/<int:health_id>/', health_detail, name='health_detail'),
    path('health/<int:health_id>/update/', health_update, name='health_update'),
    path('health/<int:health_id>/delete/', health_delete, name='health_delete'),

    path('appointments/', appointment_list, name='appointments_list'),
    path('appointments/<int:appointment_id>/', appointment_detail, name='appointment_detail'),
    path('appointments/<int:appointment_id>/update/', appointment_update, name='appointment_update'),
    path('appointments/<int:appointment_id>/delete/', appointment_delete, name='appointment_delete'),

    path('vaccination-records/', vaccination_record_list, name='vaccinationrecords_list'),
    path('vaccination-records/<int:vaccination_record_id>/', vaccination_record_detail, name='vaccination_record_detail'),
    path('vaccination-records/<int:vaccination_record_id>/update/', vaccination_record_update, name='vaccination_record_update'),
    path('vaccination-records/<int:vaccination_record_id>/delete/', vaccination_record_delete, name='vaccination_record_delete'),

    path('dog-breed-predictions/', dog_breed_prediction_list, name='predictions_list'),
    path('dog-breed-predictions/<int:prediction_id>/', dog_breed_prediction_detail, name='dog_breed_prediction_detail'),
    path('dog-breed-predictions/<int:prediction_id>/update/', dog_breed_prediction_update, name='dog_breed_prediction_update'),
    path('dog-breed-predictions/<int:prediction_id>/delete/', dog_breed_prediction_delete, name='dog_breed_prediction_delete'),

    path('profile/', user_profile, name='profile'),
    path('profiles/', user_profile_list, name='user_profile_list'),
    path('profiles/<int:profile_id>/update/', user_profile_update, name='user_profile_update'),
    path('profiles/<int:profile_id>/delete/', user_profile_delete, name='user_profile_delete'),

    path('adoption/', adoption_form, name='adoption_form'),
    path('success/', adoptionSuccess, name='adoptionSuccess'),

    path('register/', register, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', custom_logout, name='logout'),

    path('groomers/', groomers_list, name='groomers_list'),

    path('sitters/', sitters_list, name='sitters_list'),

    path('resources/<slug:slug>/', resource_detail, name='resource_detail'),

    path('trainers/', trainers_list, name='trainers_list'),
    path('trainers/<int:trainer_id>/', trainer_detail, name='trainer_detail'),
    path('trainers/create/', create_trainer, name='create_trainer'),
    path('trainers/<int:trainer_id>/update/', update_trainer, name='update_trainer'),
    path('trainers/<int:trainer_id>/delete/', delete_trainer, name='delete_trainer'),

    path('bookings/doctors/', doctor_booking_list, name='doctor_booking_list'),
    path('bookings/doctors/create/', doctor_booking_create, name='doctor_booking_create'),
    path('bookings/doctors/update/<int:pk>/', doctor_booking_update, name='doctor_booking_update'),
    path('bookings/doctors/delete/<int:pk>/', doctor_booking_delete, name='doctor_booking_delete'),

    path('bookings/trainers/', trainer_booking_list, name='trainer_booking_list'),
    path('bookings/trainers/create/', trainer_booking_create, name='trainer_booking_create'),
    path('bookings/trainers/update/<int:pk>/', trainer_booking_update, name='trainer_booking_update'),
    path('bookings/trainers/delete/<int:pk>/', trainer_booking_delete, name='trainer_booking_delete'),

    path('bookings/walkers/', walker_booking_list, name='walker_booking_list'),
    path('bookings/walkers/create/', walker_booking_create, name='walker_booking_create'),
    path('bookings/walkers/update/<int:pk>/', walker_booking_update, name='walker_booking_update'),
    path('bookings/walkers/delete/<int:pk>/', walker_booking_delete, name='walker_booking_delete'),

    path('bookings/sitters/', sitter_booking_list, name='sitter_booking_list'),
    path('bookings/sitters/create/', sitter_booking_create, name='sitter_booking_create'),
    path('bookings/sitters/update/<int:pk>/', sitter_booking_update, name='sitter_booking_update'),
    path('bookings/sitters/delete/<int:pk>/', sitter_booking_delete, name='sitter_booking_delete'),

    path('bookings/groomers/', groomer_booking_list, name='groomer_booking_list'),
    path('bookings/groomers/create/', groomer_booking_create, name='groomer_booking_create'),
    path('bookings/groomers/update/<int:pk>/', groomer_booking_update, name='groomer_booking_update'),
    path('bookings/groomers/delete/<int:pk>/', groomer_booking_delete, name='groomer_booking_delete'),

    # serializer view
    path('api/adoptions/', adoption_list, name='adoption_list'),
    path('api/groomers/', groomer_list, name='groomer_list'),
    path('api/groomings/', grooming_list, name='grooming_list'),




]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

