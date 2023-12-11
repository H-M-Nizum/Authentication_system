from django.shortcuts import render
from .forms import RegistationForm

# Create your views here.

def user_signup(request):
    form = RegistationForm()
    if request.method == 'POST':
        form = RegistationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = RegistationForm()
    return render(request, 'signup.html', {'form': form})