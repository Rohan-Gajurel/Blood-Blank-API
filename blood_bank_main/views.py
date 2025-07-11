from django.shortcuts import render
from django.views.generic import TemplateView, ListView, CreateView

from blood_bank_main.models import BloodRequest, BloodStock, DonationCenter

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
    
class MakeBloodRequestView(CreateView):
    model= BloodRequest
    template_name = 'make_blood_request.html'
    form= 'blood_request_form'
    fields = ['phone_number', 'blood_group_required', 'quantity_required']
    success_url = '/blood_requests/'

class BloodRequestListView(ListView):
    model = BloodRequest
    template_name = 'blood_request_list.html'
    context_object_name = 'blood_requests_list'
    
