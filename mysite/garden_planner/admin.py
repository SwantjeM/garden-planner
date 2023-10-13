from django.contrib import admin

# Register your models here.
from .models import Plant_info, Seed_inventory


class Plant_infoAdmin(admin.ModelAdmin):
    list_display = ("plant_name", "family_name")


# admin.site.register(Plant_info)
admin.site.register(Plant_info, Plant_infoAdmin)
admin.site.register(Seed_inventory)
