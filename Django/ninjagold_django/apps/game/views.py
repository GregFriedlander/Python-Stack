from __future__ import unicode_literals 
from datetime import datetime
import random 
from django.shortcuts import render, HttpResponse, redirect

# Create your views here.

def index(request):
    try:
        request.session['total']
    except KeyError:
        request.session['total'] = 0
    return render(request, "game/game.html")

def process(request, building_type):
    this_gold = 0
    action = "earned"
    if building_type == "farm":
        this_gold = random.randrange(10,21)
    if building_type == "cave":
        this_gold = random.randrange(5,11)
    if building_type == "house":
        this_gold = random.randrange(2,6)
    if building_type == "casino":
        this_gold = random.randrange(-50,51)
        if this_gold < 0:
            action = "lost"
    
    timestamp = datetime.now().strftime("%Y/%m/%d %-I:%M%p")
    this_log = {
        "class": action,
        "message": "You {} {} From the {} ({})".format(action, abs(this_gold), building_type, timestamp)
    }
    try: 
        log_list = request.session['logs']
    except KeyError:
        log_list = []
    
    request.session['total'] += this_gold

    log_list.append(this_log) 
    request.session['logs'] = log_list

    return redirect('/')

def restart(request):
    for key in request.session.keys():
        del request.session[key]
    return redirect('/')