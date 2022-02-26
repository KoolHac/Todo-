from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from django.http import HttpResponse
from.forms import SignForm
# Create your views here.

def signup(request):
    form = SignForm()
    if request.method == 'POST':
        form = SignForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('/accounts/login')
        else:
            return HttpResponse(form.errors)
    else:
        return render(request, 'accounts/signup.html', {'form': form})

def login_page(request):
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            if 'redirect_url' in request.POST:
                return redirect(request.POST.get('redirect_url'))
            else:
                return redirect('/todo/home/')
        else:
            return HttpResponse(form.errors)
    else:

        return render(request, 'accounts/login.html', {'form': form, 'request': request})

def logout_page(request):
    if request.method == 'POST':
        logout(request)
        return redirect('/todo/home')
    else:
        return HttpResponse('Method not allowed')
