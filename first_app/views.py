from django.shortcuts import render, redirect
from .forms import RegistationForm
from django.contrib import messages

from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, SetPasswordForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
# Create your views here.

def user_signup(request):
    if not request.user.is_authenticated:
        form = RegistationForm()
        if request.method == 'POST':
            form = RegistationForm(request.POST)
            if form.is_valid():
                messages.success(request, 'Account create susccessfully')
                form.save()
        else:
            form = RegistationForm()
        return render(request, 'signup.html', {'form': form})
    else:
        return redirect('home')



def userlogin(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = AuthenticationForm(request=request, data = request.POST)
            if form.is_valid():
                name = form.cleaned_data['username']
                userpassword = form.cleaned_data['password']

                # check database contain user or not
                user = authenticate(username = name, password = userpassword)

                if user is not None:
                    messages.success(request, 'Logged in susccessfully')
                    login(request, user)
                    return redirect('profile')
        else:
            form = AuthenticationForm()
        return render(request, './login.html', {'form':form})
        
    else:
        return redirect('user_signup')
 
    
def profile(request):
    if request.user.is_authenticated:
        return render(request, 'profile.html', {'user': request.user})
    else:
        return redirect('login')



def userlogout(request):
    messages.success(request, 'logged out susccessfully')
    logout(request)
    return redirect('home')


def passward_change(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = PasswordChangeForm(user = request.user, data=request.POST)
            if form.is_valid():
                form.save()
                # password update 
                update_session_auth_hash(request, form.user)
                return redirect('profile')
        else:
            form = PasswordChangeForm(user=request.user)

        return render(request, 'passwordChange.html', {'form': form})

    else:
        return redirect('login')


def passward_change2(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = SetPasswordForm(user = request.user, data=request.POST)
            if form.is_valid():
                form.save()
                # password update 
                update_session_auth_hash(request, form.user)
                return redirect('profile')
        else:
            form = SetPasswordForm(user=request.user)

        return render(request, 'passwordChange.html', {'form': form})
    else:
        return redirect('login')