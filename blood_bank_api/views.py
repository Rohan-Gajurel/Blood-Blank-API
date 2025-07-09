from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from blood_bank_main.models import Person
from blood_bank_api.serializer import PersonSerializer
# Create your views here.

class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    permission_class = AllowAny