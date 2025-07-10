from django.urls import path, include
from rest_framework import routers
from blood_bank_api import views

router= routers.DefaultRouter()
router.register(r'person', views.PersonViewSet)
router.register(r'hospital', views.HospitalViewSet)
router.register(r'blood_bank_branch', views.BloodBankBranchViewSet)
router.register(r'blood_stock', views.BloodStockViewSet)
router.register(r'blood_request', views.BloodRequestViewSet)
router.register(r'donation_center', views.DonationCenterViewSet)
router.register(r'donations', views.DonationsViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
