import datetime
from django.db import models
from django.utils import timezone

# Create your models here.


class Plant_info(models.Model):
    plant_name = models.CharField(max_length=200)
    plant_family = models.CharField(max_length=200, null=True)
    YVR_in_seedDate_start = models.DateTimeField(
        "Earliest indoor seed starting date", null=True
    )
    YVR_in_seedDate_stop = models.DateTimeField(
        "Latest indoor seed starting date", null=True
    )
    YVR_out_seedDate_start = models.DateTimeField(
        "Earliest outdoor seed starting date", null=True
    )
    YVR_out_seedDate_stop = models.DateTimeField(
        "Latest outdoor seed starting date", null=True
    )
    YVR_tpDate_start = models.DateTimeField("Earliest transplant date", null=True)
    YVR_tpDate_stop = models.DateTimeField("Latest transplant date", null=True)
    pub_date = models.DateTimeField("date added to DB")

    def __str__(self):
        return self.plant_name

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Seed_inventory(models.Model):
    seed_name = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date added to DB")
    plant_name = models.ForeignKey(Plant_info, on_delete=models.PROTECT)
    rating = models.IntegerField(default=0)

    def __str__(self):
        return self.seed_name
