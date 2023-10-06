from django.urls import path
from . import views

app_name = "WebhookApp"

urlpatterns = [
    path(
        "", views.webhook_endpoint, name="webhook_endpoint"
    ),  # Inclua as URLs do aplicativo UsersApp
]
