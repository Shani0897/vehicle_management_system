from django import forms
from .models import VehicleIn


class Vehicle_In_Form(forms.ModelForm):
    class Meta:
        model = VehicleIn
        fields =  [
        'vehicle_company_name','vehicle_in_time','registration_number','owner_name','owner_contact_number','vehicel_category'
        ]
        widgets = {
            'vehicel_category': forms.Select(attrs={'class':'form-select'}),
            'vehicle_company_name': forms.TextInput(attrs={'class':'form-control','placeholder':'vehicle company'}),
            'registration_number': forms.TextInput(attrs={'class':'form-control','placeholder':'registration number'}),
            'owner_name': forms.TextInput(attrs={'class':'form-control','placeholder':'owner name'}),
            'owner_contact_number': forms.TextInput(attrs={'class':'form-control','type':'tel','placeholder':'owner contact number'}),
            'vehicle_in_time': forms.DateTimeInput(attrs={'class':'form-control','type':'datetime-local'})
        }



class Vehicle_Update_Form(forms.ModelForm):
    class Meta:
        model = VehicleIn
        fields =  [
        'vehicle_in_time','vehicle_time_out','parking_charges','vehicle_status'
        ]
        widgets = {
            'vehicle_in_time': forms.DateTimeInput(attrs={'class':'form-control','type':'datetime-local','readonly':True}),
            'parking_charges': forms.TextInput(attrs={'class':'form-control','readonly': True}),
            'vehicle_time_out': forms.DateTimeInput(attrs={'class':'form-control','type':'datetime-local'}),
            'vehicle_status': forms.Select(attrs={'class':'form-select'})
        }
