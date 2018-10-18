# Generated by Django 2.1.2 on 2018-10-17 04:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dj_store_admin', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FotoDeProduto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('arquivo', models.FileField(upload_to='')),
            ],
            options={
                'verbose_name': 'Foto de produto',
                'verbose_name_plural': 'Fotos de produtos',
            },
        ),
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=128)),
                ('descricao', models.TextField(verbose_name='Descrição')),
                ('preco', models.FloatField(verbose_name='Preço')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='produtos', to='dj_store_admin.CategoriaDeProduto')),
            ],
        ),
        migrations.AddField(
            model_name='fotodeproduto',
            name='produto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fotos', to='dj_store_admin.Produto'),
        ),
    ]
