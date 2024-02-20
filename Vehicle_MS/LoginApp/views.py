from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.http import JsonResponse
from .forms import SignUp_Form
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from VManageIn_App.models import VehicleIn, VEHICLE_IN
from CategoryApp.models import Add_Category
from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.db.models import F

# Create your views here.


def signUp(request):

    if request.method == 'POST':
        signUp_form = SignUp_Form(request.POST)

        if signUp_form.is_valid():
            
            signUp_form.save()
            data = {'success':'successfully submit'}
            return JsonResponse(data, safe=False)
        else:
            errors = signUp_form.errors.as_json()
            return JsonResponse({'errors': errors})
    else:
        signUp_form = SignUp_Form()
        
    return render(request, 'LoginApp/signUp.html', {'signUp_Form': signUp_form})

def login_page(request):
    
    if not request.user.is_authenticated:
        if request.method == 'POST':
            login_form = AuthenticationForm(request, data=request.POST)

            if login_form.is_valid():
                username = login_form.cleaned_data['username']
                password = login_form.cleaned_data['password']
                user_check = authenticate(request, username=username, password=password)
                if user_check is not None:
                    login(request, user_check)
                    return JsonResponse({'success': 'successfully', 'redirect_url': '/dashboard/'})
            else:
                errors = login_form.errors.as_json()
                return JsonResponse({'errors': errors})
        else:
            login_form = AuthenticationForm()

        return render(request, 'LoginApp/login_page.html', {'loginForm': login_form})
    else:
        return redirect('/dashboard/')


def logout_page(request):
    logout(request)
    return redirect('/')


@login_required
def dashboard(request):

    vehicle_data = VehicleIn.objects.filter(vehicle_status = VEHICLE_IN)
    total_incoming_vehicle = VehicleIn.objects.filter(vehicle_status = VEHICLE_IN).count()
    vehicle_category = Add_Category.objects.all().count()
    
    today = datetime.today()
    today_incoming_entry = VehicleIn.objects.filter(vehicle_in_time__date = today).count()
    today_outgoing_entry = VehicleIn.objects.filter(vehicle_time_out__date = today).count()

    # for i, records in enumerate(vehicle_data):
    #     records.id = i + 1
    #     records.save(update_fields = ['id'])

    context = {
        'vehicleData': vehicle_data,
        'totalIncomingVehicle': total_incoming_vehicle,
        'vehicleCategory': vehicle_category,
        'todayIncomingEntry': today_incoming_entry,
        'todayOutgoingEntry': today_outgoing_entry
    }

    return render(request, 'DashboardApp/dashboard.html', context)


@login_required
def profile(request):

    if request.method == 'POST':
        form = SignUp_Form(request.POST, instance = request.user)

        if form.is_valid():
            form.save()
            data = {
                'success': 'successfully update',
                'redirect_url': '/'
            }

            return JsonResponse(data)
        else:
            form_errors = form.errors.as_json()

            return JsonResponse({'errors': form_errors})
    else:
        form = SignUp_Form(instance = request.user)
    
    return render(request, 'DashboardApp/profile.html', {'profileForm': form})


def index(request):

    form = SignUp_Form(instance = request.user)

    return render(request, 'BaseTemplate/index.html',{'user':form})