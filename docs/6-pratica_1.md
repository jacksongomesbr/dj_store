# Prática 1

## Parte 1

Criar uma view para representar a página "lista de produtos pública", que apresenta uma lista dos produtos contendo:

* uma foto (pode ser a primeira, se houver, ou uma imagem padrão, caso contrário)
* o nome do produto
* o nome da categoria do produto
* o preço do produto

A página deve ser de acesso público, ou seja, não deve solicitar autenticação do usuário.

## Parte 2

Utilize o pacote [django-bootstrap4](https://github.com/zostera/django-bootstrap4) para melhorar a aparência da página "lista de produtos pública". O processo é mais ou menos o seguinte:

1. instalar o pacote `django-bootstrap4`
2. registrar o aplicativo `'bootstrap4'` na variável `INSTALLED_APPS` do módulo `settings` do projeto
3. utilizar as tags adequadas no template

**Exemplo do template:**

```html
{% load bootstrap4 %}
{% bootstrap_css %}
{% bootstrap_javascript jquery='full' %}

<div class="container">
    <h1>Produtos</h1>
    <p>Lista de produtos...</p>
</div>
```

Ainda, tente utilizar recursos do Bootstrap para apresentar todas as fotos do produto.
