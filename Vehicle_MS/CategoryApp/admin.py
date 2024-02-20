from django.contrib import admin
from .models import Add_Category

# Register your models here.

@admin.register(Add_Category)
class AddCategory(admin.ModelAdmin):
    list_display = ('id', 'category_name', 'parking_charges_per_hour', 'category_status')