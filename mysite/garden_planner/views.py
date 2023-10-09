from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hello World. You're at the garden-planner index.")

def detail(request, plant_info_id):
    return HttpResponse("you're looking at plant variety %s" % plant_info_id)

def varieties(request, plant_info_id):
    response = "You're looking at all varieties in your seed inventory that match plant type %s."
    return HttpResponse (response % plant_info_id)

def vote(request, plant_info_id):
    return HttpResponse("you're voting on plant_info %s." % plant_info_id)
