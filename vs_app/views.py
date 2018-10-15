from django.shortcuts import render, redirect
from django.conf import settings
from .forms import UserForm, CustomUserForm, VenueForm
from django.http import HttpResponse
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

# Create your views here.

def landing(request):
    return render(request, 'vs_app/landing.html')


# USER AUTH FUCNTIONS
def signup(request):
    signedup = False
    if request.method == 'POST':
        user_form = UserForm(request.POST, request.FILES)
        customuser_form = CustomUserForm(request.POST, request.FILES)
        if user_form.is_valid() and customuser_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            customuser = customuser_form.save(commit=False)
            customuser.user = user
            customuser.save()
            # email_signup(request, user)
            signedup = True
        else:
            print(user_form.errors,customuser_form.errors)
    else:
        user_form = UserForm()
        customuser_form = CustomUserForm()
    return render(request, 'vs_app/signup.html', {'user_form':user_form,'customuser_form':customuser_form,'signedup':signedup})

def log_in(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request,user)
                print("Login successful")
                return redirect('landing')
            else:
                return HttpResponse("Your account was inactive.")
        else:
            print("Someone tried to login and failed.")
            print(f'They used username: {username} and password: {password}')
            return HttpResponse("Invalid login details given")
    else:
        user_form = UserForm()
        return render(request, 'vs_app/login.html', {'user_form': user_form})

@login_required
def log_out(request):
    logout(request)
    return redirect('landing')

# USER CRUD FUNCTIONS
# @staff_member_required
def user_list(request):
    users = CustomUser.objects.all()
    return render(request, 'vs_app/user_list.html', {'users': users})

@login_required
def user_detail(request, pk):
    user_is_making_req = request.user
    user = User.objects.get(id=pk)
    custom_user = CustomUser.objects.get(id=pk)
    venues = Venue.objects.all()
    return render(request,  "vs_app/user_detail.html", {'custom_user' : custom_user , 'user' : user, 'venues' : venues , 'user_is_making_req' : user_is_making_req})

@login_required
def user_edit(request, pk):
    user = CustomUser.objects.get(pk=pk)
    if request.method == "POST":
        customuser_form = CustomUserForm(request.POST, instance=user)
        if customuser_form.is_valid():
            user = customuser_form.save()
            return redirect('user_detail', pk=user.pk)
    else:
        customuser_form = CustomUserForm(instance=user)
    return render(request, 'vs_app/user_edit.html', {'customuser_form': customuser_form, 'user': user})

@login_required
def user_delete(request, pk):
    CustomUser.objects.get(id=pk).delete()
    return redirect('user_list')


# VENUE CRUD FUNCTIONS
def venue_list(request):
    venues = Venue.objects.all()
    return render(request, 'vs_app/venue_list.html', {'venues': venues})

def venue_detail(request, pk):
    venue = Venue.objects.get(id=pk)
    return render(request, 'vs_app/venue_detail.html', {'venue': venue})

def venue_sound(request, pk):
    venue = Venue.objects.get(id=pk)
    return render(request, 'vs_app/venue_sound.html', {'venue': venue})

def venue_lights(request, pk):
    venue = Venue.objects.get(id=pk)
    return render(request, 'vs_app/venue_lights.html', {'venue': venue})

def venue_electrical(request, pk):
    venue = Venue.objects.get(id=pk)
    return render(request, 'vs_app/venue_electrical.html', {'venue': venue})

def venue_stage(request, pk):
    venue = Venue.objects.get(id=pk)
    return render(request, 'vs_app/venue_stage.html', {'venue': venue})

def venue_back(request, pk):
    venue = Venue.objects.get(id=pk)
    return render(request, 'vs_app/venue_back.html', {'venue': venue})

@login_required
def venue_create(request):
    currentUser = User.objects.get(id= request.user.pk)
    form = VenueForm(request.POST, request.FILES)
    form.manager = currentUser
    if request.method == 'POST':
        if form.is_valid():
            venue = form.save(commit = False)
            venue.manager = CustomUser.objects.get(id= request.user.pk)
            venue.save() 
            return redirect('venue_detail', venue.pk)
    if request.method == 'GET':
        form = VenueForm()
    return render(request, 'vs_app/venue_create.html', {'form': form})

@login_required
def venue_edit(request, pk):
    venue = Venue.objects.get(pk=pk)
    if request.method == "POST":
        venue_form = VenueForm(request.POST, instance=venue)
        if venue_form.is_valid():
            venue = venue_form.save()
            return redirect('venue_detail', pk=venue.pk)
    else:
        venue_form = VenueForm(instance=venue)
    return render(request, 'vs_app/venue_edit.html', {'venue_form': venue_form})

@login_required
def venue_delete(request, pk):
    Venue.objects.get(id=pk).delete()
    return redirect('venue_list')
