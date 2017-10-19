from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string
import random
import string

# Create your views here.

def index(request):
    try:
        request.session['tries']
    except KeyError:
        request.session['tries'] = 1
    request.session['word'] = get_random_string(length=14)
    return render(request, "randomwordapp/randomwordapp.html")

def generate(request):
    request.session['tries'] += 1
    return redirect('/')

def reset(request):
    del request.session['tries']
    del request.session['word']
    return redirect('/')