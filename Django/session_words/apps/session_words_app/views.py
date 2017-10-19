from __future__ import unicode_literals
from datetime import datetime
from django.shortcuts import render, HttpResponse, redirect

def index(request):
    return render(request, 'session_words_app/wordsapp.html')

def process(request):
    new_word = {}
    for key, value in request.POST.iteritems():
        # print key, "=", value
        if key != "csrfmiddlewaretoekn" and key != "show-big":
            new_word[key] = value
        if key == "show-big":
            new_word['big'] = "big"
        else:
            new_word['big'] = ""
    new_word['created_at'] = datetime.now().strftime("%I:%M %p, %B %d, %Y")
    try:
        request.session['words']
    except KeyError:
        request.session['words'] = []

    temp_list = request.session['words']
    temp_list.insert(0, new_word)
    request.session['words'] = temp_list
    # for key, val in request.session.__dict__.iteritems():
    #     print key, val
    # for key in request.session.keys():
    #     print "HERE = ", request.session[key]
    # print "past created at", new_word    

    return redirect('/')

def clear(request):
    for key in request.session.keys():
        del request.session[key]
    return redirect('/')

# Create your views here.
