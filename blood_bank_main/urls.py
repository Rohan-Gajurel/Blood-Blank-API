
from django.urls import path, include
from .views import BloodAvailabilityView, BloodRequestListView, DonationCampsView, HomeView, MakeBloodRequestView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('blood_availability/', BloodAvailabilityView.as_view(), name='blood_availability'),
    path('donation_camps/', DonationCampsView.as_view(), name='donation_camps'),
    path('make_blood_request/', MakeBloodRequestView.as_view(), name='make_blood_request'),
    path('blood_request_list/', BloodRequestListView.as_view(), name='blood_request_list'),
]
