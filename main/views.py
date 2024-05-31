from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'main/index.html')

def aboutHTTP(request):
    return HttpResponse("<h4>About</h4>")

def about(request):
    return render(request, 'main/about_us.html')