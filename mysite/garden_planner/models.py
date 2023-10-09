import datetime
from django.db import models
from django.utils import timezone

# Create your models here.

class Plant_info(models.Model):
    plant_type = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date added to DB")
    def __str__(self):
        return self.plant_type
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Seed_inventory(models.Model):
    seed_name = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date added to DB")
    plant_type = models.ForeignKey(Plant_info, on_delete=models.PROTECT)
    rating = models.IntegerField(default=0)
    def __str__(self):
        return self.seed_name


