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