from django.db import models


class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=254, verbose_name='Nome Completo')
    doc = models.CharField(max_length=11, verbose_name='CPF', unique=True)
    telefone = models.CharField(max_length=254, verbose_name='Telefone', blank=True)
    email = models.EmailField(max_length=254, verbose_name='E-mail', blank=True)
    senha = models.CharField(max_length=254, verbose_name='Senha')

    def __str__(self):
        return self.nome


class Agencia(models.Model):
    nome = models.CharField(max_length=254, verbose_name='Nome Fantasia')
    doc = models.CharField(max_length=14, verbose_name='CNPJ', unique=True)
    telefone = models.CharField(max_length=11, verbose_name='Telefone', blank=True)
    email = models.EmailField(max_length=254, verbose_name='E-mail', blank=True)
    senha = models.CharField(max_length=254, verbose_name='Senha')

    def __str__(self):
        return self.nome
    

class Cidade(models.Model):
    nome_cidade = models.SlugField(max_length=254, verbose_name='cidade', unique=True)
    descricao = models.TextField(verbose_name='descrição')

    def __str__(self):
        return self.nome_cidade


class Categorias(models.Model):
    id_categorias = models.AutoField(primary_key=True)
    categorias = models.CharField(max_length=100)
    
    def __str__(self):
        return self.categorias  
  

class Local(models.Model):
    nome_local = models.CharField(max_length=254, verbose_name='Nome do Local')
    descricao = models.CharField(max_length=254, verbose_name='Descrição')
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE, related_name='local')
    bairro = models.CharField(max_length=254, verbose_name='Bairro')
    rua = models.CharField(max_length=254, verbose_name='Rua')
    telefone = models.CharField(max_length=14, verbose_name='Telefone', blank=True)
    email = models.EmailField(max_length=254, verbose_name='Email', blank=True)
    tipo = models.ForeignKey(Categorias, on_delete=models.CASCADE, null=True, blank=True, related_name='locais')
