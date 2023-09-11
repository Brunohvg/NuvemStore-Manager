from django.urls import path
from . import views

app_name = "FreteApp"  # Defina um namespace para o aplicativo

urlpatterns = [
    path("", views.base, name="base"),  # Exemplo de URL no aplicativo FreteApp
]
