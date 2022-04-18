from django.db import models
from common.models import TSFieldsIndexed

from datetime import date


# Create your models here.
class Registration(TSFieldsIndexed):
    stuff_id = models.TextField(max_length=100)
    full_name = models.TextField(max_length=100)
    department = models.TextField(max_length=100)
    phone_no = models.TextField(max_length=100)
    designation = models.TextField(max_length=100)
    vehicle_number = models.TextField(max_length=100)
    v_type = [
        ('Car', 'Car'),
        ('Motor Bike', 'Motor Bike'),
        ('Pickup Van', 'Pickup Van'),
    ]
    vehicle_type = models.TextField(choices=v_type, max_length=100, blank=False)
    status_choices = (('In', 'In'),
                      ('Out', 'Out'),
                      )
    status = models.CharField(max_length=100, choices=status_choices, default="Out")

    # name,department,designation,phone no,car no,

    def __str__(self):
        return self.vehicle_number


class Entry(TSFieldsIndexed):
    user = models.ForeignKey(Registration, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user)


class Exit(TSFieldsIndexed):
    user = models.ForeignKey(Registration, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user)


class logbook(TSFieldsIndexed):
    user = models.ForeignKey(Registration, on_delete=models.CASCADE)
    status_choices = (('In', 'In'),
                      ('Out', 'Out'),
                      )
    status = models.CharField(max_length=100, choices=status_choices)

    def __str__(self):
        return str(self.user)

class UnregisteredVehicle(TSFieldsIndexed):
    urnumber=models.CharField(max_length=100)

    def __str__(self):
        return str(self.urnumber)

class History(TSFieldsIndexed):
    platenumber=models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "History"
    def __str__(self):
        return str(self.platenumber)
class HistoryUnregistered(TSFieldsIndexed):
    platenumber = models.CharField(max_length=100)

    class Meta:
        verbose_name = "HistoryUnregistered"
    def __str__(self):
        return str(self.platenumber)