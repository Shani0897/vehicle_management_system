# Generated by Django 4.1 on 2023-04-26 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CategoryApp', '0007_alter_add_category_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='add_category',
            name='category_status',
            field=models.CharField(choices=[('Active', 'Active'), ('Inactive', 'Inactive')], default='active', max_length=100),
        ),
    ]
