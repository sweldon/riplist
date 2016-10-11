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

    if request.user.is_authenticated():

        return redirect('/rip')

    else:

        if request.POST:
            username = request.POST['username']
            password = request.POST['password']

            user = authenticate(username=username, password=password)

            if user is not None:
                if user.is_active:
                    login(request, user)
                    # if (len(user.groups.all()) == 0):
                    #
                    #     return render(request, 'login/request.html', {'request_user': user})
                    # else:
                    #     login(request, user)

                    # Redirect to a success page.
                    return redirect('/rip')
            else:

                print 'bad login'
                failure = True

                return redirect('/login')
        else:
            return render(request, 'login/login.html', status=200)

def logout_page(request):
    logout(request)
    # return render_to_response("login/login.html")
    return redirect('/login')