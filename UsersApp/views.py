from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.http import HttpResponse


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

    return render(request, "UsersApp/signup.html")


def login_user(request):
    if request.method == "GET":
        return render(request, template_name="UsersApp/login_user.html")
    else:
        user = request.POST.get("username")
        password = request.POST.get("password")

        user_auth = authenticate(request, user=user, password=password)

        if user_auth:
            login(request, user_auth=user_auth)

            return redirect(render("FreteApp/cotacoes.html"))


def edit_user(request):
    ...


def delit_user(request):
    ...

class LoginUser()