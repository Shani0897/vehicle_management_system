from django.db import models
    

# Create your models here.


class Add_Category(models.Model):
    ACTIVE = 'Active'
    INACTIVE = 'Inactive'

    categoryStatus = (
        (ACTIVE, 'Active'),
        (INACTIVE, 'Inactive')
    )
    category_name = models.CharField(max_length=200)
    parking_charges_per_hour = models.IntegerField()
    category_status = models.CharField(
        max_length=100, choices=categoryStatus, default='active')

    def __str__(self) -> str:
        return self.category_name
    

    def save(self, *args, **kwargs):
        if not self.pk:  # Check if the record is being created for the first time
            if not Add_Category.objects.exists():
                self.id = 1
            else:
                highest_id = Add_Category.objects.order_by('-id').first().id
                self.id = highest_id + 1
        
        super().save(*args, **kwargs)  # Call the original save method to update the record


    # def save(self, *args, **kwargs):
    #     if not Add_Category.objects.exists():
    #         self.id = 1
    #     else:
    #         highest_id = Add_Category.objects.order_by('-id').first().id
    #         self.id = highest_id + 1
        
    #     super().save()


    # def save(self, *args, **kwargs):
    #     if not self.pk:
    #         # last_id = Add_Category.objects.last().id if Add_Category.objects.exists() else 0
    #         # self.pk = last_id + 1
    #         if Add_Category.objects.exists():
    #             last_id = Add_Category.objects.last().id
    #         else:
    #             last_id = 0
    #         self.pk = last_id + 1
    #     super().save(*args, **kwargs)

    # def delete(self, *args, **kwargs):
    #     current_id = self.id
    #     super().delete(*args, **kwargs)
    #     qs = Add_Category.objects.filter(id__gt=current_id).order_by('id')
    #     for i, obj in enumerate(qs):
    #         obj.id = i + current_id
    #         obj.save()

