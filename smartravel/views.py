from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
# from .forms import CadastroUsuarioForm

from smartravel.models import Cidade, Local


def home(request):
    cidades = Cidade.objects.all()
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


# def cadastro_agencia(request):
#     if request.method == 'POST':
#         nome = request.POST.get('nome')
#         cnpj = request.POST.get('cnpj')
#         telefone = request.POST.get('telefone')
#         email = request.POST.get('email')
#         senha = request.POST.get('senha')

#         if Agencia.objects.filter(doc=cnpj).exists():
#             messages.error(request, "CNPJ já cadastrado.")
#             return redirect('index')

#         agencia = Agencia(nome=nome, doc=cnpj, telefone=telefone, email=email, senha=senha)
#         agencia.save()

#         return redirect('index')

#     return render(request, 'cadastro_agencia.html')


# def redirect_agencia(request):
#     if request.method == 'POST':
#         doc = request.POST.get('doc')
#         senha = request.POST.get('senha')

#         if len(doc) != 14:
#             messages.error(request, 'Número de CNPJ inválido.')
#             return redirect('index')

#         user = authenticate(username=doc, password=senha)

#         if user is not None:
#             login_user(request)
#             return redirect('agencia')
#         else:
#             messages.error(request, 'Credenciais inválidas.')

#     return redirect('index')


# def agencia(request):
#     if request.GET.get('blogout'):
#         logout(request)
#         messages.success(request, 'Sessão encerrada.')
#         return redirect('index')
#     return render(request, template_name='agencia.html')


def viajante(request):
    if request.GET.get('blogout'):
        logout(request)
        messages.success(request, 'Sessão encerrada.')
        return redirect('index')
    return render(request, template_name='viajante.html')


def cadastro_local(request):
    if request.method == 'GET':
        return render(request, 'cadastro_usuario.html')
    else:
        nome = request.POST.get('nome')
        cidade = request.POST.get('cidade')
        bairro = request.POST.get('bairro')
        rua = request.POST.get('rua')
        horarios = request.POST.get('horarios')

        if not nome:
            return HttpResponse('O nome de usuário deve ser fornecido')

        user = User.objects.filter(username=nome).first()

        if user:
            return HttpResponse('Usuário já cadastrado com este nome')

        user = User.objects.create_user(username=nome, cidade=cidade, bairro=bairro, rua=rua, horarios=horarios)
        user.cidade = cidade
        user.bairro = bairro
        user.rua = rua
        user.horarios = horarios
        user.save()

        return HttpResponse('Usuário cadastrado com sucesso')


def cidade(request, city_slug):
    if request.method == 'GET':
        cidade = Cidade.objects.get(nome_cidade=city_slug)
        return render(request, "cidade.html", {'cidade':cidade, 'locais':cidade.local.all()})
    

    

def local(request, local_slug):
    if request.method == 'GET':
        local = Local.objects.get(nome_local=local_slug)
        return render(request, "local.html", {'local':local})

# def cadastro_usuario(request):
#     if request.method == 'POST':
#         form = CadastroUsuarioForm(request.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'Cadastro realizado com sucesso!')
#             return redirect('login')
#         else:
#             messages.error(request, 'Erro no cadastro. Verifique os dados informados.')
#     else:
#         form = CadastroUsuarioForm()
#     return render(request, 'cadastro_usuario.html', {'form': form})


def cadastro_user(request):
    if request.method == 'GET':
        return render(request, 'cadastro_usuario.html')
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

        user = User.objects.create_user(username=username, email=email, password=senha)
        user.cod = cod
        user.save()

        return HttpResponse('Usuário cadastrado com sucesso')


def login_user(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        username = request.POST.get('username')
        senha = request.POST.get('senha')

        user = authenticate(username=username, password=senha)

        if user:
            login(request, user)
            return HttpResponse('autenticado')
        else:
            if request.user.is_authenticated:
                return HttpResponse('email ou senha inválidos')
            return HttpResponse('Necessita de estar logado')
