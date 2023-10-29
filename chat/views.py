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

            # Check if the username already exists
            if User.objects.filter(username=username).exists():
                # Handle the case where the username already exists
                # Display an error message or redirect to a different page
                return HttpResponse("Username already exists")

            # Create a new User object
            user = User.objects.create(username=username)
            # Create a new UserProfile object
            user_profile = UserProfile(user=user, name=username)
            user_profile.save()
            return redirect('chat:chat-page')
    else:
        form = MyForm()
    return render(request, 'landing.html', {'form': form})


def messagePage(request):
    return render(request, 'message.html')
