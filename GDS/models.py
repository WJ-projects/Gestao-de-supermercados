from django.db import models
from cpf_field.models import CPFField

# Create your models here.

class Cliente(models.Model):
    nome = models.CharField(max_length=255, blank=False, null=False, verbose_name='Nome completo')
    cpf = CPFField('CPF')
    email_cliente = models.EmailField(blank=True, null=True, verbose_name='E-mail')
    fk_endereco = models.ManyToManyField('Endereco', verbose_name='Nome da rua e número da casa')

    def Nome_e_numero_da_casa(self):
        return ",".join([str(p) for p in self.fk_endereco.all()])

    def __str__(self):
        return self.nome
        

class Endereco(models.Model):
    nome_rua = models.CharField(max_length=255, blank=False, null=False, verbose_name='Nome da rua')
    numero_casa = models.CharField(max_length=6, blank=False, null=False, verbose_name='Número da residência')
    bairro = models.CharField(max_length=255, blank=False, null=False, verbose_name='Bairro')
    cep = models.CharField(max_length=8, blank=False, null=False, verbose_name='CEP')
    complemento = models.CharField(max_length=255, blank=True, null=False, verbose_name='Complemento')

    def __str__(self):
        return self.nome_rua + ' --- ' + self.numero_casa


class Funcionario(models.Model):
    nome_funcionario = models.CharField(max_length=255, blank=False, null=False, verbose_name='Nome completo')
    cpf_funcionario = CPFField('CPF')
    email_funcionario = models.EmailField(blank=True, null=True, verbose_name='E-mail')
    codigo_de_contrato = models.CharField(max_length=11, blank=False, null=False, verbose_name='Código do contrato')
    fk_funcao = models.ForeignKey('Funcao', on_delete=models.DO_NOTHING, default=1, verbose_name='Cargo')
    status = models.BooleanField(blank=False, null=False, default=False, verbose_name='Situação')



class Funcao(models.Model):
    cargo = models.CharField(max_length=255, blank=False, null=False, verbose_name='Cargo')
    
    def __str__(self):
        return self.cargo


class Cadastrar_produto(models.Model):
    nome_produto = models.CharField(max_length=255, blank=False, null=False, verbose_name='Nome do produto')
    valor = models.DecimalField(max_digits=6, decimal_places=2, blank=False, null=False, verbose_name='Valor do produto')
    qtd = models.IntegerField(blank=True, null=False, default=0, verbose_name='Quantidade de produtos')
    status = models.BooleanField(blank=False, null=False, default=False)
    data_hora_cadastro = models.DateTimeField(auto_now_add=True, blank=True, null=False)


    def __str__(self):
        return self.nome_produto


class Venda(models.Model):
    fk_comprador = models.ManyToManyField('Cliente', verbose_name='Clientes')
    fk_cadastrar_produto = models.ManyToManyField('Cadastrar_produto', verbose_name='Produtos')
    qtd_itens = models.IntegerField(blank=True, null=False, default=0, verbose_name='Quantidade de Itens Vendidos')
    observacao = models.CharField(max_length=255, blank=False, null=False, verbose_name='Descrição da venda')
    data_hora_venda = models.DateTimeField(auto_now_add=True, blank=True, null=False)


    def comprador(self):
        return ",".join([str(e) for e in self.fk_comprador.all()])

    def produto_vendido(self):
        return ",".join([str(a) for a in self.fk_cadastrar_produto.all()])


class Despesa(models.Model):
    nome_despesa = models.CharField(max_length=255, blank=False, null=False, verbose_name='Nome da despesa')
    valor = models.DecimalField(max_digits=12, decimal_places=2, blank=False, null=False, verbose_name='Valor total da despesa')
    observacao = models.TextField(blank=True, null=True, verbose_name='Observação')
    data_hora = models.DateTimeField(auto_now_add=True, blank=True, null=False)


class Fornecedore(models.Model):
    nome_fantasia = models.CharField(max_length=255, blank=False, null=False, verbose_name='Nome fantasia')
    razao_social = models.CharField(max_length=255, blank=False, null=False, verbose_name='Razão social')
    cnpj = models.CharField(max_length=18, blank=False, null=False, verbose_name='Nome completo')
    email_fornecedo = models.EmailField(blank=True, null=True, verbose_name='E-mail')
    fk_endereco = models.ManyToManyField('Endereco', verbose_name='Nome da rua e número da empresa')
    observacao = models.TextField(max_length=255, blank=True, null=True, verbose_name='Observação')


    def Nome_e_numero_da_empresa(self):
        return ",".join([str(p) for p in self.fk_endereco.all()])