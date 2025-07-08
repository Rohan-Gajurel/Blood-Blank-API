from django.contrib import admin

from blood_bank_main.models import BloodBankBranch, DonationCenter, Hospital, Person
# Register your models here.
admin.site.register(Person)
admin.site.register(DonationCenter)
admin.site.register(Hospital)
admin.site.register(BloodBankBranch)
