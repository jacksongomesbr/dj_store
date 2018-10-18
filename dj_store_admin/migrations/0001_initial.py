# Generated by Django 2.1.2 on 2018-10-17 03:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CategoriaDeProduto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=128)),
            ],
            options={
                'verbose_name': 'Categoria de produto',
                'verbose_name_plural': 'Categorias de produtos',
            },
        ),
    ]
