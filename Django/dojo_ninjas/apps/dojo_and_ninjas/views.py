from django.shortcuts import render, HttpResponse, redirect


def index(request):
    return HttpResponse("Dojos and Ninjas")

# Create your views here.
