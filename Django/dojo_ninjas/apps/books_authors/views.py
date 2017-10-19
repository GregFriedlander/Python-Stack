from django.shortcuts import render, HttpResponse, redirect

def index(request):
    return HttpResponse("Authors and Books")
# Create your views here.
