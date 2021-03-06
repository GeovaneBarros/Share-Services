# Generated by Django 3.2.5 on 2021-08-10 13:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Contato',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('celular', models.CharField(max_length=16)),
                ('telefone', models.CharField(max_length=16, null=True)),
                ('email', models.EmailField(max_length=64)),
            ],
            options={
                'verbose_name': 'Contato',
                'verbose_name_plural': 'Contatos',
            },
        ),
        migrations.CreateModel(
            name='Endereco',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rua', models.CharField(max_length=64)),
                ('numero', models.CharField(max_length=8)),
                ('bairro', models.CharField(max_length=32)),
                ('cidade', models.CharField(max_length=32)),
            ],
            options={
                'verbose_name': 'Endereço',
                'verbose_name_plural': 'Endereços',
            },
        ),
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('ramo', models.CharField(max_length=100)),
                ('foto', models.ImageField(blank=True, null=True, upload_to='')),
                ('cnpj', models.CharField(blank=True, max_length=20, null=True)),
                ('premium', models.BooleanField(default=False)),
                ('contato', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.contato')),
                ('endereco', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.endereco')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Empresa',
                'verbose_name_plural': 'Empresas',
            },
        ),
        migrations.CreateModel(
            name='Descricao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('servicos', models.CharField(max_length=1024)),
                ('produtos', models.CharField(max_length=1024)),
                ('historia', models.CharField(max_length=512)),
                ('empresa', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='core.empresa')),
            ],
            options={
                'verbose_name': 'Descrição',
                'verbose_name_plural': 'Descrições',
            },
        ),
    ]
