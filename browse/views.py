from django.shortcuts import render
from django.http import HttpResponse
import json
from browse.models import *

def index(request):

    return render(request, 'browse/home.html')


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

def error404(request):
    return render(request,'browse/404.html')

def error500(request):
    return render(request, 'browse/500.html')