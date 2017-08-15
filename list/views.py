from django.shortcuts import render
from django.http import HttpResponse
import json
from browse.models import *
from geopy.geocoders import Nominatim
from geopy.distance import vincenty
from django.views.decorators.csrf import ensure_csrf_cookie
from django.core.files.storage import FileSystemStorage
from browse.models import UserProfile
import uuid
import os
from django.shortcuts import redirect

def get_file_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return os.path.join('materials/', filename)

def format_datepicker(date):
    return date[6:] + '-' + date[0:2] + '-' + date[3:5]

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

    else:

        return render(request, 'browse/home.html')


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

        address = request.POST.get("address_dropdown")
        type = request.POST.get("type")
        buysell = request.POST.get("buysell")

        if address == "account":
            user = request.user.id
            user_info = UserProfile.objects.get(user_id=user)
            (street, zipcode, state, city) = [str(user_info.address), str(user_info.zipcode), str(user_info.state), str(user_info.city)]

        elif address == "other":
            street = request.POST.get("custom_street")
            zipcode = request.POST.get("custom_zip")
            state = request.POST.get("custom_state")
            city = request.POST.get("custom_city")

        type_material = request.POST.get("type_dropdown")

        if type_material == "other":

            type_material = request.POST.get("custom_material")

        amount_material = request.POST.get("material_amount")
        price_material = request.POST.get("material_price")
        date_available = format_datepicker(request.POST.get("datepicker_available"))
        date_expiration = format_datepicker(request.POST.get("datepicker_expiration"))
        hauling = request.POST.get("hauling_dropdown")
        hauling_price = request.POST.get("hauling_price")
        hauling_distance = request.POST.get("hauling_distance_dropdown")
        loading = request.POST.get("loading_dropdown")
        loading_price = request.POST.get("loading_price")
        comments = request.POST.get("comments")

        files =  request.FILES.getlist('image_file_arr')
        filelist = []
        for afile in request.FILES.getlist('image_file_arr'):
            fs = FileSystemStorage()
            # filename = fs.save(afile.name, afile)
            filename = fs.save(get_file_path(afile, afile.name), afile)
            uploaded_file_url = fs.url(filename)
            filelist.append(str(filename))
            print 'Uploaded file: ', uploaded_file_url

        new_material = Material(
            listing_type = 'sell',
            address = street,
            city = city,
            state = state,
            zip = zipcode,
            rate = "cu yd",
            type = type_material,
            volume = amount_material,
            price = price_material,
            date_available = date_available,
            expiration_date = date_expiration,
            load_price = loading_price,
            haul_distance = hauling_distance,
            haul_price = hauling_price,
            media_dir = "test",
            notifications = "",
            comments = comments,
            author = request.user.id,
            images = ','.join(filelist))

        new_material.save()

        return redirect('/browse/materials/?id='+str(new_material.id))

    else:


        return render(request, 'browse/404.html')

def upload_image():

    if request.POST:
        print request.FILES.getlist('image_file_arr')
        for afile in request.FILES.getlist('image_file_arr'):
            fs = FileSystemStorage()
            filename = fs.save(afile.name, afile)
            uploaded_file_url = fs.url(filename)
            print uploaded_file_url
        return render(request, 'browse/404.html')
    else:
        print 'Error saving file.'