from django.db import models
from django.shortcuts import render
from django.views.generic import TemplateView, ListView, UpdateView, CreateView, DeleteView, DetailView
from .models import Cliente, Endereco, Funcionario, Funcao, Cadastrar_produto, Venda, Despesa, Fornecedore, Faq
from django.urls import reverse_lazy
from django.contrib import messages
from easy_pdf.views import PDFTemplateResponseMixin


# Create your views here.


# PÁGINA PRINCIPAL
# ----------------------------------------------

class IndexTemplateView(TemplateView):
    template_name = "index.html"


# LISTA DE ENDEREÇO
# ----------------------------------------------

class EnderecoListView(ListView):
    model = Endereco
    template_name = 'listar/endereco.html'
    context_object_name = "listar_endereco"
    paginate_by = 5


# CADASTRAMENTO DE ENDEREÇO
# ----------------------------------------------

class EnderecoCreateView(CreateView):
    model = Endereco
    template_name = "cadastrar/endereco.html"
    context_object_name = "cadastrar_endereco"
    fields = '__all__'


    def get_success_url(self):
        messages.success(self.request, 'Endereço cadastrado com sucesso!')
        return reverse_lazy('GDS:cadastrar_endereco')


# ATUALIZAÇÃO DE ENDEREÇO
# ----------------------------------------------

class EnderecoUpdateView(UpdateView):
    template_name = "atualizar/endereco.html"
    model = Endereco
    context_object_name = "atualizar_endereco"
    fields = '__all__'

    def get_success_url(self):
        messages.success(self.request, 'Endereço atualizado com sucesso!')
        return reverse_lazy("GDS:listar_endereco")
    

# EXCLUSÃO DE ENDEREÇO
# ----------------------------------------------

class EnderecoDeleteView(DeleteView):
    template_name = "deletar/endereco.html"
    model = Endereco
    fields = '__all__'
    context_object_name = 'deletar_endereco'

    def get_success_url(self):
        messages.success(self.request, 'Endereço deletado com sucesso!')
        return reverse_lazy("GDS:listar_endereco")


# DETALHE DE ENDEREÇO
# ----------------------------------------------

class EnderecoDetailView(DetailView):
    template_name = "detalhes/endereco.html"
    model = Endereco


# GERAR PDF DE CLIENTE
# ----------------------------------------------

class EnderecoPDFDetailView(PDFTemplateResponseMixin, DetailView):
    model = Endereco
    template_name = 'pdf/pdf_endereco.html'


# LISTA DE CLIENTE
# ----------------------------------------------

class ClienteListView(ListView):
    model = Cliente
    template_name = 'listar/cliente.html'
    context_object_name = "listar_cliente"
    paginate_by = 5


# CADASTRAMENTO DE CLIENTE
# ----------------------------------------------

class ClienteCreateView(CreateView):
    model = Cliente
    template_name = "cadastrar/cliente.html"
    context_object_name = "cadastrar_cliente"
    fields = '__all__'


    def get_success_url(self):
        messages.success(self.request, 'Cliente cadastrado com sucesso!')
        return reverse_lazy('GDS:cadastrar_cliente')


# ATUALIZAÇÃO DE CLIENTE
# ----------------------------------------------

class ClienteUpdateView(UpdateView):
    template_name = "atualizar/cliente.html"
    model = Cliente
    context_object_name = "atualizar_cliente"
    fields = '__all__'


    def get_success_url(self):
        messages.success(self.request, 'Cliente atualizado com sucesso!')
        return reverse_lazy("GDS:listar_cliente")
    

# EXCLUSÃO DE CLIENTE
# ----------------------------------------------

class ClienteDeleteView(DeleteView):
    template_name = "deletar/cliente.html"
    model = Cliente
    fields = '__all__'
    context_object_name = 'deletar_cliente'


    def get_success_url(self):
        messages.success(self.request, 'Cliente deletado com sucesso!')
        return reverse_lazy("GDS:listar_cliente")


# DETALHE DE CLIENTE
# ----------------------------------------------

