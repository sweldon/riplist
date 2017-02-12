from django.shortcuts import render
from django.views.decorators.csrf import ensure_csrf_cookie


@ensure_csrf_cookie
def create_listing(request):
    if request.POST:

        return render(request,'browse/home.html')

    else:

        return render(request, 'browse/home.html')
