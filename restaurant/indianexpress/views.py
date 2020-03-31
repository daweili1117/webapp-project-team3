from django.shortcuts import render
from django.shortcuts import redirect

# Create your views here.

from .forms import SignUpForm


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
    return render(request, 'indianexpress/reservation.html', {'indianexpress': reservation})


def menu(request):
    return render(request, 'indianexpress/menu.html', {'indianexpress': menu})


def cart(request):
    return render(request, 'indianexpress/cart.html', {'indianexpress': cart})

def gallery(request):
    return render(request, 'indianexpress/gallery.html', {'indianexpress': gallery})
