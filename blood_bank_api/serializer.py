from rest_framework import serializers

from blood_bank_main.models import BloodBankBranch, BloodRequest, BloodStock, DonationCenter, Donations, Hospital, Person

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model=Person
        fields = '__all__'

class HospitalSerializer(serializers.ModelSerializer):
    class Meta:
        model=Hospital
        fields = '__all__'

class BloodBankBranchSerializer(serializers.ModelSerializer):
    class Meta:
        model=BloodBankBranch
        fields = '__all__'

class BloodStockSerializer(serializers.ModelSerializer):
    class Meta:
        model=BloodStock
        fields = '__all__'

class DonationCenterSerializer(serializers.ModelSerializer):
    class Meta:
        model=DonationCenter
        fields = '__all__'

class DonationsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Donations
        fields = '__all__'

class BloodRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model=BloodRequest
        fields = '__all__'

