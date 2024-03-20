from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, "home/index.html")


def manolo(request):
    return render(request, "home/manolo.html")
