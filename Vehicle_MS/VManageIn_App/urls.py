from django.urls import path
from .views import vehicle_manageList, vehicle_add_page, vehicle_update

urlpatterns = [
    path('manageIn-vehicle/', vehicle_manageList, name = 'vehicle_manage'),
    path('add-vehicle/', vehicle_add_page, name = 'add_vehicle'),
    path('view-vehicle/<int:id>', vehicle_update, name = 'view_vehicle'),
]
