from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms


class SignUp_Form(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
        widgets ={
            'username': forms.TextInput(attrs={'class': 'form-control fst-italic text-capitalize','placeholder':'enter username'}),
            'first_name': forms.TextInput(attrs={'class':'form-control fst-italic text-capitalize','placeholder':'enter first name'}),
            'last_name': forms.TextInput(attrs={'class':'form-control fst-italic text-capitalize','placeholder':'enter last name'}),
            'email': forms.EmailInput(attrs={'class':'form-control fst-italic mb-0','placeholder':'example@gmail.com'})
        }


# class UserUpdateForm(UserChangeForm):
#     class Meta:
#         model = User
#         fields = ['username', 'first_name', 'last_name', 'email','password']
#         widgets ={
#             'username': forms.TextInput(attrs={'class': 'form-control fst-italic text-capitalize','placeholder':'enter username'}),
#             'first_name': forms.TextInput(attrs={'class':'form-control fst-italic text-capitalize','placeholder':'enter first name'}),
#             'last_name': forms.TextInput(attrs={'class':'form-control fst-italic text-capitalize','placeholder':'enter last name'}),
#             'email': forms.EmailInput(attrs={'class':'form-control fst-italic mb-0','placeholder':'example@gmail.com'})
#         }