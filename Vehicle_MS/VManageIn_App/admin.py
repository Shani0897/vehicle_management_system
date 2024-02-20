from django.contrib import admin
from .models import VehicleIn

# Register your models here.
@admin.register(VehicleIn)
class Vehicle_Manage_In(admin.ModelAdmin):
    list_display = [
        'id', 'vehicle_company_name','registration_number','owner_name','owner_contact_number',
        'vehicle_in_time','vehicle_time_out','vehicle_status','parking_number','vehicel_category',
        'parking_charges'
    ]


# @admin.register(Time_Out)
# class Time_Out_Manage(admin.ModelAdmin):
#     list_display = ['vehicle_out_time', 'vehicle_in_class']