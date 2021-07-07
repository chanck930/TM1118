from django.shortcuts import render
from django.http import JsonResponse
from django.core import serializers
from iot.models import Event

# Create your views here.
def index(request):
    return render(request, 'dashboard/index.html')

def temp_data(request):
    events = Event.objects.order_by('-date_created')[:30]
    data = serializers.serialize('json', events) #Translating Django models into JSON formats
    return JsonResponse(data, safe=False) #Returns a string that contains an array object
