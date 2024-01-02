from django.shortcuts import render, redirect
from . import forms
from .forms import RegistrationForm
from . import models
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
# Create your views here.

def user_singup(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = RegistrationForm(request.POST)
            if form.is_valid():
                form.save()
        else:
            form = RegistrationForm()
        return render(request, 'user_singup.html', {'form' : form})
    else:
        return redirect('profile')

class SignUpView(CreateView):
    # model = models.Musician
    form_class = forms.RegistrationForm
    template_name = 'user_singup.html'
    success_url = reverse_lazy('singup')


# def user_login(request):
#     if not request.user.is_authenticated:
#         if request.method == 'POST':
#             form = AuthenticationForm(request = request, data = request.POST)
#             if form.is_valid():
#                 name = form.cleaned_data['username']
#                 userpassword = form.cleaned_data['password']
#                 user = authenticate(username = name, password = userpassword)
#                 if user is not None:
#                     login(request, user)
#                     messages.success(request, 'Logged In Successfully')
#                     return redirect('profile')
#         else:
#             form = AuthenticationForm()
#         return render(request, 'user_login.html', {'form' : form})
#     else:
#         return redirect('profile')
    
class UserLoginView(LoginView):
    template_name = 'user_login.html'
    def get_success_url(self):
        return reverse_lazy('profile')
    
# def user_logout(request):
#     logout(request)
#     messages.success(request, 'Logged Out Successfully')
#     return redirect('homepage')
    

class UserLogoutView(LogoutView):
    def get_success_url(self):
        return reverse_lazy('homepage')

# def add_musician(request):
#     if request.method == 'POST':
#         musician_form = forms.MusicianFrom(request.POST)
#         if musician_form.is_valid():
#             musician_form.save()
#             return redirect('add_musician')
#     else:
#         musician_form = forms.MusicianFrom()
#     return render(request, 'add_musician.html', {'form' : musician_form})

class AddMusicianCreateView(CreateView):
    model = models.Musician
    form_class = forms.MusicianFrom
    template_name = 'add_musician.html'
    success_url = reverse_lazy('add_musician')


def user_profile(request):
    return render(request, 'profile.html')




