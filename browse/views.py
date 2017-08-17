from django.shortcuts import render
from django.http import HttpResponse
import json
from browse.models import *
from django.core.paginator import Paginator
from geopy.geocoders import Nominatim
from geopy.distance import vincenty
from django.views.decorators.csrf import ensure_csrf_cookie
from browse.models import UserProfile
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q

def date_handler(obj):
    return obj.isoformat() if hasattr(obj, 'isoformat') else obj

@ensure_csrf_cookie
def index(request):
    return render(request, 'browse/home.html')

def all_sites(request):
    return render(request, 'browse/summary.html', {'type': 'laydown_yards'})

def all_equipment(request):
    return render(request, 'browse/summary.html', {'type': 'equipment'})

def all_materials(request):
    return render(request, 'browse/summary.html', {'type': 'materials'})

def about(request):
    return render(request, 'base/about.html')


def user_agreement(request):
    return render(request, 'base/user_agreement.html')

def privacy(request):
    return render(request, 'base/privacy.html')

def search_listings(request):
    geolocator = Nominatim()
    results = {}

    search = request.POST.get("search")
    material_search = request.POST.get("materials")
    laydown_search = request.POST.get("laydown_yards" )
    equipment_search = request.POST.get("equipment")
    distance_search = request.POST.get("distance")
    temp_location = request.POST.get("user_location")
    summary = request.POST.get("summary")
    materials_results = {}
    equipment_results = {}
    laydown_results = {}
    markers = []

    #get this via post
    page = 1
    numRecords = 10

    if material_search == "true":

        if summary == "true":

            materials = Material.objects.all().order_by('-id')

        else:

            materials = Material.objects.filter(Q(type__icontains=search) | Q(city__icontains=search)).order_by('-id')


        paginator = Paginator(materials, numRecords)

        try:
            content = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            content = paginator.page(1)
        except EmptyPage:
            # If page is out of range, deliver last page of results.
            content = paginator.page(paginator.num_pages)

        total_pages = paginator.num_pages

        for listing in content:
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
            attrs["images"] = listing.images.split(',')

            geo = geolocator.geocode(listing.address + " "+ listing.state + " "+ listing.zip)
            location = (geo.latitude, geo.longitude)

            #if user is logged in, use geolocator to calculate distance with their address, see line 58: geolocator.geocode(listing.address + " "+ listing.state + " "+ listing.zip)
            # it will be more accurate

            if request.user.is_authenticated():

                address = UserProfile.objects.get(user_id= request.user.id).address
                state = UserProfile.objects.get(user_id= request.user.id).state
                zip = UserProfile.objects.get(user_id= request.user.id).zipcode
                loc = address + " "+ state + " "+ zip
                usergeo = geolocator.geocode(loc)
                if(usergeo is not None):
                    userlocation = (usergeo.latitude, usergeo.longitude)
                    distance_to = vincenty(location, userlocation).miles
                    print "USER LOGGED IN: "+str(distance_to)
                else:
                    distance_to = vincenty(location, temp_location).miles
                    print "USER LOGGED IN BUT LOCATION AMBIGUOUS: " + str(distance_to)

            else:

                distance_to = vincenty(location, temp_location).miles
                print "ANONYMOUS USER: " + str(distance_to)

            materials_results[listing.id] = attrs

            if distance_search is None:
                attrs["distance"] = round(distance_to, 2)

            elif(distance_search != 'Any'):
                if (int(distance_to) <= int(distance_search)):
                    attrs["distance"] = round(distance_to,2)
                    markers.append([geo.latitude, geo.longitude])
            else:
                attrs["distance"] = round(distance_to,2)
                markers.append([geo.latitude, geo.longitude])


    elif(laydown_search == "true"):

        if summary == "true":

            laydown = Site.objects.all().order_by('-id')

        else:

            laydown = Site.objects.filter(Q(surface__icontains=search) | Q(city__icontains=search)).order_by('-id')


        paginator = Paginator(laydown, numRecords)

        try:
            content = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            content = paginator.page(1)
        except EmptyPage:
            # If page is out of range, deliver last page of results.
            content = paginator.page(paginator.num_pages)

        total_pages = paginator.num_pages

        for listing in content:
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

            geo = geolocator.geocode(listing.address + " "+ listing.state + " "+ listing.zip)
            location = (geo.latitude, geo.longitude)

            #if user is logged in, use geolocator to calculate distance with their address, see line 58: geolocator.geocode(listing.address + " "+ listing.state + " "+ listing.zip)
            # it will be more accurate

            if request.user.is_authenticated():

                address = UserProfile.objects.get(user_id= request.user.id).address
                state = UserProfile.objects.get(user_id= request.user.id).state
                zip = UserProfile.objects.get(user_id= request.user.id).zipcode
                loc = address + " "+ state + " "+ zip
                usergeo = geolocator.geocode(loc)
                if(usergeo is not None):
                    userlocation = (usergeo.latitude, usergeo.longitude)
                    distance_to = vincenty(location, userlocation).miles
                    print "USER LOGGED IN: "+str(distance_to)
                else:
                    distance_to = vincenty(location, temp_location).miles
                    print "USER LOGGED IN BUT LOCATION AMBIGUOUS: " + str(distance_to)

            else:

                distance_to = vincenty(location, temp_location).miles
                print "ANONYMOUS USER: " + str(distance_to)

            laydown_results[listing.id] = attrs

            if distance_search is None:
                attrs["distance"] = round(distance_to, 2)

            elif(distance_search != 'Any'):
                if (int(distance_to) <= int(distance_search)):
                    attrs["distance"] = round(distance_to,2)
                    markers.append([geo.latitude, geo.longitude])
            else:
                attrs["distance"] = round(distance_to,2)
                markers.append([geo.latitude, geo.longitude])

    elif(equipment_search == 'true'):

        if summary == "true":

            equipment = Equipment.objects.all().order_by('-id')

        else:

            equipment = Equipment.objects.filter(Q(make__icontains=search) | Q(city__icontains=search)).order_by('-id')


        paginator = Paginator(equipment, numRecords)

        try:
            content = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            content = paginator.page(1)
        except EmptyPage:
            # If page is out of range, deliver last page of results.
            content = paginator.page(paginator.num_pages)

        total_pages = paginator.num_pages

        for listing in content:
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

            geo = geolocator.geocode(listing.address + " "+ listing.state + " "+ listing.zip)
            location = (geo.latitude, geo.longitude)

            #if user is logged in, use geolocator to calculate distance with their address, see line 58: geolocator.geocode(listing.address + " "+ listing.state + " "+ listing.zip)
            # it will be more accurate

            if request.user.is_authenticated():

                address = UserProfile.objects.get(user_id= request.user.id).address
                state = UserProfile.objects.get(user_id= request.user.id).state
                zip = UserProfile.objects.get(user_id= request.user.id).zipcode
                loc = address + " "+ state + " "+ zip
                usergeo = geolocator.geocode(loc)
                if(usergeo is not None):
                    userlocation = (usergeo.latitude, usergeo.longitude)
                    distance_to = vincenty(location, userlocation).miles
                    print "USER LOGGED IN: "+str(distance_to)
                else:
                    distance_to = vincenty(location, temp_location).miles
                    print "USER LOGGED IN BUT LOCATION AMBIGUOUS: " + str(distance_to)

            else:

                distance_to = vincenty(location, temp_location).miles
                print "ANONYMOUS USER: " + str(distance_to)

            equipment_results[listing.id] = attrs

            if distance_search is None:
                attrs["distance"] = round(distance_to, 2)

            elif(distance_search != 'Any'):
                if (int(distance_to) <= int(distance_search)):
                    attrs["distance"] = round(distance_to,2)
                    markers.append([geo.latitude, geo.longitude])
            else:
                attrs["distance"] = round(distance_to,2)
                markers.append([geo.latitude, geo.longitude])


    data = {"materials_results":materials_results, "equipment_results":equipment_results, "laydown_results":laydown_results, "markers":markers, "total_pages":get_pages(total_pages)}
    data = json.dumps(data)
    return HttpResponse(data)

