from django.urls import path
from . import views

app_name = 'empresas'
urlpatterns = [
    path('empresas/', views.empresas, name='empresas'),
]
