from django.shortcuts import render, redirect
from django.http import Http404
from django.urls import reverse
from .models import *
from .forms import *
# Create your views here.


def categoriadeproduto_list(request):
    categorias = CategoriaDeProduto.objects.all()
    return render(request, 'dj_store_admin/categoriadeproduto_list.html', {'categorias': categorias})


def categoriadeproduto_detalhes(request, id):
    try:
        categoria = CategoriaDeProduto.objects.get(pk=id)
    except CategoriaDeProduto.DoesNotExist:
        return Http404('Esta categoria não foi encontrada')
    return render(request, 'dj_store_admin/categoriadeproduto_detalhes.html', {'categoria': categoria})


def produto_detalhes(request, id):
    try:
        produto = Produto.objects.get(pk=id)
    except Produto.DoesNotExist:
        return Http404('O produto não foi encontrado')
    if request.method == 'GET':
        form = ComprarProdutoForm(initial={'produto_id': produto.id})
    if request.method == 'POST':
        form = ComprarProdutoForm(request.POST)
        if form.is_valid():
            carrinho = request.session.get('carrinho', {})
            dados = form.clean()
            produto_id = str(produto.id)
            if produto_id in carrinho:
                carrinho[produto_id]['quantidade'] += dados['quantidade']
                carrinho[produto_id]['preco_total'] = carrinho[produto_id]['preco_unitario'] * \
                    carrinho[produto_id]['quantidade']
            else:
                carrinho[produto_id] = {
                    'quantidade': dados['quantidade'],
                    'nome': produto.nome,
                    'preco_unitario': produto.preco,
                    'preco_total': produto.preco
                }
            request.session['carrinho'] = carrinho
            return redirect(reverse('dj_store_admin:carrinho_detalhes'))
    return render(request, 'dj_store_admin/produto_detalhes.html',
                  {'form': form, 'produto': produto})


def carrinho_detalhes(request):
    carrinho = request.session.get('carrinho', {})
    preco_total = 0
    for produto_id in carrinho:
        preco_total += carrinho[produto_id]['preco_total']
    if request.method == 'POST':
        acao = request.POST.get('acao', None)
        if acao == 'excluir':
            produto_id = request.POST.get('produto_id', None)
            if produto_id in carrinho:
                carrinho.pop(produto_id, None)
                request.session['carrinho'] = carrinho
    return render(request, 'dj_store_admin/carrinho.html', {'carrinho': carrinho, 'preco_total': preco_total})


def carrinho_limpar(request):
    request.session.flush()
    return redirect(reverse('dj_store_admin:categoriadeproduto_list'))
