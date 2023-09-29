# FreteApp/urls.py
from django.urls import path
from . import views

app_name = "FreteApp"  # Defina um namespace para o aplicativo

urlpatterns = [
    path("", views.dashboard, name="dashboard"),
    path("calculadora/", views.calculadora, name="calculadora"),
    path("entregas/", views.listar_entregas, name="entregas")
    # Exemplo de URLs no aplicativo FreteApp
]
