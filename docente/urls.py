from django.contrib import admin
from django.urls import path, include
from . import views

app_name="docente"
urlpatterns = [
    path('', views.docente,name="docentes"),
]