from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DogViewSet, WalkViewSet, BreedViewSet, TrainingViewSet, HealthViewSet, FoodViewSet, \
    FriendlySpotViewSet, MicrochipViewSet, DogBreedPredictionViewSet, UserProfileViewSet, PredictionRatingViewSet, \
    dogs_list, dog_detail, create_dog, update_dog
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
router.register(r'predictionratings', PredictionRatingViewSet)
router.register(r'userprofiles', UserProfileViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('', TemplateView.as_view(template_name='homepage.html'), name='home'),
    path('dogs/', dogs_list, name='dogs_list'),
    path('dogs/<int:dog_id>/', dog_detail, name='dog_detail'),
    path('dogs/create/', create_dog, name='create_dog'),
    path('dogs/update/<int:dog_id>/', update_dog, name='update_dog'),
]