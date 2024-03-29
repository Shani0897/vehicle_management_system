# Generated by Django 4.1 on 2023-04-11 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Add_Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=200)),
                ('parking_charges_per_hour', models.IntegerField()),
                ('category_status', models.CharField(choices=[('active', 'Active'), ('inactive', 'Inactive')], default='active', max_length=100)),
            ],
        ),
    ]
