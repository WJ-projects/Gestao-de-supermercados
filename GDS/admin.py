from django.contrib import admin
from .models import Cliente, Endereco

# Register your models here.

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ("nome", "cpf", "email_cliente", "Nome_e_numero_da_casa",)

@admin.register(Endereco)
class EnderecoAdmin(admin.ModelAdmin):
    list_display = ("nome_rua", "numero_casa", "bairro", "complemento", "cep",)
