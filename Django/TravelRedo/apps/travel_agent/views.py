from __future__ import unicode_literals 
import bcrypt
from django.shortcuts import render, redirect, HttpResponse
from models import *
from django.contrib import messages 
from datetime import datetime

# Create your views here.

def index(request):
    return render(request, 'travel_agent/loginpage.html')

def register(request):
    if request.method == "POST":
        errors = User.objects.validate_reg(request.POST)
        if len(errors):
            for key in errors:
                messages.error(request, errors[key])
            return redirect('/')
    
    pw = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
    user = User.objects.create(name=request.POST['name'], username=request.POST['username'], email=request.POST['email'], password=pw)
    request.session['id'] = user.id
    request.session['name'] = user.name
    request.session['username'] = user.username
    request.session['email'] = user.email
    return redirect('/homepage')

def login(request):
    login_return = User.objects.validate_login(request.POST)
    if 'user' in login_return:
        request.session['id'] = login_return['user'].id
        request.session['name'] = login_return['user'].name
        request.session['username'] = login_return['user'].username
        request.session['email'] = login_return['user'].email
        
        return redirect('/homepage')
    else:
        messages.error(request, login_return['error'])
        return redirect('/')

def logout(request):
    for key in request.session.keys():
        del request.session[key]
    return redirect('/')

def homepage(request):
    this_user = User.objects.get(id=request.session['id'])
    user_trips = this_user.location.all()
    other_trips = Trip.objects.exclude(travelers=request.session['id'])
    print "this is other_trips", other_trips
    context = {
        "user_trips": user_trips,
        "other_trips": other_trips
    }
    return render(request, 'travel_agent/homepage.html', context)

def add(request):
    return render(request, 'travel_agent/addtrip.html')

def join(request, trip_id):
    this_trip = Trip.objects.get(id=trip_id)
    this_user = User.objects.get(id=request.session['id'])
    this_trip.travelers.add(this_user)
    return redirect('/homepage')

def processtrip(request):
    if len(request.POST['destination']) < 1 or len(request.POST['description']) < 1:
        messages.error(request, "Destination and Description must both be filled in")
        return redirect('/add')
    if request.POST['start'] < datetime.now().strftime("%Y-%m-%d"):
        messages.error(request, "Your trip must begin in the future")
        return redirect('/add')
    if request.POST['end'] < request.POST['start']:
        messages.error(request, "End date must be after start date")
        return redirect('/add')
    else:
        this_user = User.objects.get(id=request.session['id'])
        Trip.objects.create(destination=request.POST['destination'], description=request.POST['description'], start=request.POST['start'], end=request.POST['end'], creator=this_user) 
        this_trip = Trip.objects.last()
        this_trip.travelers.add(this_user)
        return redirect('/homepage')

def trip(request, trip_id):
    trip = Trip.objects.get(id=trip_id)
    trip_creator = trip.creator
    people = trip.travelers.exclude(id=trip_creator.id)
    context = {
        "trip": trip,
        "people": people
    }
    return render(request, 'travel_agent/trip.html', context)
