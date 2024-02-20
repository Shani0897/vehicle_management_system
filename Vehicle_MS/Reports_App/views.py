from django.shortcuts import render
from VManageIn_App.models import VehicleIn, VEHICLE_IN, VEHICLE_OUT
from django.http import JsonResponse
from django.core import serializers
import json

# Create your views here.


def report(request):

    if request.method == 'POST':
        from_date = request.POST.get('from_date')
        to_date = request.POST.get('to_date')
        selected_type = request.POST.get('select_type')

        if selected_type == 'all':
            vehicle_record = VehicleIn.objects.filter(vehicle_in_time__range = [from_date, to_date])

            data = serializers.serialize('json', vehicle_record)
            context = {
                'data': data,
                'all': 'all'
            }
            return JsonResponse(context, safe=False)
        
        if selected_type == 'incoming_vehicle':
            vehicle_record = VehicleIn.objects.filter(vehicle_status = VEHICLE_IN, vehicle_in_time__range = [from_date, to_date])
            data = serializers.serialize('json', vehicle_record)
            context = {
                'data': data
            }

            return JsonResponse(context, safe=False)
        
        if selected_type == 'outgoing_vehicle':
            vehicle_record = VehicleIn.objects.filter(vehicle_status = VEHICLE_OUT, vehicle_in_time__range = [from_date, to_date])

            data = serializers.serialize('json', vehicle_record)
            context = {
                'data': data
            }

            return JsonResponse(context, safe=False)
        
        if selected_type == 'vehicle_number':
            
            vehicle_registrationNumber = request.POST.get('vehicle_reg_number')
            vehicle_record = VehicleIn.objects.filter(registration_number = vehicle_registrationNumber, vehicle_in_time__range = [from_date, to_date])
            data = serializers.serialize('json', vehicle_record)
            context = {
                'data': data
            }

            return JsonResponse(context, safe=False)
        
        if selected_type == 'user_name':
            user_name = request.POST.get('owner_name')
            vehicle_record = list(VehicleIn.objects.filter(owner_name = user_name, vehicle_in_time__range = [from_date, to_date]))
            data = serializers.serialize('json', vehicle_record)
            context = {
                'data': data,
                'username': 'username'
            }
            return JsonResponse(context, safe=False)
        
        if selected_type == 'phone_number':
            phone_number = request.POST.get('contact_number')
            vehicle_record = VehicleIn.objects.filter(owner_contact_number = phone_number, vehicle_in_time__range = [from_date, to_date])
            data = serializers.serialize('json', vehicle_record)
            context = {
                'data': data
            }

            return JsonResponse(context, safe=False)
    else:

        return render(request, 'Reports_templates/report.html')