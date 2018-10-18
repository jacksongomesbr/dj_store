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
    if request.method == 'GET':
        try:
            produto = Produto.objects.get(pk=id)
            form = ComprarProdutoForm(initial={'produto_id': produto.id})
        except Produto.DoesNotExist:
            return Http404('O produto não foi encontrado')
    if request.method == 'POST':
        form = ComprarProdutoForm(request.POST)
        if form.is_valid:
            carrinho = request.session.get('carrinho', [])
            dados = form.clean()
            carrinho.append(
                {'produto': form.cleaned_data['produto_id'],
                 'quantidade': form.cleaned_data['quantidade']})
            request.session['carrinho'] = carrinho
            return redirect(reverse('carrinho'))
    return render(request, 'dj_store_admin/produto_detalhes.html',
                  {'form': form, 'produto': produto})


def carrinho_detalhes(request):
    carrinho = request.session.get('carrinho', [])
    return render(request, 'dj_store_admin/carrinho.html', {'carrinho': carrinho})
