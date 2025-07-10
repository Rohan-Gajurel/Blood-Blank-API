from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated
from blood_bank_main.models import BloodBankBranch, BloodRequest, BloodStock, DonationCenter, Donations, Hospital, Person
from blood_bank_api.serializer import BloodBankBranchSerializer, BloodRequestSerializer, BloodStockSerializer, DonationCenterSerializer, DonationsSerializer, HospitalSerializer, PersonSerializer

class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    permission_class = AllowAny

    def get_permissions(self):
        if self.action in['list','retrive']:
            self.permission_class = [AllowAny]

        return super().get_permissions()
        
class HospitalViewSet(viewsets.ModelViewSet):
    queryset = Hospital.objects.all()
    serializer_class = HospitalSerializer
    permission_class = IsAuthenticated

    def get_permissions(self):
        if self.action in['list','retrive']:
            self.permission_class = [AllowAny]

        return super().get_permissions()

class BloodBankBranchViewSet(viewsets.ModelViewSet):
    queryset = BloodBankBranch.objects.all()
    serializer_class = BloodBankBranchSerializer
    permission_class = IsAuthenticated

    def get_permissions(self):
        if self.action in['list','retrive']:
            self.permission_class = [AllowAny]

        return super().get_permissions()

class BloodStockViewSet(viewsets.ModelViewSet):
    queryset = BloodStock.objects.all()
    serializer_class = BloodStockSerializer
    permission_class = IsAuthenticated

    def get_permissions(self):
        if self.action in['list','retrive']:
            self.permission_class = [AllowAny]

        return super().get_permissions()

class BloodRequestViewSet(viewsets.ModelViewSet):
    queryset = BloodRequest.objects.all()  
    serializer_class = BloodRequestSerializer  
    permission_class = IsAuthenticated

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.user.is_authenticated:
            queryset = queryset.filter(status in ['Pending', 'Approved'])
        return queryset

    def get_permissions(self):
        if self.action in['list','retrive']:
            self.permission_class = [AllowAny]

        return super().get_permissions()

class DonationCenterViewSet(viewsets.ModelViewSet):
    queryset = DonationCenter.objects.all()
    serializer_class = DonationCenterSerializer
    permission_class = IsAuthenticated

    def get_permissions(self):
        if self.action in['list','retrive']:
            self.permission_class = [AllowAny]

        return super().get_permissions()

class DonationsViewSet(viewsets.ModelViewSet):
    queryset = Donations.objects.all()
    serializer_class = DonationsSerializer
    permission_class = IsAuthenticated

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.user.is_authenticated:
            queryset = queryset.filter(expire_date__gte=datetime.date.today())
        return queryset

    def get_permissions(self):
        if self.action in['list','retrive']:
            self.permission_class = [AllowAny]

        return super().get_permissions()