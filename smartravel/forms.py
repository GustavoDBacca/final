from django import forms
from .models import Cidade, Local, Usuario, Categorias


class CadastroUsuarioForm(forms.ModelForm):
    senha = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Usuario
        fields = ['nome', 'doc', 'telefone', 'email', 'senha']

class CadastroLocalForm(forms.ModelForm):
    class Meta:
        model = Local
        cidade = forms.ModelChoiceField(queryset=Cidade.objects.all())
        fields = ['nome_local', 'descricao', 'cidade', 'bairro', 'rua', 'telefone', 'email', 'tipo']


        tipo = forms.ModelChoiceField(queryset=Categorias.objects.all(), empty_label=None, widget=forms.Select(attrs={'class': 'form-control'}))


class CadastroCidadeForm(forms.ModelForm):
    class Meta:
        model = Cidade
        fields = ['nome_cidade', 'descricao']