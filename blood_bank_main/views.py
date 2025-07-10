from django.shortcuts import render
from django.views.generic import TemplateView, ListView

from blood_bank_main.models import BloodStock, DonationCenter

# Create your views here.
class HomeView(TemplateView):
    template_name = 'home.html'

class BloodAvailabilityView(ListView):
    model= BloodStock
    template_name = 'blood_availability.html'
    context_object_name = 'blood_availability_list'

    def get_queryset(self):
        return BloodStock.objects.all()

class DonationCampsView(ListView):
    model = DonationCenter
    template_name = 'donation_camps.html'
    context_object_name = 'donation_camps_list'

    def get_queryset(self):
        return DonationCenter.objects.all()