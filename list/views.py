from django.shortcuts import render
from django.http import HttpResponse
import json
from browse.models import *
from geopy.geocoders import Nominatim
from geopy.distance import vincenty
from django.views.decorators.csrf import ensure_csrf_cookie


@ensure_csrf_cookie
def create_listing(request):
    if request.POST:

        return render(request,'browse/home.html')

    else:

        return render(request, 'browse/home.html')
