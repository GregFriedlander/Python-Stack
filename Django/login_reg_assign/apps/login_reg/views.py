from __future__ import unicode_literals
import bcrypt
from django.shortcuts import render, HttpResponse, redirect
from models import *
from django.contrib import messages

# Create your views here.

def index(request):
   return render(request, "login_reg/login_reg.html")

def register(request):
    if request.method == "POST":
        errors = Users.objects.validate_reg(request.POST)
        if len(errors):
            for key in errors:
                print errors[key]
                messages.error(request, errors[key])
            return redirect('/') 
    
        pw = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
        user = Users.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'], password=pw)
        request.session['id'] = user.id
        messages.success(request, "Successfully registered!")

    return redirect ('/success')

def login(request):
    login_return = Users.objects.login_reg(request.POST)
    if 'user' in login_return:
        request.session['id'] = login_return['user'].id
        messages.success(request, "Successfully logged in!")
        return redirect ('/success')
    else:
        messages.error(request, login_return['error'])
        return redirect ('/')

def success(request):

    users = Users.objects.get(id=request.session['id'])

    context = {
        "users": users
    }

    return render (request, "login_reg/success.html", context)
