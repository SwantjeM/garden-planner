from django.contrib import admin

# Register your models here.
from .models import Plant_info, Seed_inventory, Plant_families


class Plant_infoAdmin(admin.ModelAdmin):
    list_display = ("plant_name", "family_name", "plants_per_sqf")


class Seed_inventoryAdmin(admin.ModelAdmin):
    list_display = ("seed_name", "plant_name", "seed_source", "seed_year")


# admin.site.register(Plant_info)
admin.site.register(Plant_info, Plant_infoAdmin)
admin.site.register(Seed_inventory, Seed_inventoryAdmin)
admin.site.register(Plant_families)
