from django.shortcuts import render, HttpResponse, redirect 

# Create your views here.

def index(response):
    return HttpResponse("placeholder to later display all the list of users")

def new(response):
    return HttpResponse("placeholder to display a new form to create a new user")

def login(response):
    return HttpResponse("placeholder for users to login")