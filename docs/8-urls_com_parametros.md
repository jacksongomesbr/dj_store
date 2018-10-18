# URLs com parâmetros

A página *lista de categorias de produtos* apresenta a lista das categorias de produtos. É interessante ter também uma página *detalhes da categoria de produto*, que apresenta o nome da categoria de produto e a lista de produtos dessa categoria. Para fazer isso é necessário utilizar **parâmetros de URL**. 

O código a seguir apresenta o módulo `urls` do aplicativo `dj_store_admin`:

```python
from django.urls import path
from .views import *

app_name = 'dj_store_admin'

urlpatterns = [
    path('categorias/', categoriadeproduto_list, name='categoriadeproduto_list'),
    path('categorias/<id>/', categoriadeproduto_detalhes, name='categoriadeproduto_detalhes'),
]
```

O segundo elemento da lista `urlpatterns` representa um padrão de URL cujo caminho tem a seguinte representação: `categorias/<id>/`. A presença da sintaxe `<nome>` define um parâmetro de URL onde `nome` representa o nome ou identificador do parâmetro.

Utilizar parâmetros de URL permite que a view baseada em função tenha parâmetros além do `request`. A seguir o código da view `categoriadeproduto_detalhes()`:

```python
def categoriadeproduto_detalhes(request, id):
    try:
        categoria = CategoriaDeProduto.objects.get(pk=id)
    except CategoriaDeProduto.DoesNotExist:
        return Http404('Esta categoria não foi encontrada')
    return render(request, 'dj_store_admin/categoriadeproduto_detalhes.html', {'categoria': categoria})
```

A função `categoriadeproduto_detalhes()` tem o parâmetro `id`, que está relacionado ao parâmetro de URL de mesmo nome -- isso é necessário. O código utiliza o método `get()` do manager de `CategoriaDeProduto` para localizar uma categoria de produto pelo seu identificador. Se não encontrar, a view retorna uma exceção do tipo `Http404`, que representa um código de erro de página não encontrada.
