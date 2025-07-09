from django.contrib import admin

from blood_bank_main.models import BloodBankBranch, BloodRequest, BloodStock, DonationCenter, Donations, Hospital, Person
# Register your models here.
admin.site.register(Person)
admin.site.register(DonationCenter)
admin.site.register(Hospital)
admin.site.register(BloodBankBranch)
admin.site.register(BloodRequest)
admin.site.register(Donations)
admin.site.register(BloodStock)
