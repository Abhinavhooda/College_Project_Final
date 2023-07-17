import re
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render, redirect
from .models import *
from .forms import SignUpForm
from stations.models import *

def home(request):
    stations = Station.objects.filter()
    return render(request, 'core/index.html', {'stations': stations})

def chargingstations(request):
    stations = Station.objects.all()
    query = request.GET.get('query', '')

    if query:
        stations = stations.filter(Q(name__icontains=query) | Q(description__icontains=query))
    return render(request, 'core/stations.html', {'stations': stations})

def about(request):
    return render(request, 'core/about.html', {})
    
    

# @login_required
# def booking(request, slot_id):
#     slot = get_object_or_404(ChargingSlot, pk=slot_id)
#     if not slot.is_available:
#         # Slot is already booked
#         return redirect('home')

#     if request.method == 'POST':
#         start_time = request.POST['start_time']
#         end_time = request.POST['end_time']
#         # Create a booking
#         Booking.objects.create(user=request.user, charging_slot=slot, start_time=start_time, end_time=end_time)
#         # Update slot availability
#         slot.is_available = False
#         slot.save()
#         return redirect('booking_success')

#     return render(request, 'booking.html', {'slot': slot})

def helpline(request):
    return render(request, 'core/helpline.html', {})

@login_required
def My_account(request):
    return render(request, 'core/myaccount.html', {})

@login_required
def edit_myaccount(request):
    if request.method == 'POST':
        user = request.user
        user.first_name = request.POST.get('first_name')
        user.last_name = request.POST.get('last_name')
        user.email = request.POST.get('email')
        user.username = request.POST.get('username')
        user.save()

        return redirect('myaccount')
    return render(request, 'core/edit_myaccount.html')
    
    

@login_required
def booking_success(request):
    return render(request, 'booking_success.html')

@login_required
def my_bookings(request):
    bookings = Booking.objects.filter(user=request.user)
    return render(request, 'my_bookings.html', {'bookings': bookings})

# def login_view(request):
#     if request.method == 'POST':
#         form = AuthenticationForm(request, data=request.POST)
#         if form.is_valid():
#             user = form.get_user()
#             login(request, user)
#             return redirect('/')
#     else:
#         form = AuthenticationForm()
    
#     return render(request, 'registration/login.html', {'form': form})

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
            user = form.save()

            login(request, user)

            return redirect('/')
    else:
        form = SignUpForm()

    return render(request, 'registration/signup.html', {'form': form})

def offers_view(request):
    return render(request, 'core/offers.html', {})
