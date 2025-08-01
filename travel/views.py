from django.shortcuts import render, redirect
from .models import Destination, Booking

def index(request):
    dests = Destination.objects.all()
    return render(request, 'travel/index.html', {'dests': dests})  # updated path

def book(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        destination_id = request.POST.get('destination')
        date = request.POST.get('date')

        Booking.objects.create(
            name=name,
            email=email,
            destination_id=destination_id,
            date=date
        )
        return redirect('home')  # make sure your URL name is 'home'
    else:
        dests = Destination.objects.all()
        return render(request, 'travel/book.html', {'dests': dests})  # updated path
