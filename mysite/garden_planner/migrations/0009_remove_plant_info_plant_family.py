# Generated by Django 4.2.6 on 2023-10-12 23:03

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("garden_planner", "0008_alter_plant_info_plant_family"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="plant_info",
            name="plant_family",
        ),
    ]