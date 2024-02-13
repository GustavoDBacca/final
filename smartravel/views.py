from msilib.schema import ListView
from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .forms import CadastroCidadeForm, CadastroLocalForm, CadastroUsuarioForm
from smartravel.models import Categorias, Cidade, Local, Usuario
from django.contrib.auth import logout


def home(request):
    cidades = Cidade.objects.all()
    print(request.user)
    return render(request, 'home.html', {'cidades':cidades})

def logout_view(request):
    logout(request)
    return redirect('login')


def cadastro_local(request):
    if request.method == 'GET':
        form = CadastroLocalForm()
        cidades = Cidade.objects.all()
        return render(request, 'cadastro_local.html', {'cidades':cidades, 'form':form})
    elif request.method == 'POST':
        form = CadastroLocalForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('Local cadastrado com sucesso')
        else:
            return HttpResponse('Erro no formulário. Verifique os dados informados.')


def local(request, local_id):
    if request.method == 'GET':
        local = get_object_or_404(Local, id=local_id)
        return render(request, "local.html", {'local': local})


def cidade(request, city_slug):
    if request.method == 'GET':
        cidade = Cidade.objects.get(nome_cidade=city_slug)
        categorias = Categorias.objects.all()
        categoria = request.GET.get('categoria')
        if categoria is None:
            local = cidade.local.all()
        else:
            local = Local.objects.filter(cidade__nome_cidade=city_slug, tipo__categorias=categoria)
        return render(request, "cidade.html", {'cidade':cidade, 'locais':local, 'categorias':categorias})
    

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
        form = CadastroCidadeForm(request.POST)
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
        

# def adicionar_ao_carrinho(request, local_id):
#     local = get_object_or_404(Local, id=local_id)
#     if request.method == 'POST':
#         carrinho, _ = Carrinho.objects.get_or_create(usuario=request.user)
#         carrinho.locais.add(local)
#         return redirect('carrinho')
    
    
# def carrinho(request):
#     carrinho, _ = Carrinho.objects.get_or_create(usuario=request.user)
#     locais = carrinho.locais.all()
#     return render(request, "carrinho.html", {"carrinho": locais})