from django.shortcuts import render, redirect

def index(request):
    return render(request, 'buff/index.html')

def add_actor(request):
    return render(request, 'buff/index.html')
