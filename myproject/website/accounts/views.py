from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login

from .forms import RegisterForm


def register(request):
    if request.method == 'GET':
        form = RegisterForm()
        return render(request, 'accounts/register.html', { 'form': form})

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            messages.success(request, 'You have singed up successfully. Please login!')
            return redirect('website:index')
        else:
            return render(request, 'accounts/register.html', {'form': form})