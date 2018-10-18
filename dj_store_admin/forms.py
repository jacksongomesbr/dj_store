from django import forms
from .models import *


class ComprarProdutoForm(forms.Form):
    produto_id = forms.IntegerField(required=True, widget=forms.HiddenInput())
    quantidade = forms.IntegerField()

    def clean(self):
        dados = super().clean()
        produto_id = dados.get('produto_id', None)
        quantidade = dados.get('quantidade', None)
        if not produto_id:
            raise forms.ValidationError('Produto não informado')
        if not Produto.objects.filter(pk=produto_id).exists():
            raise forms.ValidationError('Produto não existe')
        if not quantidade:
            self.add_error(
                'quantidade', 'Informe a quantidade de unidades para comprar')
        if quantidade == 0:
            self.add_error(
                'quantidade', 'A quantidade não pode ser igual a zero')
        if quantidade > 10:
            self.add_error(
                'quantidade', 'Não é permitido comprar mais de 10 unidades do produto')
        return dados
