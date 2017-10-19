from django.shortcuts import render, HttpResponse, redirect

def index(request):
    return render(request, 'survey/survey.html')

def create(request):
    try:
        request.session["tries"]
    except KeyError:
        request.session["tries"] = 0
    request.session['name'] = request.POST['name']
    request.session['location'] = request.POST['location']
    request.session['language'] = request.POST['language']
    request.session['comment'] = request.POST['comment']
    request.session["tries"] += 1
    return redirect('/submit')

def submit(request):
    return render(request, 'survey/result.html')

def goback(request):
    return redirect('/')

def reset(request):
    del request.session["tries"]
    return redirect('/')


# Create your views here.
