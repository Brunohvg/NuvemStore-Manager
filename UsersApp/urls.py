from django.urls import path
from . import views

app_name = "UsersApp"  # Defina um namespace para o aplicativo

urlpatterns = [
    path("", views.login_user, name="login"),  # Exemplo de URL
    path("signup/", views.signup, name="signup"),  # Views responsavel Auth user
    path("deslogar/", views.user_logout, name="logaut"),
]
