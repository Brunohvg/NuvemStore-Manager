from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import HttpResponse
from .forms import CommentForm

from django.contrib.auth.signals import user_logged_out
from django.core.cache import cache


def clear_user_cache(sender, user, request, **kwargs):
    cache.delete(f"roles_{user.id}")


user_logged_out.connect(clear_user_cache)


def login_user(request):
    if request.method == "GET":
        return render(request, template_name="UsersApp/login_user.html")
    else:
        user = request.POST.get("username")
        password = request.POST.get("password")

        if user and password:
            user_auth = authenticate(request, username=user, password=password)

            if user_auth:
                login(request, user_auth)
                print(user_auth)

                return redirect("FreteApp:dashboard")
            else:
                messages.error(request, "Usuário ou senha inválido.")
        else:
            messages.error(request, "Por favor, preencha todos os campos.")

        return redirect("UsersApp:login")


def user_logout(request):
    logout(request, "deslogado")

    return redirect("UsersApp:login")


def signup(request):
    if request.method == "POST":
        username = request.POST.get("email_user")
        email = request.POST.get("email_user")
        password = request.POST.get("password")

        # Verificar se o usuário já existe
        existing_user = User.objects.filter(username=username).exists()
        if existing_user:
            return HttpResponse("Usuário já existe. Escolha outro nome de usuário.")

        # Criar um novo usuário
        user = User.objects.create_user(username=email, email=email, password=password)
        user.save()

        # Redirecionar para outra página após o registro bem-sucedido
        return redirect("nome_da_view")

    comment_form = CommentForm()

    return render(request, "UsersApp/signup.html", context={"form": comment_form})


def edit_user(request):
    ...


def delit_user(request):
    ...
