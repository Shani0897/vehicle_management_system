from django.urls import path
from .views import report


urlpatterns = [
    path('reports/', report, name = 'report')
]
