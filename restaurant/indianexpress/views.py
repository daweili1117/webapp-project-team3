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
from django.core.mail import send_mail
from django.http import HttpResponse




def home(request):
   return render(request, 'indianexpress/home.html',
                 {'indianexpress': home})


def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'indianexpress/signup.html', {'form': form})

def reservation(request):
    if request.method == 'POST':
        a = request.POST['name']
        b = request.POST['email']
        c = request.POST['num']
        d = request.POST['date']
        e = request.POST['time']
        f = request.POST['guests']
        g = request.POST['requests']
        bb=Reservation.objects.create(name=a,email=b,num=c,date=d,time=e,guests=f,requests=g)
        bb.save()
    aq='Book Us!'
    return render(request, 'indianexpress/reservation.html', {'indianexpress': reservation}, {'title':aq})


def menu(request):
    return render(request, 'indianexpress/menu.html', {'indianexpress': menu})


def cart(request):
    return render(request, 'indianexpress/cart.html', {'indianexpress': cart})

def gallery(request):
    return render(request, 'indianexpress/gallery.html', {'indianexpress': gallery})
