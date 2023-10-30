from django.contrib.auth import authenticate
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
                request.session['username'] = username
                return redirect('chat:chat-page')
            else:
                return HttpResponse("Invalid username or password")

    else:
        form = MyForm()
    return render(request, 'landing.html', {'form': form})


def messagePage(request):
    username = request.session.get('username')
    if not username:
        return redirect('login-page')

    if request.method == 'POST':
        message = request.POST.get('message')

    return render(request, 'chat-room-page.html')


def signUp(request):
    # if a form was submitted with the request then do this
    if request.method == 'POST':
        form = MyForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            # Checks if the username is already taken inside the database
            # So we don't have duplicate users
            if UserProfile.objects.filter(username=username).exists():
                return HttpResponse("Username already exists")

            # Create a new User object
            user = UserProfile.objects.create_user(username=username, password=password)
            # saves to database
            user.save()
            # redirects to the login page!
            return redirect('chat:homepage')
    # otherwise simply return the page and prep the form for submission
    else:
        form = MyForm()
    return render(request, 'signUpPage.html', {'form': form})
