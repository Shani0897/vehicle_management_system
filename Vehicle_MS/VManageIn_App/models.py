from django.db import models
from CategoryApp.models import Add_Category
import random
from django.utils import timezone

# Create your models here.

VEHICLE_IN = 'vechicle in'
VEHICLE_OUT = 'vechicle out'

vehicleStatus = (
    (VEHICLE_IN, 'vehicle in'),
    (VEHICLE_OUT, 'vehicle out')
)

class VehicleIn(models.Model):
    vehicel_category = models.ForeignKey(Add_Category, on_delete=models.PROTECT)
    vehicle_company_name = models.CharField(max_length=100)
    registration_number = models.CharField(max_length=100)
    owner_name = models.CharField(max_length=100, null=True)
    owner_contact_number = models.CharField(max_length=16)
    vehicle_in_time = models.DateTimeField(blank=True, null=True)
    vehicle_status = models.CharField(max_length=100, choices=vehicleStatus ,default=VEHICLE_IN)
    parking_number = models.IntegerField(null=True)
    vehicle_time_out = models.DateTimeField(blank=True, null=True)
    parking_charges = models.CharField(max_length=100, null=True)


    def save(self):

        if not self.parking_number:

            self.parking_number = random.randint(10000, 90000)
            while VehicleIn.objects.filter(parking_number = self.parking_number).exists():

                self.parking_number = random.randint(10000, 90000)
            
        super().save()
