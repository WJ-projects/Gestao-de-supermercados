from django.contrib import admin
from .models import Cliente, Endereco, Funcionario, Funcao, Cadastrar_produto, Venda, Despesa, Fornecedore

# Register your models here.

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ("nome", "cpf", "email_cliente", "Nome_e_numero_da_casa",)

@admin.register(Endereco)
class EnderecoAdmin(admin.ModelAdmin):
    list_display = ("nome_rua", "numero_casa", "bairro", "complemento", "cep",)

@admin.register(Funcionario)
class FuncionarioAdmin(admin.ModelAdmin):
    list_display = ("nome_funcionario", "cpf_funcionario", "email_funcionario", "codigo_de_contrato", "fk_funcao", "status")

admin.site.register(Funcao)