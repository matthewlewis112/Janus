from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.hallPassHome),
    path('Leave/', views.leave),
    path('Return/', views.returning),
    path('Leave/Submitted/', views.submitted),
    path('Return/Submitted/', views.submitted)
]