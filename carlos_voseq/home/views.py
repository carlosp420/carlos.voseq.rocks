from django.shortcuts import render


def index(request):
    return render(request, "home/index.html")


def manolo(request):
    return render(request, "home/manolo.html")


def portfolio(request):
    return render(request, "home/portfolio.html")
