from django.urls import path
from GDS.views import (
    FaqCreateView,
    IndexTemplateView
    , ClienteListView
    , ClienteUpdateView
    , ClienteCreateView
    , ClienteDeleteView
    , ClienteDetailView
    , ClientePDFDetailView
    , EnderecoListView
    , EnderecoUpdateView
    , EnderecoCreateView
    , EnderecoDeleteView
    , EnderecoDetailView
    , EnderecoPDFDetailView
    , FuncionarioListView
    , FuncionarioUpdateView
    , FuncionarioCreateView
    , FuncionarioDeleteView
    , FuncionarioDetailView
    , FuncionarioPDFDetailView
    , FuncaoListView
    , FuncaoUpdateView
    , FuncaoCreateView
    , FuncaoDeleteView
    , ProdutoListView
    , ProdutoUpdateView
    , ProdutoCreateView
    , ProdutoDeleteView
    , ProdutoDetailView
    , ProdutoPDFDetailView
    , VendaListView
    , VendaUpdateView
    , VendaCreateView
    , VendaDeleteView
    , VendaDetailView
    , VendaPDFDetailView
    , DespesaListView
    , DespesaUpdateView
    , DespesaCreateView
    , DespesaDeleteView
    , DespesaDetailView
    , DespesaPDFDetailView
    , FornecedorListView
    , FornecedorUpdateView
    , FornecedorCreateView
    , FornecedorDeleteView
    , FornecedorDetailView
    , FornecedorPDFDetailView
    , FaqListView
    # , FaqCreateView
)

app_name = 'GDS'

