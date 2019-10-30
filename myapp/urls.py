
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home),
    path('next/', views.page1),
]
