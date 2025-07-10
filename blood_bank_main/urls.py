
from django.urls import path, include
from .views import BloodAvailabilityView, DonationCampsView, HomeView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('blood_availability/', BloodAvailabilityView.as_view(), name='blood_availability'),
    path('donation_camps/', DonationCampsView.as_view(), name='donation_camps'),
]
