
from django.db import models


class DonorScreening(models.Model):
    BLOOD_GROUPS = [
        ('A+', 'A+'), ('A-', 'A-'),
        ('B+', 'B+'), ('B-', 'B-'),
        ('AB+', 'AB+'), ('AB-', 'AB-'),
        ('O+', 'O+'), ('O-', 'O-'),
    ]

    SCREENING_STATUSES = [
        ('Pending', 'Pending'),
        ('Eligible', 'Eligible'),
        ('Ineligible', 'Ineligible'),
    ]

    full_name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    phone = models.CharField(max_length=15)
    blood_group = models.CharField(max_length=3, choices=BLOOD_GROUPS)
    screening_date = models.DateField()
    screening_status = models.CharField(
        max_length=15,
        choices=SCREENING_STATUSES,
        default='Pending',
    )

    def __str__(self):
        return self.full_name


class ComponentSeparation(models.Model):
    COMPONENT_TYPES = [
        ('RBC', 'Red Blood Cells'),
        ('Plasma', 'Plasma'),
        ('Platelets', 'Platelets'),
    ]

    donor = models.ForeignKey(
        DonorScreening,
        on_delete=models.PROTECT,
    )
    batch_number = models.CharField(max_length=30, unique=True)
    component_type = models.CharField(max_length=15, choices=COMPONENT_TYPES)
    quantity_units = models.PositiveIntegerField()
    separation_date = models.DateField()

    def __str__(self):
        return self.batch_number


class ColdStorage(models.Model):
    STORAGE_STATUSES = [
        ('Available', 'Available'),
        ('Reserved', 'Reserved'),
        ('Expired', 'Expired'),
        ('Quarantined', 'Quarantined'),
    ]

    component = models.ForeignKey(
        ComponentSeparation,
        on_delete=models.PROTECT,
    )
    storage_location = models.CharField(max_length=50)
    expiry_date = models.DateField()
    available_units = models.PositiveIntegerField()
    status = models.CharField(
        max_length=15,
        choices=STORAGE_STATUSES,
        default='Available',
    )

    def __str__(self):
        return self.storage_location


class Dispatch(models.Model):
    DISPATCH_STATUSES = [
        ('Pending', 'Pending'),
        ('Approved', 'Approved'),
        ('Dispatched', 'Dispatched'),
        ('Cancelled', 'Cancelled'),
    ]

    storage = models.ForeignKey(
        ColdStorage,
        on_delete=models.PROTECT,
    )
    recipient_hospital = models.CharField(max_length=150)
    quantity_units = models.PositiveIntegerField()
    dispatch_date = models.DateField()
    authorized_by = models.CharField(max_length=100)
    status = models.CharField(
        max_length=15,
        choices=DISPATCH_STATUSES,
        default='Pending',
    )

    def __str__(self):
        return self.recipient_hospital


