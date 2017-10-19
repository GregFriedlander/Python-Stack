from django.shortcuts import render, HttpResponse, redirect 
from time import gmtime, strftime, localtime


def index(request):
    
    context = {
        "date": strftime("%b %d, %Y", gmtime()),
        "time": strftime("%I:%M %p", gmtime()),
    }
    return render(request, 'displaytime/displaytime.html', context)

# Create your views here.
