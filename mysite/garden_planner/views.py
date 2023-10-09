from django.shortcuts import render
from django.http import HttpResponse

from .models import Plant_info

# Create your views here.
def index(request):
    latest_plants_list = Plant_info.objects.order_by("-pub_date")[:5]
    output = ", ".join([t.plant_type for t in latest_plants_list])
    return HttpResponse(output)

def detail(request, plant_info_id):
    return HttpResponse("you're looking at plant variety %s" % plant_info_id)

def varieties(request, plant_info_id):
    response = "You're looking at all varieties in your seed inventory that match plant type %s."
    return HttpResponse (response % plant_info_id)

def vote(request, plant_info_id):
    return HttpResponse("you're voting on plant_info %s." % plant_info_id)
