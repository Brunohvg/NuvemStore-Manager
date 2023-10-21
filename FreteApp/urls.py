# FreteApp/urls.py
from django.urls import path
from . import views

app_name = "FreteApp"  # Defina um namespace para o aplicativo

urlpatterns = [
    path("", views.dashboard, name="dashboard"),
    path("calculadora/", views.calculadora, name="calculadora"),
    path("entregas/", views.listar_entregas, name="entregas"),
    path("detalhes/<str:identificador>", views.detalhes, name="detalhes"),
    path("imprimir/<str:identificador>", views.gerar_pdf, name="gerar_pdf"),
    path("exluir/<str:identificador>", views.deletar_entrega, name="deletar_entrega"),
    path("consultar_end/", views.consultar_end_google, name="end_google")
    # Exemplo de URLs no aplicativo FreteApp
]
