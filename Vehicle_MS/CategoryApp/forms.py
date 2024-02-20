from django import forms
from .models import Add_Category


class Add_Category_Form(forms.ModelForm):
    class Meta:
        model = Add_Category
        fields = '__all__'
        widgets = {
            'category_name': forms.TextInput(attrs={'class':'form-control','placeholder':'name'}),
            'parking_charges_per_hour': forms.TextInput(attrs={'class':'form-control','type':'number','placeholder':'parking charges per hour'}),
            'category_status': forms.Select(attrs={'class':'form-select'})
        }



class Edit_Category_Form(forms.ModelForm):
    class Meta:
        model = Add_Category
        fields = '__all__'
        widgets = {
            'category_name': forms.TextInput(attrs={'class':'form-control','placeholder':'name'}),
            'parking_charges_per_hour': forms.TextInput(attrs={'class':'form-control','type':'number','placeholder':'parking charges per hour'}),
            'category_status': forms.Select(attrs={'class':'form-select'})
        }