from django.contrib.auth import authenticate
from django.contrib.auth import (
    get_user_model, )
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth.forms import (
    SetPasswordForm,
)
from django.contrib.auth.models import User
from django.contrib.auth.tokens import default_token_generator
from django.core.exceptions import ValidationError
from django.core.mail import send_mail
from django.core.validators import validate_email
from django.db.models.query_utils import Q
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.shortcuts import render
from django.shortcuts import resolve_url
from django.template import loader
from django.template.response import TemplateResponse
from django.urls import reverse
from django.utils.encoding import force_bytes
from django.utils.encoding import force_text
from django.utils.http import urlsafe_base64_decode
from django.utils.http import urlsafe_base64_encode
from django.utils.translation import gettext_lazy as _

from ewdatabase.models import UserProfile
from plapp.settings import DEFAULT_FROM_EMAIL

UserModel = get_user_model()

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
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        address = request.POST['address']
        zipcode = request.POST['zipcode']
        state = request.POST['state']
        phone = str(request.POST['phone1']) + str(request.POST['phone2']) + str(request.POST['phone3'])
        business_name = request.POST['business_name']

        user = User.objects.filter(Q(username=username) | Q(email=email))

        if(len(user) < 1):

            newuser = User.objects.create_user(
                username=username,
                password=password,
                first_name=firstname,
                last_name=lastname,
                email=email,
            )

            # newaccount = User.objects.get(username=username)

            userprofile = UserProfile(
                user_id = newuser.id,
                address=address,
                zipcode=zipcode,
                state=state,
                phone=phone,
                business=business_name
            )

            userprofile.save()

            login(request, newuser)

            # Redirect to a success page.
            return redirect('/browse')

        else:

            print 'user already exists'
            failure = True

            return render(request, 'login/register.html', {'error': failure})
    else:
        return render(request, 'login/register.html', status=200)



def validate_email_address(email):

    try:
        validate_email(email)
        return True
    except ValidationError:
        return False

def recover(request):

    if request.POST:

        success = False
        email = request.POST['email']

        if(validate_email_address(email) == True):

            associated_users= User.objects.filter(Q(email=email))
            if associated_users.exists():
                for user in associated_users:
                        c = {
                            'email': user.email,
                            'domain': request.META['HTTP_HOST'],
                            'site_name': 'Earthworkx',
                            'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                            'user': user,
                            'token': default_token_generator.make_token(user),
                            'protocol': 'http',
                            }
                        subject_template_name='login/passwordresetsubject.txt'
                        # copied from django/contrib/admin/templates/registration/password_reset_subject.txt to templates directory
                        email_template_name='login/passwordresetemail.html'
                        # copied from django/contrib/admin/templates/registration/password_reset_email.html to templates directory
                        subject = loader.render_to_string(subject_template_name, c)
                        # Email subject *must not* contain newlines
                        subject = ''.join(subject.splitlines())
                        email = loader.render_to_string(email_template_name, c)
                        send_mail(subject, email, DEFAULT_FROM_EMAIL , [user.email], fail_silently=False)

                success = True
                print(request, 'An email has been sent to ' + email +". Please check its inbox to continue reseting password.")


            print(request, 'No user is associated with this email address')


        return render(request, 'login/recover.html', {'success': success})


    else:
        return render(request, 'login/recover.html', status=200)


def passwordresetpage(request, uidb64=None, token=None,
                           template_name='login/passwordresetpage.html',
                           token_generator=default_token_generator,
                           set_password_form=SetPasswordForm,
                           post_reset_redirect=None,
                           extra_context=None):

    assert uidb64 is not None and token is not None  # checked by URLconf
    if post_reset_redirect is None:
        post_reset_redirect = reverse('password_reset_complete')
    else:
        post_reset_redirect = resolve_url(post_reset_redirect)
    try:
        # urlsafe_base64_decode() decodes to bytestring
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = UserModel._default_manager.get(pk=uid)
    except (TypeError, ValueError, OverflowError, UserModel.DoesNotExist):
        user = None

    if user is not None and token_generator.check_token(user, token):
        validlink = True
        title = _('Enter new password')
        if request.method == 'POST':
            form = set_password_form(user, request.POST)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect(post_reset_redirect)
        else:
            form = set_password_form(user)
    else:
        validlink = False
        form = None
        title = _('Password reset unsuccessful')
    context = {
        'form': form,
        'title': title,
        'validlink': validlink,
    }
    if extra_context is not None:
        context.update(extra_context)

    return TemplateResponse(request, template_name, context)

def password_reset_complete(request):

    return render(request, 'login/passwordresetcomplete.html', status=200)

