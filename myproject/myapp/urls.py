from rest_framework import routers,serializers,viewsets
from django.urls import path
from django.urls import include
from . import views
urlpatterns = [

    path('external-books',views.getBooks),
    path('v1/books', views.book_list),
    path('v1/books/<int:pk>/', views.book_detail),
    path('v1/books/<int:pk>/DELETE/',views.book_detail),
]