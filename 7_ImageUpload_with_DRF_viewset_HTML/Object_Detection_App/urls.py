from django.urls import path

from Object_Detection_App.views import index

urlpatterns = [
    path("", index, name="index"),
]

