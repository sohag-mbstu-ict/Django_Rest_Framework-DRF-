from django.urls import path
from DjangoRESTApp import views

urlpatterns = [
    path('article/', views.articlelist,name="articlelist"),
    path('article/<int:pk>/', views.articlelist_detail,name="articlelist_detail"),
]
