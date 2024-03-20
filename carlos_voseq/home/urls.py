from django.urls import path

from home import views

urlpatterns = [
    path("", views.index, name="index"),
    path("portolio/manolo", views.manolo, name="manolo"),
]