def error404(request):
    return render(request,'browse/404.html')

def error500(request):
    return render(request, 'browse/500.html')

def get_pages(total_pages):
    html = "<a id='previous_page'>&laquo;</a> ";
    pageList = range(1, total_pages+1)

    for page in pageList:
        html += "<a class='page_number'>" + str(page) + "</a> "

    html += " <a id='next_page'>&raquo;</a>";
    return html


def get_address(request):
    user = request.user.id
    user_info = UserProfile.objects.get(user_id=user)
    (street, zipcode, state) = [str(user_info.address), str(user_info.zipcode), str(user_info.state)]
    geolocator = Nominatim()

    success = True
    location = [0, 0]

    if request.POST.get("custom_address") is not None:

        try:
            geo = geolocator.geocode(request.POST.get("custom_address"))
            location = [geo.latitude, geo.longitude]
        except AttributeError:
            success = False



    else:
        geo = geolocator.geocode(street + " " + state + " " + zipcode)
        location = [geo.latitude, geo.longitude]

    rdata = {"street":street, "zipcode":zipcode, "state":state, "lat":location[0], "lng":location[1], "success":success}
    rdata = json.dumps(rdata)
    return HttpResponse(rdata)

def materials(request):

    listing_id = request.GET.get("id")
    listing = Material.objects.get(id=listing_id)
    type = listing.type
    volume = listing.volume
    rate = listing.rate
    title = str(type) + " - " + str(volume) + " " + str(rate)
    images = [str(image) for image in listing.images.split(',')]
    price = str(listing.price) + " / " + str(rate)
    address = str(listing.address) + ", " + str(listing.city) + ", " + str(listing.state) + ", " + str(listing.zip)
    loading = str(listing.load_price)
    haul_price = str(listing.haul_price)
    haul_distance = str(listing.haul_distance)
    date_available = str(listing.date_available)
    date_expiration = str(listing.expiration_date)
    comments = str(listing.comments)
    seller = str(User.objects.get(id=int(listing.author)).username)



    return render(request, 'browse/listing.html',  {'title': title,
                                                    'images':images,
                                                    'price':price,
                                                    'address':address,
                                                    'loading':loading,
                                                    'haul_price':haul_price,
                                                    'haul_distance':haul_distance,
                                                    'date_available':date_available,
                                                    'date_expiration':date_expiration,
                                                    'comments':comments,
                                                    'seller':seller})

