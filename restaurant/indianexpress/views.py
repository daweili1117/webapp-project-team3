# from django.contrib.auth.decorators import login_required
from itertools import product

from django.core.mail import send_mail
from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_text
from django.contrib.auth import login, authenticate

from cart.cart import Cart
from cart.forms import CartAddProductForm
from orders.forms import OrderCreateForm
from orders.models import OrderItem
from shop.models import Product, Category
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

from django.shortcuts import render, get_object_or_404

from cart.cart import Cart
from cart.forms import CartAddProductForm


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
        # user.profile.phone_number = form.cleaned_data.get('phone_number')
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
    test = Reservation.objects.all

    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            #reserve = form.save()
            #reserve.refresh_from_db()
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
