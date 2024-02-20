from django.urls import path
from .views import category, add_category, category_edit, del_category_record


urlpatterns = [
    path('category/', category, name = 'category'),
    # path('category/<int:id>', del_category_record, name = 'category'),
    path('add-category/', add_category, name = 'add_category'),
    path('update-vehicle-category/<int:id>', category_edit, name = 'update_category'),
    path('delete-category/<int:record_id>/', del_category_record, name = 'delete_category')
]
