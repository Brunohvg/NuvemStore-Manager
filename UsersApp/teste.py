from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect


def signup(request):
    if request.method == "POST":
        # Obtenha os dados do formulário de registro
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]

        # Crie um novo usuário
        user = User.objects.create_user(
            username=username, email=email, password=password
        )
        user.save()

        # Faça o login do usuário após o registro bem-sucedido
        login(request, user)

        # Redirecione para outra página após o registro bem-sucedido
        return redirect(
            "nome_da_view_de_redirecionamento"
        )  # Substitua 'nome_da_view_de_redirecionamento' pela view desejada
    else:
        # Exiba o formulário de registro para o usuário
        return render(
            request, "signup.html"
        )  # Substitua 'signup.html' pelo nome do seu template de registro