def equipment(request):

    listing_id = request.GET.get("id")
    listing = Equipment.objects.get(id=listing_id)
    type = listing.type
    address = str(listing.address) + ", " + str(listing.city) + ", " + str(listing.state) + ", " + str(listing.zip)
    make = str(listing.make)
    model = str(listing.model)
    year = str(listing.year)
    attachments = str(listing.attachments)
    hauling = str(listing.hauling_options)
    trailer = str(listing.trailer)
    operator = str(listing.operator)
    fuel = str(listing.fuel)
    date_available = str(listing.date_available)
    expiration_date = str(listing.expiration_date)
    date_needed = str(listing.date_needed)
    rate = str(listing.rate)
    price = str(listing.price) + " / " + str(rate)
    comments = str(listing.comments)
    seller = str(User.objects.get(id=int(listing.author)).username)
    title = str(year) + " " + str(make) + " " + str(model) + " " + str(type)
    images = [str(image) for image in listing.images.split(',')]



    return render(request, 'browse/listing_equipment.html',  {  'title': title,
                                                                'images':images,
                                                                'price':price,
                                                                'address':address,
                                                                'date_available':date_available,
                                                                'comments':comments,
                                                                'seller':seller,
                                                                'year':year,
                                                                'attachments':attachments,
                                                                'hauling':hauling,
                                                                'trailer':trailer,
                                                                'operator':operator,
                                                                'fuel':fuel,
                                                                'date_expiration':expiration_date,
                                                                'date_needed':date_needed,
                                                                'rate':rate
                                                              })

def sites(request):

    listing_id = request.GET.get("id")
    listing = Site.objects.get(id=listing_id)
    address = str(listing.address) + ", " + str(listing.city) + ", " + str(listing.state) + ", " + str(listing.zip)
    surface = str(listing.surface)
    fenced = str(listing.fenced)
    size = str(listing.size)
    gated = str(listing.gated)
    num_entrances = str(listing.num_entrances)
    width_entrances = str(listing.width_entrances)
    utilities = str(listing.utilities)
    ammenities = str(listing.ammenities)
    date_available = str(listing.date_available)
    expiration_date = str(listing.expiration_date)
    rate = str(listing.rate)
    price = str(listing.price) + " / " + str(rate)
    comments = str(listing.comments)
    seller = str(User.objects.get(id=int(listing.author)).username)
    title = str(size) + " " + str(surface) + " - " + str(listing.city) + ",  " + str(listing.state)
    images = [str(image) for image in listing.images.split(',')]



    return render(request, 'browse/listing_site.html',  {  'title': title,
                                                                'images':images,
                                                                'price':price,
                                                                'address':address,
                                                                'date_available':date_available,
                                                                'comments':comments,
                                                                'seller':seller,
                                                                'date_expiration':expiration_date,
                                                                'rate':rate,
                                                                'surface':surface,
                                                                'fenced':fenced,
                                                                'size':size,
                                                                'gated':gated,
                                                                'num_entrances':num_entrances,
                                                                'width_entrances':width_entrances,
                                                                'utilities':utilities,
                                                                'ammenities':ammenities
                                                              })