import datetime
from django.db import models
from django.utils import timezone


# Create your models here.


class Plant_families(models.Model):
    family_name = models.CharField(max_length=200)

    def __str__(self):
        return self.family_name


class Plant_info(models.Model):
    plant_name = models.CharField(max_length=200)
    family_name = models.ForeignKey(Plant_families, on_delete=models.PROTECT, null=True)
    #   plant_family = models.CharField(max_length=200, blank=True, null=True, default="")
    YVR_in_seedDate_start = models.DateField(
        "Earliest indoor seed date", blank=True, null=True
    )
    YVR_in_seedDate_stop = models.DateField(
        "Latest indoor seed date", blank=True, null=True
    )
    YVR_out_seedDate_start = models.DateField(
        "Earliest outdoor seed date", blank=True, null=True
    )
    YVR_out_seedDate_stop = models.DateField(
        "Latest outdoor seed date", blank=True, null=True
    )
    YVR_tpDate_start = models.DateField(
        "Earliest transplant date", blank=True, null=True
    )
    YVR_tpDate_stop = models.DateField("Latest transplant date", blank=True, null=True)
    pub_date = models.DateField("date added to DB")
    plants_per_sqf = models.SmallIntegerField(
        "Plants per square foot", blank=True, null=True
    )

    def __str__(self):
        return self.plant_name

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Seed_inventory(models.Model):
    seed_name = models.CharField(max_length=200)
    seed_source = models.CharField(max_length=200, default="", blank=True)
    seed_link = models.CharField(max_length=1000, default="", blank=True)
    seed_year = models.PositiveSmallIntegerField(default=timezone.now().year)
    pub_date = models.DateField("date added to DB")
    plant_name = models.ForeignKey(Plant_info, on_delete=models.PROTECT)
    rating = models.IntegerField(default=0)

    def __str__(self):
        return self.seed_name
