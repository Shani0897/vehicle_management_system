# Generated by Django 4.1 on 2023-05-01 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('VManageIn_App', '0002_remove_vehiclein_vehicle_out_time_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehiclein',
            name='parking_charges',
            field=models.IntegerField(null=True),
        ),
    ]