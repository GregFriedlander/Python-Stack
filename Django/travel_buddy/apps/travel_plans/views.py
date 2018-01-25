# from __future__ import unicode_literals 
import bcrypt
from django.shortcuts import render, redirect, HttpResponse
from models import *
from django.contrib import messages 
from datetime import datetime

# Create your views here.


def index(request):
    return render(request, "travel_plans/login.html")

def register(request):
    if request.method == "POST":
        errors = Users.objects.validate_reg(request.POST)
        if len(errors):
            for key in errors:
                messages.error(request, errors[key])
            return redirect('/')
    
    pw = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
    user = Users.objects.create(name=request.POST['name'], username=request.POST['username'], email=request.POST['email'], password=pw)
    request.session['id'] = user.id
    request.session['name'] = user.name
    request.session['username'] = user.username
    request.session['email'] = user.email
        
    
    return redirect('/homepage')

def login(request):
    login_return = Users.objects.validate_login(request.POST)
    if 'user' in login_return:
        request.session['id'] = login_return['user'].id
        request.session['name'] = login_return['user'].name
        request.session['username'] = login_return['user'].username
        request.session['email'] = login_return['user'].email
        
        return redirect('/homepage')
    else:
        messages.error(request, login_return['error'])
        return redirect('/')

# def logout(request):
#     for key in request.session.keys():
#         del request.session[key]
#     return redirect('/')
    
# def homepage(request):
#     this_user = Users.objects.get(id=request.session['id'])
#     user_trips = this_user.trips.all()
#     not_user = Users.objects.exclude(id=request.session['id'])

#     context = {
#         "user_trips": user_trips,
#         "not_user": not_user
#     }


#     return render (request, "travel_plans/homepage.html", context)

# def add(request):
#     return render (request, "travel_plans/add.html")

# def trip(request, trip_id):
#     trip = Trips2.objects.get(id=trip_id)
#     # travelers = Users.trips.filter(id=trip_id)   WAS ALREADY COMMENTED
#     context = {
#         "trip": trip,
#         # "travelers": travelers
#     }

#     return render (request, "travel_plans/trippage.html", context )

# def process(request):
#     if len(request.POST['destination']) < 1 or len(request.POST['description']) < 1:
#         messages.error(request, "Destination and Description must both be filled in")
#         return redirect('/add')
#     # if startdate < currentdate:     WAS ALREADY COMMENTED
#     #     messages.error(request, "Start date cannot be in the past")   WAS ALREADY COMMENTED
#     #     return redirect('/add')   WAS ALREADY COMMENTED
#     if request.POST['end'] < request.POST['start']:
#         messages.error(request, "End date must be after start date")
#         return redirect('/add')
#     else:
#         Trips2.objects.create(destination=request.POST['destination'], description=request.POST['description'], start=request.POST['start'], end=request.POST['end'])
#         this_user = Users.objects.get(id=request.session['id'])
#         this_trip = Trips2.objects.last()
#         this_trip.users.add(this_user)
#         return redirect ('/homepage')
    