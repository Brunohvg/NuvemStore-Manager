from django.urls import path
from . import views

app_name = "LinkApp"

urlpatterns = [
    path(
        "", views.gerar_link, name="gerar_link"
    ),  # Inclua as URLs do aplicativo UsersApp
]
