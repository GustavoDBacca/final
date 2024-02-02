from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('cidade/<slug:city_slug>/', views.cidade, name='cidade'), 
    path('local/<slug:local_slug>/', views.local, name='local'),
    path('cadastro_local/', views.cadastro_local, name='cadastro_local'),
    path('cadastro_funcionario/', views.cadastro_funcionario, name='cadastro_funcionario'),    
    path('cadastro_cidade/', views.cadastro_cidades, name='cadastro_cidade'),
    path('viajante/principal/', views.viajante, name='viajante'),
    path('login/', views.login_user, name='login'),
    path('login/cadastro_usuario/', views.cadastro_usuario, name='cadastro_usuario'),
]
