from django.urls import path

from home import views

urlpatterns = [
    path("", views.index, name="index"),
    path("portfolio", views.portfolio, name="portfolio"),
    path("portfolio/manolo", views.manolo, name="manolo"),
]
