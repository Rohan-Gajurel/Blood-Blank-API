from django.db import models

# Create your models here.
class Person(models.Model):
    GENDER_CHOICES = [("M", "Male"), ("F", "Female"), ("O", "Other")]
    ROLE_CHOICES = [("Donor", "Donor"), ("Receiver", "Receiver"), ("Both", "Both")]
    BLOOB_GROUP_CHOICES = [
        ("A+", "A+"),
        ("A-", "A-"),
        ("B+", "B+"),
        ("B-", "B-"),
        ("AB+", "AB+"),
        ("AB-", "AB-"),
        ("O+", "O+"),
        ("O-", "O-"),
    ]
    MEDICAL_CONDITION=[("None", "None"), ("Anemia", "Anemia"), ("Diabetes", "Diabetes"), ("Hypertension", "Hypertension")]

    first_name = models.CharField(max_length=55)
    middle_name = models.CharField(max_length=55, null=True, blank=True)
    last_name = models.CharField(max_length=55)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    address = models.CharField(max_length=55)
    blood_group = models.CharField(max_length=5, choices=BLOOB_GROUP_CHOICES, null=True)
    dob = models.DateField()
    contact_number = models.CharField(max_length=15, unique=True)
    email = models.EmailField(max_length=254, unique=True, null=True, blank=True)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)

    # Donor-specific fields (can be null for non-donors)
    latest_donation_date = models.DateField(null=True, blank=True)
    medical_condition_donor = models.CharField(max_length=30, null=True, blank=True)

    # Receiver-specific fields (can be null for non-receivers)
    latest_transfusion_date = models.DateField(null=True, blank=True)
    medical_condition_receiver = models.CharField(max_length=30, null=True, blank=True)
    quantity_required = models.IntegerField(null=True, blank=True)
    hospital=models.ForeignKey('Hospital', on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.first_name

class Hospital(models.Model):
    name= models.CharField(max_length=100, null=False)
    address = models.CharField(max_length=255, null=False)
    contact_number = models.CharField(max_length=15, null=False, unique=True)
    def __str__(self):
        return self.name
    
class BloodBankBranch(models.Model):
    name = models.CharField(max_length=100, null=False)
    address = models.CharField(max_length=255, null=False)
    contact_number = models.CharField(max_length=15, null=False, unique=True)
    def __str__(self):
        return self.name

class BloodStock(models.Model):
    branch = models.ForeignKey(BloodBankBranch, on_delete=models.CASCADE)
    blood_group = models.CharField(max_length=5, null=False)
    quantity = models.PositiveIntegerField(null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.branch.name

class DonationCenter(models.Model):
    name = models.CharField(max_length=100, null=False)
    address = models.CharField(max_length=255, null=False)
    contact_number = models.CharField(max_length=15, null=False, unique=True)
    def __str__(self):
        return self.name

class Donations(models.Model):
    blood_group = models.CharField(max_length=5, null=False)
    donor = models.ForeignKey(Person, on_delete=models.CASCADE, null=False)
    donation_center = models.ForeignKey(DonationCenter, on_delete=models.CASCADE, null=False)
    date_collected = models.DateField(null=False)
    expire_date = models.DateField(null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.blood_group


class BloodRequest(models.Model):
    receiver = models.ForeignKey(Person, on_delete=models.CASCADE, null=False)
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE, null=False)
    blood_group_required = models.CharField(max_length=5, null=False)
    quantity_required = models.PositiveIntegerField(null=False)
    request_date = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=[("Pending", "Pending"), ("Approved", "Approved"), ("Rejected", "Rejected")], default="Pending")
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.receiver.first_name

