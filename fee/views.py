from django.shortcuts import render, redirect
from fee. forms import UserRegistrationForm, Userdataform
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required 
@login_required
def data(request):
    if request.method == 'POST':
        userdata_form = Userdataform(request.POST,request.FILES)
        if userdata_form.is_valid():
            userdata_form.save()
        else:
            return HttpResponse('Got Invalid Data')
    return render (request, 'data.html')
def base(request):
    return render(request, 'base.html')
def register(request):
    if request.method == 'POST':
        user_form= UserRegistrationForm(data=request.POST)
        if user_form.is_valid():
            user_form.save()
            return HttpResponseRedirect(reverse('Login'))
        else:
            print(UserRegistrationForm.errors)
    else:
        user_form= UserRegistrationForm()
    return render(request, 'registration.html', {'user_form': user_form})
def user_login(request):
    if request.method == 'POST':
        username1 = request.POST.get('username')
        password1 = request.POST.get('password')
        user = authenticate (request, username=username1, password=password1)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('data'))
            else:
                return HttpResponse("Your account was inactive.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username1,password1))
            return HttpResponse("Invalid login details given")
    return render(request, 'login form.html')
def logout_view(request):
    logout(request)
    return render(request, 'logoutpage.html')
