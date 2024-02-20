from django.shortcuts import render
from .forms import Vehicle_In_Form, Vehicle_Update_Form
from .models import VehicleIn, VEHICLE_IN
from django.http import JsonResponse
from django.core.paginator import Paginator

# Create your views here.


def vehicle_manageList(request):

    vehicle_data = VehicleIn.objects.filter(vehicle_status = VEHICLE_IN)
    paginator = Paginator(vehicle_data, 10)
    page = request.GET.get('page')
    vehicle_records = paginator.get_page(page)

    records = paginator.get_page(page)

    context = {
        'vehicleData': vehicle_records,
        'records': records
    }

    return render(request, 'Vehicle_Manage_In_App/vehicleManageList.html',context)


def vehicle_add_page(request):
    
    if request.method == 'POST':
        vehicle_form = Vehicle_In_Form(request.POST)

        if vehicle_form.is_valid():
            
            vehicle_form.save()

            return JsonResponse({'success':'successfully save','redirect_url':'/vehicle-manageIn/manageIn-vehicle/'})
        else:
            errors = vehicle_form.errors.as_json()
            return JsonResponse({'errors':errors})
    else:
        vehicle_form = Vehicle_In_Form()

    context ={
        'vehicleForm': vehicle_form
    }

    return render(request, 'Vehicle_Manage_In_App/vehicle_add.html', context)



def vehicle_update(request, id):

    if request.method == 'POST':

        vehicle_record = VehicleIn.objects.get(pk=id)  
        vehicle_update_form = Vehicle_Update_Form(request.POST, instance=vehicle_record)

        if vehicle_update_form.is_valid():
            vehicle_update_form.save()

            data = {'success':'successfully update','redirect_url':'/vehicle-manageIn/manageIn-vehicle/'}

            return JsonResponse(data)
    else:
        vehicle_record = VehicleIn.objects.get(pk=id)  
        vehicle_update_form = Vehicle_Update_Form(instance=vehicle_record)
    
    context = {
        'vehicleForm': vehicle_update_form,
        'vehicleRecord': vehicle_record,
        # 'parking_charges': parking_charges
    }
    return render(request, 'Vehicle_Manage_In_App/vehicle_update_page.html', context)