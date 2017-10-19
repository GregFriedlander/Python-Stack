from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect
from models import *
from django.contrib.messages import error

# Create your views here.

def index(request):

    courses = Courses.objects.all().order_by("-created_at")

    context = {
        "courses": courses
    }

    return render(request, "course_creation/courses.html", context)

def create(request):
    if request.method == "POST":

        errors = Courses.objects.validate(request.POST)
        if len(errors):
            for field, message in errors.iteritems():
                error(request, message, extra_tags=field)
            return redirect('/')

        Courses.objects.create(name=request.POST['name'], desc=request.POST['description'])
    
    return redirect('/')

def confirm(request, user_id):

    courses = Courses.objects.get(id=user_id)

    context = {
        "courses": courses
    }

    return render(request, "course_creation/deletecourse.html", context)

def destroy(request, user_id):

    c = Courses.objects.get(id=user_id)

    c.delete()
    return redirect('/')