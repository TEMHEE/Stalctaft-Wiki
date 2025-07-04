from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'main/index.html')

def about(request):
    return render(request, 'main/about.html')

def pvp(request):
    return render(request, 'main/pvp.html')

def artifacts(request):
    return render(request, 'main/artifacts.html')

def guides(request):
    return render(request, 'main/guides.html')

def maps(request):
    return render(request, 'main/maps.html')

def login(request):
    return render(request, 'main/login.html')