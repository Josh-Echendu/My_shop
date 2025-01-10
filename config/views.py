from django.contrib.auth import logout
from django.shortcuts import redirect, render
from django.urls import reverse
from .forms import SignupForm


def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')
    
def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = SignupForm()
        return render (request, 'products/signup2.html')