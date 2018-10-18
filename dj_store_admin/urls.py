from django.urls import path
from .views import *

app_name = 'dj_store_admin'

urlpatterns = [
    path('categorias/', categoriadeproduto_list, name='categoriadeproduto_list'),
    path('categorias/<id>/', categoriadeproduto_detalhes, name='categoriadeproduto_detalhes'),
    path('produtos/<id>/', produto_detalhes, name='produto_detalhes'),
    path('carrinho/', carrinho_detalhes, name='carrinho_detalhes'),
]
