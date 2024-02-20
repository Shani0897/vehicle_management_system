from django.urls import path
from .views import vehicle_list_out, view_vehicle_record



urlpatterns = [
    path('manage-outgoingvehicle/', vehicle_list_out, name = 'vehicle_out_list'),
    path('view-outgoingvehicle/<int:id>', view_vehicle_record, name = 'view_vehicle_record')
]
