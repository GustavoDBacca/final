from msilib.schema import ListView
from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .forms import CadastroCidadeForm, CadastroLocalForm, CadastroUsuarioForm
# from .forms import CadastroUsuarioForm
from django.db.models import Q

from smartravel.models import Cidade, Local, Usuario


def home(request):
    cidades = Cidade.objects.all()
    print(request.user)
    return render(request, 'home.html', {'cidades':cidades})


def redirect_viajante(request):
    if request.method == 'POST':
        doc = request.POST.get('doc')
        senha = request.POST.get('senha')

        if len(doc) != 11:
            messages.error(request, 'Número de CPF inválido.')
            return redirect('index')

        user = authenticate(username=doc, password=senha)

        if user is not None:
            login_user(request)
            return redirect('viajante')
        else:
            messages.error(request, 'Credenciais inválidas.')

    return redirect('index')


def viajante(request):
    if request.GET.get('blogout'):
        logout(request)
        messages.success(request, 'Sessão encerrada.')
        return redirect('index')
    return render(request, template_name='viajante.html')


def cadastro_local(request):
    if request.method == 'GET':
        form = CadastroLocalForm()
        cidades = Cidade.objects.all()
        return render(request, 'cadastro_local.html', {'cidades':cidades, 'form':form})
    elif request.method == 'POST':
        form = CadastroLocalForm(request.POST)
        if form.is_valid():
            novo_local = form.save(commit=False)
            novo_local.tipo = form.cleaned_data['tipo']  
            novo_local.save()
            form.save()
            return HttpResponse('Local cadastrado com sucesso')
        else:
            return HttpResponse('Erro no formulário. Verifique os dados informados.')


def cidade(request, city_slug):
    if request.method == 'GET':
        cidade = Cidade.objects.get(nome_cidade=city_slug)
        return render(request, "cidade.html", {'cidade':cidade, 'locais':cidade.local.all()})


def local(request, local_slug):
    if request.method == 'GET':
        local = Local.objects.get(nome_local=local_slug)
        return render(request, "local.html", {'local':local})


def cadastro_usuario(request):
    if request.method == 'POST':
        form = CadastroUsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Cadastro realizado com sucesso!')
            return redirect('login')
        else:
            messages.error(request, 'Erro no cadastro. Verifique os dados informados.')
    else:
        form = CadastroUsuarioForm()
    return render(request, 'cadastro_usuario.html', {'form': form})


def cadastro_funcionario(request):
    if request.method == 'GET':
        return render(request, 'cadastro_funcionario.html')
    else:
        username = request.POST.get('username')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        cod = request.POST.get('cod')

        if not username:
            return HttpResponse('O nome de usuário deve ser fornecido')

        user = User.objects.filter(username=username).first()

        if user:
            return HttpResponse('Usuário já cadastrado com este nome')

        user = User.objects.create_user(username=username, email=email, password=senha, is_staff=True)
        user.cod = cod
        user.save()

        return HttpResponse('Usuário cadastrado com sucesso')


def cadastro_cidades(request):
    if request.method == 'POST':
        form = CadastroCidadeForm()
        if form.is_valid():
            form.save()
            return redirect('home')

    else:
        form = CadastroCidadeForm()

    return render(request, 'cadastro_cidade.html', {'form': form})


def login_user(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        username = request.POST.get('username')
        senha = request.POST.get('senha')

        user = authenticate(username=username, password=senha)

        if user:
            login(request, user)
            return redirect('/')
        else:
            if request.user.is_authenticated:
                return HttpResponse('email ou senha inválidos')
            return HttpResponse('Necessita de estar logado')
        
