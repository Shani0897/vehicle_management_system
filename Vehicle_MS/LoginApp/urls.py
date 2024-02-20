from django.urls import path
from .views import login_page, signUp, dashboard, logout_page, profile

urlpatterns = [
    path('', login_page, name = 'login_page'),
    path('signpage/', signUp, name = 'signpage'),
    path('dashboard/', dashboard, name = 'dashboard'),
    path('logout/', logout_page, name = 'logout_page'),
    path('profile/', profile, name = 'profile')
]
