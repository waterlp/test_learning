from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    #return HttpResponse("Hello Django")
    return render(request, "index.html")

def login_action(request):
    if request.method == "POST":
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        #if username == 'admin' and password == 'admin123':
        if user is not None:
            auth.login(request, user)
            request.session['user'] = username
            #return HttpResponse('login success')
            response = HttpResponseRedirect('/event_manage/')
            #response.set_cookie('user', username, 3600)
            return response
        else:
            return render(request, 'index.html', {'error': 'username or password error!'})

@login_required
def event_manage(request):
    #username = request.COOKIES.get('user', '')
    username = request.session.get('user', '')
    return render(request, "event_manage.html", {"user":username})