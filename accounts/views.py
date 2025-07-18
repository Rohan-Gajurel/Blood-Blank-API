from django.shortcuts import render
from django.contrib.auth import login
from .forms import RegistrationForm

# Create your views here.
def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Automatically log in the user after registration
            return render(request, "registration/login.html", {"user": user})
    else:
        form = RegistrationForm()
    
    return render(request, "registration/register.html", {"form": form})