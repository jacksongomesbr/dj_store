from django.db import models

# Create your models here.


class CategoriaDeProduto(models.Model):
    class Meta:
        verbose_name = 'Categoria de produto'
        verbose_name_plural = 'Categorias de produtos'

    nome = models.CharField(max_length=128)

    def __str__(self):
        return self.nome


class Produto(models.Model):
    nome = models.CharField(max_length=128)
    descricao = models.TextField('Descrição')
    categoria = models.ForeignKey(
        CategoriaDeProduto, on_delete=models.CASCADE, related_name='produtos')
    preco = models.FloatField('Preço')

    def __str__(self):
        return self.nome

    @property
    def foto_da_capa(self):
        if self.fotos.count() == 0:
            return None
        return self.fotos.all()[0]


class FotoDeProduto(models.Model):
    class Meta:
        verbose_name = 'Foto de produto'
        verbose_name_plural = 'Fotos de produtos'

    produto = models.ForeignKey(
        Produto, on_delete=models.CASCADE, related_name='fotos')
    arquivo = models.FileField()

    def __str__(self):
        return self.arquivo.name
