from django.shortcuts import render
from django.http import HttpResponse
import json
from browse.models import *
from geopy.geocoders import Nominatim
from geopy.distance import vincenty
from django.views.decorators.csrf import ensure_csrf_cookie



def create_listing(request):

    if request.POST:

        create_type = request.POST.get("listing_dropdown")
        listing_type = request.POST.get("buytype")


        if(create_type=="material"):

            if(listing_type=='sell'):

                return render(request, 'list/material_sell.html')

            elif (listing_type == 'buy'):

                return render(request, 'list/comingsoon.html')
                # return render(request, 'list/material_buy.html')

        else:

            return render(request, 'list/comingsoon.html')

        # if (create_type == "equipment"):
        #
        #     if (listing_type == 'buy'):
        #
        #         return render(request, 'list/equipment_buy.html')
        #
        #
        #     elif (listing_type == 'sell'):
        #
        #         return render(request, 'list/equipment_sell.html')
        #
        # if (create_type == "laydown"):
        #
        #     if (listing_type == 'buy'):
        #
        #         return render(request, 'list/laydown_buy.html')
        #
        #     elif (listing_type == 'sell'):
        #
        #         return render(request, 'list/laydown_sell.html')


def submit_listing(request):

    if request.POST:

        create_type = request.POST.get("listing_dropdown")

    return render(request, 'browse/404.html')
