from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.contrib.auth import authenticate
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth import login
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.shortcuts import render


def login_page(request):

    username = password = ''
    failure = False

    if request.user.is_authenticated():

        return redirect('/browse')

    else:

        if request.POST:
            username = request.POST['username']
            password = request.POST['password']

            user = authenticate(username=username, password=password)

            if user is not None:
                if user.is_active:
                    login(request, user)

                    return redirect('/browse')
            else:

                print 'bad login'
                failure = True

                return render(request, 'login/login.html', {'error': failure})
        else:
            return render(request, 'login/login.html', status=200)

def logout_page(request):
    logout(request)
    # return render_to_response("login/login.html")
    return redirect('/login')

def register(request):

    if request.POST:
        username = request.POST['username']
        password = request.POST['password']

        user = User.objects.filter(username=username)

        if(len(user) < 1):

            newuser = User.objects.create_user(username=username, password=password)

            login(request, newuser)

            # Redirect to a success page.
            return redirect('/browse')

        else:

            print 'user already exists'
            failure = True

            return render(request, 'login/register.html', {'error': failure})
    else:
        return render(request, 'login/register.html', status=200)
