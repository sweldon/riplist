from django.shortcuts import render

def index(request):

    return render(request, 'rip/rip.html')


def rip(request):

    # return render(request, 'rip/rip.html')
    return render(request, 'rip/home.html')