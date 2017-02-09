from django.shortcuts import render
from django.http import HttpResponse
import json
from browse.models import *
from django.core.paginator import Paginator
from geopy.geocoders import Nominatim
from geopy.distance import vincenty
from django.views.decorators.csrf import ensure_csrf_cookie



def date_handler(obj):
    return obj.isoformat() if hasattr(obj, 'isoformat') else obj

@ensure_csrf_cookie
def index(request):

    return render(request, 'browse/home.html')

def search_listings(request):

    geolocator = Nominatim()

    results = {}

    search = request.POST.get("search")
    material_search = request.POST.get("materials")
    laydown_search = request.POST.get("laydown_yards" )
    equipment_search = request.POST.get("equipment")
    distance_search = request.POST.get("distance")
    temp_location = request.POST.get("user_location")
    # depending on above flags, search appropriate models

    materials_results = {}
    equipment_results = {}
    laydown_results = {}

    markers = []

    if(material_search == "true"):

        materials = Material.objects.filter(type__icontains=search)
        for listing in materials:
            attrs = {}
            attrs["id"] = listing.id
            attrs["listing_type"]= listing.listing_type
            attrs["address"] = listing.address
            attrs["city"] = listing.city
            attrs["state"] = listing.state
            attrs["zip"] = listing.zip
            attrs["type"] = listing.type
            attrs["volume"] = str(listing.volume)
            attrs["price"] = str(listing.price)
            attrs["rate"] = listing.rate
            attrs["date_available"] = date_handler(listing.date_available)
            attrs["expiration_date"] = date_handler(listing.expiration_date)
            attrs["load_price"] = str(listing.load_price)
            attrs["haul_distance"] = str(listing.haul_distance)
            attrs["haul_price"] = str(listing.haul_price)
            attrs["media_dir"] = listing.media_dir
            attrs["notifications"] = listing.notifications
            attrs["comments"] = listing.comments

            geo = geolocator.geocode(listing.address + " "+ listing.state + " "+ listing.zip)
            location = (geo.latitude, geo.longitude)

            #if user is logged in, use geolocator to calculate distance with their address, see line 58: geolocator.geocode(listing.address + " "+ listing.state + " "+ listing.zip)
            # it will be more accurate
            distance_to = vincenty(location, temp_location).miles

            if(distance_search != 'Any'):

                if (int(distance_to) <= int(distance_search)):
                    materials_results[listing.id] = attrs
                    attrs["distance"] = round(distance_to,2)
                    markers.append([geo.latitude, geo.longitude])
            else:
                materials_results[listing.id] = attrs
                attrs["distance"] = round(distance_to,2)
                markers.append([geo.latitude, geo.longitude])


    elif(laydown_search == "true"):

        laydown = Site.objects.filter(surface__icontains=search)
        for listing in laydown:
            attrs = {}
            attrs["id"] = listing.id
            attrs["listing_type"]= listing.listing_type
            attrs["address"] = listing.address
            attrs["city"] = listing.city
            attrs["state"] = listing.state
            attrs["zip"] = listing.zip
            attrs["size"] = listing.size
            attrs["surface"] = listing.surface
            attrs["fenced"] = listing.fenced
            attrs["gated"] = listing.gated
            attrs["num_entrances"] = listing.num_entrances
            attrs["width_entrances"] = listing.width_entrances
            attrs["utilities"] = listing.utilities
            attrs["ammenities"] = listing.ammenities
            attrs["date_available"] = date_handler(listing.date_available)
            attrs["expiration_date"] = date_handler(listing.expiration_date)
            attrs["price"] = str(listing.price)
            attrs["rate"] = listing.rate
            attrs["comments"] = listing.comments

            geo = geolocator.geocode(listing.address + " " + listing.state + " " + listing.zip)
            location = (geo.latitude, geo.longitude)

            distance_to = vincenty(location, temp_location).miles

            if (distance_search != 'Any'):

                if (int(distance_to) <= int(distance_search)):
                    laydown_results[listing.id] = attrs
                    attrs["distance"] = round(distance_to, 2)
                    markers.append([geo.latitude, geo.longitude])
            else:
                laydown_results[listing.id] = attrs
                attrs["distance"] = round(distance_to, 2)
                markers.append([geo.latitude, geo.longitude])


    elif(equipment_search == 'true'):

        equipment = Equipment.objects.filter(make__icontains=search)
        for listing in equipment:
            attrs = {}
            attrs["id"] = listing.id
            attrs["listing_type"] = listing.listing_type
            attrs["address"] = listing.address
            attrs["city"] = listing.city
            attrs["state"] = listing.state
            attrs["zip"] = listing.zip
            attrs["type"] = listing.type
            attrs["make"] = listing.make
            attrs["model"] = listing.model
            attrs["year"] = listing.year
            attrs["attachments"] = listing.attachments
            attrs["hauling_options"] = listing.hauling_options
            attrs["trailer"] = listing.trailer
            attrs["operator"] = listing.operator
            attrs["fuel"] = listing.fuel
            attrs["date_available"] = date_handler(listing.date_available)
            attrs["expiration_date"] = date_handler(listing.expiration_date)
            attrs["date_needed"] =  date_handler(listing.date_needed)
            attrs["price"] = str(listing.price)
            attrs["rate"] = listing.rate
            attrs["comments"] = listing.comments

            geo = geolocator.geocode(listing.address + " " + listing.state + " " + listing.zip)
            location = (geo.latitude, geo.longitude)

            distance_to = vincenty(location, temp_location).miles

            if (distance_search != 'Any'):

                if (int(distance_to) <= int(distance_search)):
                    equipment_results[listing.id] = attrs
                    attrs["distance"] = round(distance_to, 2)
                    markers.append([geo.latitude, geo.longitude])
            else:
                equipment_results[listing.id] = attrs
                attrs["distance"] = round(distance_to, 2)
                markers.append([geo.latitude, geo.longitude])

    data = {"materials_results":materials_results, "equipment_results":equipment_results, "laydown_results":laydown_results, "markers":markers}
    data = json.dumps(data)
    return HttpResponse(data)

def error404(request):
    return render(request,'browse/404.html')

def error500(request):
    return render(request, 'browse/500.html')