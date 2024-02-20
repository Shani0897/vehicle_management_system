from django.shortcuts import render
from django.http import JsonResponse
from .forms import Add_Category_Form
from .models import Add_Category
from django.core.exceptions import ObjectDoesNotExist
from django.views.decorators.csrf import csrf_exempt
from django.db.models import F
from django.core.paginator import Paginator
# Create your views here.


def category(request):

    category_data = Add_Category.objects.all()
    paginator = Paginator(category_data, 10)
    page = request.GET.get('page')
    category_records = paginator.get_page(page)

    records = paginator.get_page(page)

    context = {
        'categoryData': category_records,
        'records': records
    }

    return render(request, 'CategoryApp/categoryList.html', context)


# ADD_____________CATEGORY____________CODE___________START

def add_category(request):

    if request.method == 'POST':
        add_category_form = Add_Category_Form(request.POST)

        if add_category_form.is_valid():
            try:
                category_name = request.POST['category_name']
                existing_item = Add_Category.objects.get(
                    category_name=category_name)
                return JsonResponse({'duplicate_error': f'{existing_item} already exist!'})
            except ObjectDoesNotExist:
                add_category_form.save()
                data = {'success': 'saved successfully',
                    'redirect_url': '/vehicle-category/category/'}
                return JsonResponse(data, safe=False)
        else:
            errors = add_category_form.errors.as_json()
            return JsonResponse({'errors': errors})
    else:
        add_category_form = Add_Category_Form()

    return render(request, 'CategoryApp/addCategory.html', {'addCategoryForm': add_category_form})



# EDIT__________________CATEGORY____________________RECORD

def category_edit(request, id):

    if request.method == 'POST':

        record_id = Add_Category.objects.get(pk=id)
        edit_form = Add_Category_Form(request.POST, instance=record_id)
        if edit_form.is_valid():

            edit_form.save()
            data = {'success': 'updated successfully', 'redirect_url': '/vehicle-category/category/'}
            return JsonResponse(data)
        else:
            errors = edit_form.errors.as_json()
            return JsonResponse({'errors': errors})
    else:
        record_id = Add_Category.objects.get(pk=id)
        edit_form = Add_Category_Form(instance=record_id)

    return render(request, 'CategoryApp/edit_category.html', {'editForm': edit_form})


# DELETE___________CATEGORY_____________RECORD

@csrf_exempt
def del_category_record(request, record_id):

    delete_category_record = Add_Category.objects.get(id=record_id)

    current_position = delete_category_record.id

    delete_category_record.delete()

    Add_Category.objects.filter(id__gt=current_position).update(id=F('id')-1)

    objects = Add_Category.objects.all().order_by('id')
    data = [{'id': obj.id, 'name': obj.category_name} for obj in objects]

    return JsonResponse({'message': 'deleted successfully.','objects':data  ,'redirect_url': '/vehicle-category/category/'})