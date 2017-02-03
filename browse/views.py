from django.shortcuts import render
from django.http import HttpResponse
import json
from browse.models import *
from django.core.paginator import Paginator

def date_handler(obj):
    return obj.isoformat() if hasattr(obj, 'isoformat') else obj

def index(request):

    return render(request, 'browse/home.html')


def search_listings(request):

    results = {}

    search = request.POST.get("search")
    material_search = request.POST.get("materials")
    laydown_search = request.POST.get("laydown_yards")
    equipment_search = request.POST.get("equipment")
    distance_search = request.POST.get("distance")

    # depending on above flags, search appropriate models
    materials = Material.objects.filter(type__icontains=search)[:4]
    equipment = Equipment.objects.filter(model__icontains=search)[:4]
    laydown = Site.objects.filter(surface__icontains=search)


    materials_results = {}
    equipment_results = {}
    laydown_results = {}

    if(material_search):
        for listing in materials:
            attrs = {}
            materials_results[listing.id] = attrs
            attrs["listing_type"]= listing.listing_type
            attrs["address"] = listing.address
            attrs["city"] = listing.city
            attrs["state"] = listing.state
            attrs["zip"] = listing.zip
            attrs["type"] = listing.type
            attrs["volume"] = str(listing.volume)
            attrs["price"] = str(listing.price)
            attrs["date_available"] = date_handler(listing.date_available)
            attrs["expiration_date"] = date_handler(listing.expiration_date)
            attrs["load_price"] = str(listing.load_price)
            attrs["haul_distance"] = str(listing.haul_distance)
            attrs["haul_price"] = str(listing.haul_price)
            attrs["media_dir"] = listing.media_dir
            attrs["notifications"] = listing.notifications
            attrs["comments"] = listing.comments

    if(laydown_search):
        for listing in laydown:
            attrs = {}
            laydown_results[int(listing.id)] = attrs
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
            attrs["comments"] = listing.comments


    if(equipment_search):
        pass

    data = {"materials_results":materials_results, "equipment_results":equipment_results, "laydown_results":laydown_results}
    data = json.dumps(data)
    return HttpResponse(data)

def error404(request):
    return render(request,'browse/404.html')

def error500(request):
    return render(request, 'browse/500.html')