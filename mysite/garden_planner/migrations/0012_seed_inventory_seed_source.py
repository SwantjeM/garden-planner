# Generated by Django 4.2.6 on 2023-10-13 15:30

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        (
            "garden_planner",
            "0011_plant_families_remove_plant_info_plant_family_and_more",
        ),
    ]

    operations = [
        migrations.AddField(
            model_name="seed_inventory",
            name="seed_source",
            field=models.CharField(blank=True, default="", max_length=200),
        ),
    ]