# Generated by Django 4.1 on 2023-04-18 22:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CategoryApp', '0006_alter_add_category_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='add_category',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
