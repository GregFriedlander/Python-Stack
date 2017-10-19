from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect
from models import *
from django.contrib.messages import error 
# Create your views here.

def index(request):

    users = Users.objects.all()

    context = {
        "users": users
    }

    return render(request, "semi_restful/userboard.html", context)

def new(request):
    return render(request, "semi_restful/newuser.html")

def create(request):
    if request.method == "POST":
        errors = Users.objects.validate(request.POST)
        if len(errors):
            for field, message in errors.iteritems():
                error(request, message, extra_tags=field)
            return redirect('/users/new')

        Users.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'])
    return redirect('/')

def show(request, user_id):
    
    users = Users.objects.get(id=user_id)

    context = {

        "users": users

    }

    return render(request, "semi_restful/show.html", context)

def edit(request, user_id):

    users = Users.objects.get(id=user_id)

    context = {
        "users": users
    }

    return render(request, "semi_restful/edit.html", context)

def update(request, user_id):
    if request.method == "POST":

        errors = Users.objects.validate(request.POST)
        if len(errors):
            for field, message in errors.iteritems():
                error(request, message, extra_tags=field)
            return redirect('/users/{}/edit'.format(user_id))

        user_updated = Users.objects.get(id=user_id)
        user_updated.first_name = request.POST['first_name']
        user_updated.last_name = request.POST['last_name']
        user_updated.email = request.POST['email']
        user_updated.save()
        return redirect('/users')

def delete(request, user_id):
    this_user = Users.objects.get(id=user_id)
    this_user.delete()
    return redirect('/users')