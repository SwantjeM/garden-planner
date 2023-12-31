# Generated by Django 4.2.6 on 2023-10-16 17:57

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("garden_planner", "0015_plant_info_plants_per_sqf"),
    ]

    operations = [
        migrations.AddField(
            model_name="seed_inventory",
            name="height_cm",
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="seed_inventory",
            name="seed_notes",
            field=models.TextField(blank=True, default=""),
        ),
        migrations.AddField(
            model_name="seed_inventory",
            name="size_type",
            field=models.CharField(blank=True, default="", max_length=200),
        ),
        migrations.AddField(
            model_name="seed_inventory",
            name="width_cm",
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
    ]
