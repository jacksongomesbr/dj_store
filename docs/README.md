# Introdução

**dj_store** é um software web para gerenciamento de uma loja. Não é um software completo porque é utilizado como base para um curso de desenvolvimento de software web com django, ministrado por @jacksongomesbr.

Esta documentação apresenta informações sobre o desenvolvimento desse software e conceitos de desenvolvimento de software django.

## Django

**Django** é um framework de desenvolvimento de software web para Python e é desenvolvido com base no padrão arquitetural **MVC** (model-view-controller). O **model** representa a estrutura dos dados; a **view** representa a interface gráfica e o **controller** representa a lógica de negócio.

Na prática, esses elementos, com exceção do model, estão representados no Django de uma maneira um pouco diferente:

* **view**: representa a lógica de negócio
* **template**: representa a interface gráfica

Por isso o padrão arquitetural também pode ser considerado como **MTV** (model-template-view).

## Ambiente virtual do python (virtualenv)

É importante desenvolver o software Django utilizando um ambiente virtual como forma de separar as dependências (pacotes) de outros projetos. 

Para fazer isso, na pasta do projeto, execute:

```
python -m venv venv
```

O comando cria um diretório `venv`, que representa o virtualenv do projeto.

A partir disso, ative o ambiente utilizando o comando conforme o sistema operacional:

* **linux e MacOS**: `$ source venv/bin/activate`
* **windows**: `# venv\Scripts\activate`

Ao ativar o virtualenv é criado um prompt com a identificação do mesmo, mais ou menos assim:

```
(venv) c:\dj_store
```

A partir disso, execute todos os comandos deste referencial no prompt criado para o virtualenv e dentro da pasta do projeto.

## Pacote python

O Django é disponibilizado como um pacote python e, por isso, é necessário instalá-lo. Isso pode ser feito com o programa **pip**:

```
pip install django
```

## Projeto e aplicativo

Um software django é organizado em projeto (somente um) e aplicativos (zero ou mais).

### Estrutura do projeto

Um **projeto** é uma parte fundamental do software Django. Ele reúne os arquivos que realizam a configuração do projeto, sua execução e URLs.

Há uma pasta com o nome do projeto (ex: `dj_store_project`) e, dentro dela, os arquivos:

* `__init__.py`: indica que a pasta representa um pacote python
* `settings.py`: contém as configurações do projeto
* `urls.py`: contém as URLs do projeto
* `wsgi.py`: contém a configuração de execução do projeto

No contexto do python cada arquivo `.py` em um pacote é chamado de **módulo**. Portanto, o módulo **settings** do `dj_store_project` refere-se ao arquivo `dj_store_project/settings.py`.

Além disso, fora dessa pasta (ou seja, na pasta pai) há o arquivo `manage.py`, que executa comandos do Django no projeto.

### Estrutura do aplicativo

Um **aplicativo** contém lógica e funcionalidades específicas de uma parte do software. É comum utilizar aplicativos como forma de organizar a estrutura do projeto em partes menores.

Há uma pasta para o aplicativo (ex: `dj_store_admin`) e, dentro dela, os arquivos:

* `__init__.py`: indica que a pasta representa um pacote python
* `admin.py`: contém os recursos de gerenciamento de dados do projeto, utilizando o pacote `django-admin` (mais sobre isso adiante)
* `apps.py`: contém configurações do projeto
* `models.py`: contém os models
* `tests.py`: contém os testes unitários
* `views.py`: contém as views
* `migrations`: pasta que contém as **migrations** (veremos isso mais à frente)

Cada aplicativo deve ser instalado no projeto, modificando a variável `INSTALLED_APPS` do módulo `settings` do `dj_store_project`:

```
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'dj_store_admin'
]
```

O trecho de código anterior apresenta, nas primeiras seis linhas, os aplicativos Django instalados por padrão. A última linha indica a instalação do aplicativo `dj_store_admin`.

## Executando o projeto

Para executar o projeto utiliza-se o comando:

```
python manage.py runserver
```

O comando inicia um **servidor web** de desenvolvimento (ou local) e disponibiliza o software no endereço `http://localhost:8000`.

## Material de referência

A maior parte deste material foi escrita com base na **Documentação do Django**, disponível online: https://docs.djangoproject.com/en/2.1/. Se preferir utilize a variante em português: https://docs.djangoproject.com/pt-br/2.1/.

Outro material de referência é o livro gratuito **Desenvolvimento web com Django**, de Jackson Gomes de Souza, disponível online (incluindo código-fonte) em: https://github.com/jacksongomesbr/djangobook-project/. Na pasta `output` há o arquivo `livro.pdf`, que representa a última versão do livro para leitura.
