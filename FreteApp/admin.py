from django.contrib import admin
from .models import Cliente, Endereco, Entrega

# Register your models here.
admin.site.register(Endereco)
admin.site.register(Cliente)
admin.site.register(Entrega)


