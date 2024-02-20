from django.shortcuts import render
from VManageIn_App.models import VehicleIn, VEHICLE_OUT
from django.core.paginator import Paginator

# Create your views here.


def vehicle_list_out(request):

    vehicle_out_list_records = VehicleIn.objects.filter(vehicle_status = VEHICLE_OUT)
    paginator = Paginator(vehicle_out_list_records, 10)
    page = request.GET.get('page')
    vehicle_list_records = paginator.get_page(page)

    records = paginator.get_page(page)

    context = {
        'vehicle_OutList_Data': vehicle_list_records,
        'records': records
    }

    return render(request, 'Vehicle_ManageOut_App/vehicle_out_list.html', context)



def view_vehicle_record(request, id):

    vehicle_record = VehicleIn.objects.get(pk=id)

    context = {
        'outVehicleRecord': vehicle_record
    }
    return render(request, 'Vehicle_ManageOut_App/view_vehicle.html', context)