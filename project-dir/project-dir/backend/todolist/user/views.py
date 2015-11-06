from django.shortcuts import render, render_to_response, get_object_or_404,redirect
from django.contrib import auth
from django.http import HttpResponse , HttpResponseRedirect
from django.core.context_processors import csrf
from django.contrib.auth.forms import UserCreationForm
from forms import RegForm
from django.contrib.auth import logout
from django.contrib.auth.models import User

def register_user(request):
    # if request.method == 'POST':
    #     form = RegForm(request.POST)
    #     if form.is_valid():
    #         print 'form is valid! here'
    #         form.save()
    #         return redirect('login')
    #     else:
    #         print form.errors
    args = {}
    args.update(csrf(request))
    args['form'] = RegForm()
    return render_to_response('todo/register.html',args)


def render_login(request):
    return render(request,'todolist.html')

def login(request):
    c = {}
    c.update(csrf(request))
    if not request.user.is_authenticated():
        return render_login(request)
    return redirect('index')

def auth_view(request):
    username = request.POST.get('username','')
    password = request.POST.get('password','')
    user = auth.authenticate(username=username,password=password)

    if user is not None:
        auth.login(request,user)
        return redirect('index')
    else:
        return redirect('register')

def loggedin(request):
    return render_to_response( 'societal/loggedin.html',
                                {'full_name' :request.user.username })

def invalid_login(request):

    return render_login(request)

def logout_view(request):
    if request.user.is_authenticated():
        print "logged on!"
        logout(request)
    print "not logged in"
    return redirect('index')