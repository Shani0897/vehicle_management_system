# Generated by Django 4.1 on 2023-04-17 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CategoryApp', '0002_alter_add_category_id'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='add_category',
            options={'ordering': ['display_id']},
        ),
        migrations.AddField(
            model_name='add_category',
            name='display_id',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='add_category',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]