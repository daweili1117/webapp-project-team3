#from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404,HttpResponseRedirect
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_text
from django.contrib.auth import login, authenticate
from .forms import SignUpForm
from .models import *
from .forms import *
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.utils.http import urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode

from django.template.loader import render_to_string



def home(request):
   return render(request, 'indianexpress/home.html',
                 {'indianexpress': home})

def activation_sent_view(request):
    return render(request, 'activation_sent.html')


def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    # checking if the user exists, if the token is valid.
    if user is not None and account_activation_token.check_token(user, token):
        # if valid set active true
        user.is_active = True
        # set signup_confirmation true
        user.profile.signup_confirmation = True
        user.save()
        login(request, user)
        return redirect('home')
    else:
        return render(request, 'activation_invalid.html')


def signup(request):
    form = SignUpForm(request.POST)
    if form.is_valid():
        user = form.save()
        user.refresh_from_db()
        user.profile.first_name = form.cleaned_data.get('first_name')
        user.profile.last_name = form.cleaned_data.get('last_name')
        #user.profile.phone_number = form.cleaned_data.get('phone_number')
        user.profile.zip_code = form.cleaned_data.get('zip_code')
        user.profile.email = form.cleaned_data.get('email')
        user.is_active = False
        user.save()
        current_site = get_current_site(request)
        subject = 'Please Activate Your Account'
        # load a template like get_template()
        # and calls its render() method immediately.
        message = render_to_string('indianexpress/activation_request.html', {
            'user': user,
            'domain': current_site.domain,
            'uid': urlsafe_base64_encode(force_bytes(user.pk)),
            # method will generate a hash value with user related data
            'token': account_activation_token.make_token(user),
        })
        user.email_user(subject, message)
        return redirect('activation_sent')

    else:
        form = SignUpForm()
    return render(request, 'indianexpress/signup.html', {'form': form})


def reservation(request):
    return render(request, 'indianexpress/reservation.html', {'indianexpress': reservation})


def menu(request):
    return render(request, 'indianexpress/menu.html', {'indianexpress': menu})


def cart(request):
    return render(request, 'indianexpress/cart.html', {'indianexpress': cart})

def gallery(request):
    return render(request, 'indianexpress/gallery.html', {'indianexpress': gallery})