class ClienteDetailView(DetailView):
    template_name = "detalhes/cliente.html"
    model = Cliente


# GERAR PDF DE CLIENTE
# ----------------------------------------------

class ClientePDFDetailView(PDFTemplateResponseMixin, DetailView):
    model = Cliente
    template_name = 'pdf/pdf_cliente.html'


# LISTA DE FUNCIONÁRIO
# ----------------------------------------------

class FuncionarioListView(ListView):
    model = Funcionario
    template_name = 'listar/funcionario.html'
    context_object_name = "listar_funcionario"
    paginate_by = 5


# CADASTRAMENTO DE FUNCIONÁRIO
# ----------------------------------------------

class FuncionarioCreateView(CreateView):
    model = Funcionario
    template_name = "cadastrar/funcionario.html"
    context_object_name = "cadastrar_funcionario"
    fields = '__all__'


    def get_success_url(self):
        messages.success(self.request, 'Funcionario cadastrado com sucesso!')
        return reverse_lazy('GDS:cadastrar_funcionario')


# ATUALIZAÇÃO DE FUNCIONÁRIO
# ----------------------------------------------

class FuncionarioUpdateView(UpdateView):
    template_name = "atualizar/funcionario.html"
    model = Funcionario
    context_object_name = "atualizar_funcionario"
    fields = '__all__'


    def get_success_url(self):
        messages.success(self.request, 'Funcionario atualizado com sucesso!')
        return reverse_lazy("GDS:listar_funcionario")


# EXCLUSÃO DE FUNCIONÁRIO
# ----------------------------------------------

class FuncionarioDeleteView(DeleteView):
    template_name = "deletar/funcionario.html"
    model = Funcionario
    fields = '__all__'
    context_object_name = 'deletar_funcionario'


    def get_success_url(self):
        messages.success(self.request, 'Funcionario deletado com sucesso!')
        return reverse_lazy("GDS:listar_funcionario")


# DETALHE DE FUNCIONÁRIO
# ----------------------------------------------

class FuncionarioDetailView(DetailView):
    template_name = "detalhes/funcionario.html"
    model = Funcionario


# GERAR PDF DE FUNCIONÁRIO
# ----------------------------------------------

class FuncionarioPDFDetailView(PDFTemplateResponseMixin, DetailView):
    model = Funcionario
    template_name = 'pdf/pdf_funcionario.html'


# # LISTA DE CARGOS
# # ----------------------------------------------

class FuncaoListView(ListView):
    model = Funcao
    template_name = 'listar/funcao.html'
    context_object_name = "listar_funcao"
    paginate_by = 5


# # CADASTRAMENTO DE CARGOS
# # ----------------------------------------------

class FuncaoCreateView(CreateView):
    model = Funcao
    template_name = "cadastrar/funcao.html"
    context_object_name = "cadastrar_funcao"
    fields = '__all__'


    def get_success_url(self):
        messages.success(self.request, 'Cargo cadastrado com sucesso!')
        return reverse_lazy('GDS:cadastrar_funcao')


# # ATUALIZAÇÃO DE CARGOS
# # ----------------------------------------------

class FuncaoUpdateView(UpdateView):
    template_name = "atualizar/funcao.html"
    model = Funcao
    context_object_name = "atualizar_funcao"
    fields = '__all__'

    def get_success_url(self):
        messages.success(self.request, 'Cargo atualizado com sucesso!')
        return reverse_lazy('GDS:listar_funcao')


# # EXCLUSÃO DE CARGOS
# # ----------------------------------------------

class FuncaoDeleteView(DeleteView):
    template_name = "deletar/funcao.html"
    model = Funcao
    fields = '__all__'
    context_object_name = 'deletar_funcao'
    
    
    def get_success_url(self):
        messages.success(self.request, 'Cargo deletado com sucesso!')
        return reverse_lazy('GDS:listar_funcao')


# LISTA DE PRODUTO
# ----------------------------------------------

class ProdutoListView(ListView):
    model = Cadastrar_produto
    template_name = 'listar/produto.html'
    context_object_name = "listar_produto"
    paginate_by = 5


