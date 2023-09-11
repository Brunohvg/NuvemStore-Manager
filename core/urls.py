from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("auth/", include("UsersApp.urls")),  # Inclua as URLs do aplicativo UsersApp
    path("admin/", admin.site.urls),
    path("cotar/", include("FreteApp.urls")),  # Inclua as URLs do aplicativo FreteApp
]
