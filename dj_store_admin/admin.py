from django.contrib import admin
from django.utils.html import format_html
from .models import *

# Register your models here.


@admin.register(CategoriaDeProduto)
class CategoriaDeProdutoAdmin(admin.ModelAdmin):
    pass


class FotoDeProdutoInline(admin.TabularInline):
    model = FotoDeProduto
    extra = 1


class IntervaloDePrecoDeProdutoListFilter(admin.SimpleListFilter):
    title = 'Intervalo de preços'
    parameter_name = 'intervalo_de_preco'

    def lookups(self, request, model_admin):
        return (
            ('0-100', 'Até R$ 100,00'),
            ('100-300', 'Entre R$ 100,00 e R$ 300,00'),
            ('300-500', 'Entre R$ 300,00 e R$ 500,00'),
            ('500-1000', 'Entre R$ 500,00 e R$ 1.000,00'),
            ('1000-2000', 'Entre R$ 1.000,00 e R$ 2.000,00'),
            ('2000-', 'Acima de R$ 2.000,00')
        )

    def queryset(self, request, queryset):
        if self.value() == '0-100':
            return queryset.filter(preco__lte=100)
        if self.value() == '100-300':
            return queryset.filter(preco__gt=100, preco__lte=300)
        if self.value() == '300-500':
            return queryset.filter(preco__gt=300, preco__lte=500)
        if self.value() == '500-1000':
            return queryset.filter(preco__gt=500, preco__lte=1000)
        if self.value() == '1000-2000':
            return queryset.filter(preco__gt=1000, preco__lte=2000)
        if self.value() == '2000-':
            return queryset.filter(preco__gt=2000)


@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    inlines = (FotoDeProdutoInline, )
    list_select_related = ('categoria', )
    list_display = ('foto', 'nome', 'categoria', 'preco')
    list_display_links = list_display
    list_filter = ('categoria', IntervaloDePrecoDeProdutoListFilter)
    list_per_page = 25
    ordering = ('categoria', 'nome')
    raw_id_fields = ('categoria', )
    search_fields = ('categoria__nome', 'nome', 'descricao')

    def foto(self, obj):
        imagem = obj.foto_da_capa
        return format_html('<img src="{}" width="50" height="50">',
                           imagem.arquivo.url if imagem else 'https://via.placeholder.com/50'
                           )
    foto.short_description = 'Foto'