# CADASTRAMENTO DE PRODUTO
# ----------------------------------------------

class ProdutoCreateView(CreateView):
    model = Cadastrar_produto
    template_name = "cadastrar/produto.html"
    context_object_name = "cadastrar_produto"
    fields = '__all__'


    def get_success_url(self):
        messages.success(self.request, 'Produto cadastrado com sucesso!')
        return reverse_lazy('GDS:cadastrar_produto')


# ATUALIZAÇÃO DE PRODUTO
# ----------------------------------------------

class ProdutoUpdateView(UpdateView):
    template_name = "atualizar/produto.html"
    model = Cadastrar_produto
    context_object_name = "atualizar_produto"
    fields = '__all__'


    def get_success_url(self):
        messages.success(self.request, 'Produto atualizado com sucesso!')
        return reverse_lazy("GDS:listar_produto")


# EXCLUSÃO DE PRODUTO
# ----------------------------------------------

class ProdutoDeleteView(DeleteView):
    template_name = "deletar/produto.html"
    model = Cadastrar_produto
    fields = '__all__'
    context_object_name = 'deletar_produto'
    

    def get_success_url(self):
        messages.success(self.request, 'Produto deletado com sucesso!')
        return reverse_lazy("GDS:listar_produto")

    
# DETALHE DE PRODUTO
# ----------------------------------------------

class ProdutoDetailView(DetailView):
    template_name = "detalhes/produto.html"
    model = Cadastrar_produto


# GERAR PDF DE PRODUTO
# ----------------------------------------------

class ProdutoPDFDetailView(PDFTemplateResponseMixin, DetailView):
    model = Cadastrar_produto
    template_name = 'pdf/pdf_produto.html'


# LISTA DE VENDAS
# ----------------------------------------------

class VendaListView(ListView):
    model = Venda
    template_name = 'listar/venda.html'
    context_object_name = "listar_venda"
    paginate_by = 5


# CADASTRAMENTO DE VENDAS
# ----------------------------------------------

class VendaCreateView(CreateView):
    model = Venda
    template_name = "cadastrar/venda.html"
    context_object_name = "cadastrar_venda"
    fields = '__all__'


    def get_success_url(self):
        messages.success(self.request, 'Venda cadastrado com sucesso!')
        return reverse_lazy('GDS:cadastrar_venda')


# ATUALIZAÇÃO DE VENDAS
# ----------------------------------------------

class VendaUpdateView(UpdateView):
    template_name = "atualizar/venda.html"
    model = Venda
    context_object_name = "atualizar_venda"
    fields = '__all__'


    def get_success_url(self):
        messages.success(self.request, 'Venda atualizada com sucesso!')
        return reverse_lazy("GDS:listar_venda")


# EXCLUSÃO DE VENDAS
# ----------------------------------------------

class VendaDeleteView(DeleteView):
    template_name = "deletar/venda.html"
    model = Venda
    fields = '__all__'
    context_object_name = 'deletar_venda'
    
    
    def get_success_url(self):
        messages.success(self.request, 'Venda deletado com sucesso!')
        return reverse_lazy("GDS:listar_venda")

    
# DETALHE DE VENDAS
# ----------------------------------------------

class VendaDetailView(DetailView):
    template_name = "detalhes/venda.html"
    model = Venda


# GERAR PDF DE VENDAS
# ----------------------------------------------

class VendaPDFDetailView(PDFTemplateResponseMixin, DetailView):
    model = Venda
    template_name = 'pdf/pdf_venda.html'


# LISTA DE DESPESA
# ----------------------------------------------

class DespesaListView(ListView):
    model = Despesa
    template_name = 'listar/despesa.html'
    context_object_name = "listar_despesa"
    paginate_by = 5


# CADASTRAMENTO DE DESPESA
# ----------------------------------------------