urlpatterns = [
    # GET /
    path('', IndexTemplateView.as_view(), name="index"),

    # GET listar/cliente
    path('listar/cliente', ClienteListView.as_view(), name="listar_cliente"),

    # GET/ atualizar/cliente/{pk}
    path('atualizar/cliente/<pk>', ClienteUpdateView.as_view(), name="atualizar_cliente"),
    
    # GET /cadastrar/cliente
    path('cadastrar/cliente', ClienteCreateView.as_view(), name="cadastrar_cliente"),

    # GET /deletar/cliente/{pk}
    path('deletar/cliente/<pk>', ClienteDeleteView.as_view(), name="deletar_cliente"),

    # GET /detalhe/cliente/{pk}
    path('detalhe/cliente/<pk>', ClienteDetailView.as_view(), name="detalhe_cliente"),

    # GET /pdf/cliente/{pk}
    path('pdf/cliente/<pk>', ClientePDFDetailView.as_view(), name="pdf_cliente"),

    # GET listar/endereco
    path('listar/endereco', EnderecoListView.as_view(), name="listar_endereco"),

    # GET/ atualizar/endereco/{pk}
    path('atualizar/endereco/<pk>', EnderecoUpdateView.as_view(), name="atualizar_endereco"),
    
    # GET /cadastrar/endereco
    path('cadastrar/endereco', EnderecoCreateView.as_view(), name="cadastrar_endereco"),

    # GET /deletar/endereco/{pk}
    path('deletar/endereco/<pk>', EnderecoDeleteView.as_view(), name="deletar_endereco"),

    # GET /detalhe/endereco/{pk}
    path('detalhe/endereco/<pk>', EnderecoDetailView.as_view(), name="detalhe_endereco"),

    # GET /pdf/endereco/{pk}
    path('pdf/endereco/<pk>', EnderecoPDFDetailView.as_view(), name="pdf_endereco"),

    # GET listar/funcionario
    path('listar/funcionario', FuncionarioListView.as_view(), name="listar_funcionario"),

    # GET/ atualizar/funcionario/{pk}
    path('atualizar/funcionario/<pk>', FuncionarioUpdateView.as_view(), name="atualizar_funcionario"),
    
    # GET /cadastrar/funcionario
    path('cadastrar/funcionario', FuncionarioCreateView.as_view(), name="cadastrar_funcionario"),

    # GET /deletar/funcionario/{pk}
    path('deletar/funcionario/<pk>', FuncionarioDeleteView.as_view(), name="deletar_funcionario"),

    # GET /detalhe/funcionario/{pk}
    path('detalhe/funcionario/<pk>', FuncionarioDetailView.as_view(), name="detalhe_funcionario"),

    # GET /pdf/endereco/{pk}
    path('pdf/endereco/<pk>', FuncionarioPDFDetailView.as_view(), name="pdf_funcionario"),

    # # GET listar/funcao
    path('listar/funcao', FuncaoListView.as_view(), name="listar_funcao"),

    # # GET/ atualizar/funcao/{pk}
    path('atualizar/funcao/<pk>', FuncaoUpdateView.as_view(), name="atualizar_funcao"),
    
    # # GET /cadastrar/funcao
    path('cadastrar/funcao', FuncaoCreateView.as_view(), name="cadastrar_funcao"),

    # # GET /deletar/funcao/{pk}
    path('deletar/funcao/<pk>', FuncaoDeleteView.as_view(), name="deletar_funcao"),

    # GET listar/produto
    path('listar/produto', ProdutoListView.as_view(), name="listar_produto"),

    # GET/ atualizar/produto/{pk}
    path('atualizar/produto/<pk>', ProdutoUpdateView.as_view(), name="atualizar_produto"),
    
    # GET /cadastrar/produto
    path('cadastrar/produto', ProdutoCreateView.as_view(), name="cadastrar_produto"),

    # GET /deletar/produto/{pk}
    path('deletar/produto/<pk>', ProdutoDeleteView.as_view(), name="deletar_produto"),

    # GET /detalhe/produto/{pk}
    path('detalhe/produto/<pk>', ProdutoDetailView.as_view(), name="detalhe_produto"),

    # GET /pdf/produto/{pk}
    path('pdf/produto/<pk>', ProdutoPDFDetailView.as_view(), name="pdf_produto"),
    
    # GET listar/venda
    path('listar/venda', VendaListView.as_view(), name="listar_venda"),

    # GET/ atualizar/venda/{pk}
    path('atualizar/venda/<pk>', VendaUpdateView.as_view(), name="atualizar_venda"),
    
    # GET /cadastrar/venda
    path('cadastrar/venda', VendaCreateView.as_view(), name="cadastrar_venda"),

    # GET /deletar/venda/{pk}
    path('deletar/venda/<pk>', VendaDeleteView.as_view(), name="deletar_venda"),

    # GET /detalhe/venda/{pk}
    path('detalhe/venda/<pk>', VendaDetailView.as_view(), name="detalhe_venda"),

    # GET /pdf/venda/{pk}
    path('pdf/venda/<pk>', VendaPDFDetailView.as_view(), name="pdf_venda"),
    
    # GET listar/despesa
    path('listar/despesa', DespesaListView.as_view(), name="listar_despesa"),

    # GET/ atualizar/despesa/{pk}
    path('atualizar/despesa/<pk>', DespesaUpdateView.as_view(), name="atualizar_despesa"),
    
    # GET /cadastrar/despesa
    path('cadastrar/despesa', DespesaCreateView.as_view(), name="cadastrar_despesa"),

    # GET /deletar/despesa/{pk}
    path('deletar/despesa/<pk>', DespesaDeleteView.as_view(), name="deletar_despesa"),

    # GET /detalhe/despesa/{pk}
    path('detalhe/despesa/<pk>', DespesaDetailView.as_view(), name="detalhe_despesa"),

    # GET /pdf/despesa/{pk}
    path('pdf/despesa/<pk>', DespesaPDFDetailView.as_view(), name="pdf_despesa"),

    # GET listar/fornecedor
    path('listar/fornecedor', FornecedorListView.as_view(), name="listar_fornecedor"),

    # GET/ atualizar/fornecedor/{pk}
    path('atualizar/fornecedor/<pk>', FornecedorUpdateView.as_view(), name="atualizar_fornecedor"),
    
    # GET /cadastrar/fornecedor
    path('cadastrar/fornecedor', FornecedorCreateView.as_view(), name="cadastrar_fornecedor"),

    # GET /deletar/fornecedor/{pk}
    path('deletar/fornecedor/<pk>', FornecedorDeleteView.as_view(), name="deletar_fornecedor"),

    # GET /detalhe/fornecedor/{pk}
    path('detalhe/fornecedor/<pk>', FornecedorDetailView.as_view(), name="detalhe_fornecedor"),

    # GET /pdf/fornecedor/{pk}
    path('pdf/fornecedor/<pk>', FornecedorPDFDetailView.as_view(), name="pdf_fornecedor"),

    # GET /faq
    path('faq', FaqListView.as_view(), name="listar_faq"),

    # GET /faq/cadastrar
    # path('faq/cadastrar', FaqCreateView.as_view(), name="cadastrar_faq"),
]
