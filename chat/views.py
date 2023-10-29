from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import MyForm
from .models import UserProfile


# Create your views here.
def homepage(request):
    if request.method == 'POST':
        form = MyForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            # Check if the there is a user in the database
            auth = authenticate(request, username=username, password=password)
            if auth is not None:
                return redirect('chat:chat-page')
            else:
                return HttpResponse("Invalid username or password")

    else:
        form = MyForm()
    return render(request, 'landing.html', {'form': form})


def messagePage(request):
    return render(request, 'chat-room-page.html')


def signUp(request):
    if request.method == 'POST':
        form = MyForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            # Checks if the username is already taken inside the database
            # So we don't have duplicate users
            if User.objects.filter(username=username).exists():
                return HttpResponse("Username already exists")

            # Create a new User object
            user = User.objects.create_user(username=username, password=password)
            # Create a new UserProfile object
            user_profile = UserProfile(user=user)
            user_profile.save()
            return redirect('chat:homepage')

    else:
        form = MyForm()
    return render(request, 'signUpPage.html', {'form': form})
