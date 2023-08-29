from typing import Any
from django.shortcuts import render, redirect
from django import forms
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class AppUserForm(UserCreationForm):
    username = forms.CharField(label='Ник', min_length=5, max_length=150, widget=forms.TextInput(attrs={'class': 'form-control form-control-lg'}))
    first_name = forms.CharField(label='Имя', required=False, widget=forms.TextInput(attrs={'class': 'form-control form-control-lg'}))
    last_name = forms.CharField(label='Фамилия', required=False, widget=forms.TextInput(attrs={'class': 'form-control form-control-lg'}))
    password1 = forms.CharField(label='Пароль', required=False, widget=forms.PasswordInput(attrs={'class': 'form-control form-control-lg'}))
    password2 = forms.CharField(label='Подтверждение пароля', required=False, widget=forms.PasswordInput(attrs={'class': 'form-control form-control-lg'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'password1', 'password2')

    def save(self, commit: True):
        user = super(AppUserForm, self).save(commit=False)
        if commit:
            user.save()
        return user


def register(request):
    if request.method == "POST":
        user_form = AppUserForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password1'])
            new_user.save()
            return redirect(reverse('login'))
        else:
            form = AppUserForm()
            context = {'form': form}
            context.update({'error': user_form.errors})
            return render(request, 'app_auth/register.html', context=context)#, {'error': user_form.errors})
    # else:
    form = AppUserForm()
    context = {'form': form}
    return render(request, 'app_auth/register.html', context=context)

def login_view(request):
    redirect_url = reverse('profile')
    if request.method == "GET":
        if request.user.is_authenticated:
            return redirect(redirect_url)
        else:
            return render(request, 'app_auth/login.html')
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect(redirect_url)
    return render(request, 'app_auth/login.html', {'error': 'Пользователь не найден'})
    

def profile(request):    
    return render(request, 'app_auth/profile.html')

def logout_view(request):
    logout(request)
    return render(request, 'app_auth/login.html')