from django.shortcuts import render
from django.http import HttpResponse
import json
from rip.models import *

def index(request):

    return render(request, 'rip/rip.html')


def rip(request):

    # return render(request, 'rip/rip.html')
    return render(request, 'rip/home.html')

def searchLocation(request):
    term = request.GET.get('term') #jquery-ui.autocomplete parameter
    cities = Locations.objects.filter(name__istartswith=term) #lookup for a city
    res = []
    for c in cities:
         #make dict with the metadatas that jquery-ui.autocomple needs (the documentation is your friend)
         # dict = {'id':c.id, 'label':c.__unicode__(), 'value':c.__unicode__()}
         # res.append(dict)
        res.append(c.name)
        res = list(set(res))
    return HttpResponse(json.dumps(res))