from django.urls import path
from DjangoRESTApp import views

urlpatterns = [
    path('article/', views.ArticleList.as_view(), name='ArticleList'),
    path('article/<int:pk>/', views.ArticleList_detail.as_view(), name='ArticleList_detail'),
]
