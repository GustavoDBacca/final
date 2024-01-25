from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('cidade/<slug:city_slug>/', views.cidade, name='cidade'), 
    path('local/<slug:local_slug>', views.local, name='local'),
    # path('agencia/principal/', views.agencia, name='agencia'),
    path('viajante/principal/', views.viajante, name='viajante'),
    # path('cadastro_agencia/', views.cadastro_agencia, name='cadastro_agencia'),
    path('cadastro_roteiros/', views.cadastro_local, name='cadastro_local'),
    path('login/', views.login_user, name='login'),
    path('login/cadastro_usuario/', views.cadastro_user, name='cadastro_usuario'),
]

#    path('blumenau/', views.blumenau, name='blumenau'),
#    path('indaial/', views.indaial, name='indaial'),
#    path('pomerode/', views.pomerode, name='pomerode'),
#    path("balneario_Camboriu/", views.balneario_camboriu, name="balneario_camboriu"),
#    path("itapema/", views.itapema, name="itapema"),
#    path("joinville/", views.joinville, name="joinville"),
#    path("timbo/", views.timbo, name="timbo"),
#    path("gaspar/", views.gaspar, name="gaspar"),
#    path("bombinhas/", views.bombinhas, name="bombinhas"),
#    path("florianopolis/", views.florianopolis, name="florianopolis"),