class DespesaCreateView(CreateView):
    model = Despesa
    template_name = "cadastrar/despesa.html"
    context_object_name = "cadastrar_despesa"
    fields = '__all__'


    def get_success_url(self):
        messages.success(self.request, 'Despesa cadastrado com sucesso!')
        return reverse_lazy('GDS:cadastrar_despesa')


# ATUALIZAÇÃO DE DESPESA
# ----------------------------------------------

class DespesaUpdateView(UpdateView):
    template_name = "atualizar/despesa.html"
    model = Despesa
    context_object_name = "atualizar_despesa"
    fields = '__all__'


    def get_success_url(self):
        messages.success(self.request, 'Despesa atualizada com sucesso!')
        return reverse_lazy("GDS:listar_despesa")


# EXCLUSÃO DE DESPESA
# ----------------------------------------------

class DespesaDeleteView(DeleteView):
    template_name = "deletar/despesa.html"
    model = Despesa
    fields = '__all__'
    context_object_name = 'deletar_despesa'
    
    
    def get_success_url(self):
        messages.success(self.request, 'Despesa deletada com sucesso!')
        return reverse_lazy("GDS:listar_despesa")


# DETALHE DE DESPESA
# ----------------------------------------------

class DespesaDetailView(DetailView):
    template_name = "detalhes/despesa.html"
    model = Despesa


# GERAR PDF DE DESPESA
# ----------------------------------------------

class DespesaPDFDetailView(PDFTemplateResponseMixin, DetailView):
    model = Despesa
    template_name = 'pdf/pdf_despesa.html'


# LISTA DE FORNECEDOR
# ----------------------------------------------

class FornecedorListView(ListView):
    model = Fornecedore
    template_name = 'listar/fornecedor.html'
    context_object_name = "listar_fornecedor"
    paginate_by = 5


# CADASTRAMENTO DE FORNECEDOR
# ----------------------------------------------

class FornecedorCreateView(CreateView):
    model = Fornecedore
    template_name = "cadastrar/fornecedor.html"
    context_object_name = "cadastrar_fornecedor"
    fields = '__all__'


    def get_success_url(self):
        messages.success(self.request, 'Fornecedor cadastrado com sucesso!')
        return reverse_lazy('GDS:cadastrar_fornecedor')


# ATUALIZAÇÃO DE FORNECEDOR
# ----------------------------------------------

class FornecedorUpdateView(UpdateView):
    template_name = "atualizar/fornecedor.html"
    model = Fornecedore
    context_object_name = "atualizar_fornecedor"
    fields = '__all__'


    def get_success_url(self):
        messages.success(self.request, 'Fornecedor atualizado com sucesso!')
        return reverse_lazy("GDS:listar_fornecedor")


# EXCLUSÃO DE FORNECEDOR
# ----------------------------------------------

class FornecedorDeleteView(DeleteView):
    template_name = "deletar/fornecedor.html"
    model = Fornecedore
    fields = '__all__'
    context_object_name = 'deletar_fornecedor'
    
    
    def get_success_url(self):
        messages.success(self.request, 'Fornecedor deletado com sucesso!')
        return reverse_lazy("GDS:listar_fornecedor")

    
# DETALHE DE FORNECEDOR
# ----------------------------------------------

class FornecedorDetailView(DetailView):
    template_name = "detalhes/fornecedor.html"
    model = Fornecedore


# GERAR PDF DE FORNECEDOR
# ----------------------------------------------

class FornecedorPDFDetailView(PDFTemplateResponseMixin, DetailView):
    model = Fornecedore
    template_name = 'pdf/pdf_fornecedor.html'


# LISTA DE FAQ
# ----------------------------------------------

class FaqListView(ListView):
    model = Faq
    template_name = 'listar/faq.html'
    context_object_name = "listar_faq"


# CADASTRO DE FAQ
# ----------------------------------------------

class FaqCreateView(CreateView):
    model = Faq
    template_name = 'cadastrar/faq.html'
    context_object_name = "cadastrar_faq"
    fields = '__all__'


    def get_success_url(self):
        messages.success(self.request, 'Fornecedor cadastrado com sucesso!')
        return reverse_lazy("GDS:listar_faq")
