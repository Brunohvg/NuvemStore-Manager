from django.urls import path
from . import views

app_name = "UsersApp"  # Defina um namespace para o aplicativo

urlpatterns = [
    path("login/", views.login_user, name="login"),  # Exemplo de URL
    path("signup/", views.signup, name="signup"),  # Views responsavel Auth user
]
