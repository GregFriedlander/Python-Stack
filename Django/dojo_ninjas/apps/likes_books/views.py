from django.shortcuts import render, HttpResponse, redirect

def index(request):
    return HttpResponse("Likes and Books")

# Create your views here.
