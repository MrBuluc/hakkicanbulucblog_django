from django.contrib import admin
from django.urls import path
from . import views
app_name = "project"

urlpatterns = [
    path('create/', views.index, name="index"),
]
