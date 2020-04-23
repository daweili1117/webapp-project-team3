# from django.contrib.auth.decorators import login_required
from itertools import product

from django.core.mail import send_mail
from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_text
from django.contrib.auth import login, authenticate

from .forms import *
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.utils.http import urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode

from django.template.loader import render_to_string

from django.shortcuts import render, get_object_or_404

from cart.cart import Cart
from cart.forms import CartAddProductForm


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
    test = Reservation.objects.all

    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            # reserve = form.save()
            # reserve.refresh_from_db()
            name = form.cleaned_data.get('name')
            email = form.cleaned_data.get('email')
            num = form.cleaned_data.get('num')
            date = form.cleaned_data.get('date')
            time = form.cleaned_data.get('time')
            guests = form.cleaned_data.get('guests')
            requests = form.cleaned_data.get('requests')

            form.save()

            ctx = {
                'name': name,
                'email': email,
                'num': num,
                'date': date,
                'time': time,
                'guests': guests,
                'requests': requests,
            }
            message = render_to_string('indianexpress/reservation.txt', ctx)
            send_mail(
                'Your reservation with IndianXpress',
                message,
                'indxpr@gmail.com',
                [email],
            )
            return render(request, 'indianexpress/confirm.html', ctx)
    else:
        aq = 'Book Us!'
    return render(request, 'indianexpress/reservation.html', {'indianexpress': reservation}, {'title': aq})


def menu(request):
    cart = Cart(request)
    for item in cart:
        item['update_quantity_form'] = CartAddProductForm(
            initial={'quantity': item['quantity'], 'update': True})
    return render(request, 'shop/product/list.html', {'cart': cart})


def cart(request):
    cart = Cart(request)
    for item in cart:
        item['update_quantity_form'] = CartAddProductForm(
            initial={'quantity': item['quantity'], 'update': True})
    return render(request, 'cart/detail.html', {'cart': cart})


def gallery(request):
    return render(request, 'indianexpress/gallery.html', {'indianexpress': gallery})
