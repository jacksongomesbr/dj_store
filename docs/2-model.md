# Model

O fluxo de desenvolvimento do software começa pela implementação do model. Em termos práticos, o objetivo é criar classes no módulo `models` do aplicativo `dj_store_admin` utilizando os recursos do ORM do Django.

O **ORM** (*Oject-Relational Mapper*, ou *Mapeador Objeto-Relacional*) é responsável por fornecer os recursos para descrever o model de um software, converter objetos python para o banco de dados e vice-versa. A tarefa de *mapear* significa exatamente isso.

Descrever um model significa criar uma *classe e seus campos*, com o intuito de representar uma entidade do modelo de dados e seus relacionamentos.

## Categoria de produto

Vamos começar criando o model de uma entidade mais simples: `CategoriaDeProduto`.

Conforme o modelo de dados o model seria algo como o seguinte:

```python
from django.db import models

class CategoriaDeProduto(models.Model):
    class Meta:
        verbose_name = 'Categoria de produto'
        verbose_name_plural = 'Categorias de produtos'

    nome = models.CharField(max_length=128)

    def __str__(self):
        return self.nome
```

O pacote `django.db.models` fornece a classe `Model`, que é utilizada como superclasse para toda classe do model (a classe `CategoriaDeProduto` herda de `Model`). A classe interna `Meta` é utilizada para determinar características importantes do model. Nesse caso os atributos `verbose_name` e `verbose_name_plural` definem, respectivamente, o nome literal no singular e o nome literal no plural.

A classe `CategoriaDeProduto` possui o campo `nome`, do tipo `CharField`. A maior parte do trabalho de criar classes do model tem relação com escrever campos e utilizar corretamente os tipos de campos do Django.

A classe também declara o método `__str__()`, que retorna uma string que representa uma *instância* da classe.

Depois de criar a classe o próximo passo é criar um **arquivo de migração**, uma espécie de descrição detalhada (em python) do que o Django deve fazer para criar uma tabela (ou mais) no banco de dados para representar o model.

**Observação**: o banco de dados padrão do projeto Django é um arquivo do SQLite (`db.sqlite3`). Entretanto, é possível alterar para outro SGBD mais robusto (como Microsoft SQL Server, Oracle, PostgreSQL ou MySQL) sem ter que escrever qualquer código específico para o banco de dados. Esse é um benefício importante de utilizar ORM.

Para criar o arquivo de migração execute o comando:

```
python manage.py makemigrations dj_store_admin
```

A última parte do comando (`dj_store_admin`) pode ser omitida para que o Django descubra, por si só, para quais aplicativos deve criar o arquivo de migração.

Depois, é necessário executar a migração, usando o comando:

```
python manage.py migrate dj_store_admin
```

**Observação**: se for a primeira vez em que estiver executando o comando `migrate` é importante omitir a especificação do aplicativo para que o Django execute as migrações de outros aplicativos (como o `django admin`). Além disso, também é importante criar o **super-usuário** para a *interface de administração*. Isso é feito executando o comando `python manage.py createsuperuser` e seguindo as intruções apresentadas na tela.

Ao executar o comando `migrate` é criado o arquivo `0001_initial.py` na pasta `dj_store_admin/migrations`. Esse arquivo python descreve o que o Django precisa fazer para criar a tabela relacionada à classe `CategoriaDeProduto` do model e seus campos. O número com quatro algarismos no início do arquivo funciona como um identificador do arquivo de migração. Ou seja, o arquivo em questão é identificado pelo número `0001`.

Sempre que modificar uma classe do model, repita o processo:

1. criar o arquivo de migração
2. executar a migração

