# Generated by Django 4.2.6 on 2023-10-12 23:10

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("garden_planner", "0009_remove_plant_info_plant_family"),
    ]

    operations = [
        migrations.AddField(
            model_name="plant_info",
            name="plant_family",
            field=models.CharField(blank=True, default="", max_length=200, null=True),
        ),
    ]
