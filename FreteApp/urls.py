# FreteApp/urls.py
from django.urls import path
from . import views

app_name = "FreteApp"  # Defina um namespace para o aplicativo

urlpatterns = [
    path("calculadora/", views.calculadora, name="calculadora"),
    path("", views.dashboard, name="dashboard")
    # Exemplo de URLs no aplicativo FreteApp
]
