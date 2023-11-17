from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="home"),
    path('openUser/', views.openUser, name="openUser"),
    path('openHistory/', views.openHistory, name="openHistory"),
    path('openRegras/', views.openRegras, name="openRegras"),
    path('openCurious/', views.openCurious, name="openCurious"),
    path('openRefs/', views.openRefs, name="openRefs"),
    path('openFundamentos/<str:caso>', views.openFundamentos, name="openFundamentos"),
    path('openMsg/', views.openMsg, name="openMsg"),
    path('openLogin/', views.openLogin, name="openLogin"),
    path('mandar_msg/', views.envia_msg, name="mandar_msg"),
    path('cadastrar_user/', views.cadastrar_user, name="cadastrar_user"),
    path('realizar_login/', views.realizar_login, name="realizar_login"),
    path('deslogar/', views.deslogar, name="deslogar"),
    path('recuperarSenha/', views.recuperarSenha, name="recuperarSenha"),
    path('conferirCode/<str:nomeusuario>', views.conferirCode, name="conferirCode"),   
    path('esqueceuSenha/', views.esqueceuSenha, name="esqueceuSenha"),
    path('openConf/', views.openConf, name="openConf"),
    path('openChat/', views.openChat, name="openChat"),
    path('getMensages/', views.getMensages, name="getMensages"),
    path('excluirConta/', views.excluirConta, name="excluirConta"),
    path('mudarNome/', views.mudarNome, name="mudarNome"),
    path('definirSenhaConf/', views.definirSenhaConf, name="definirSenhaConf"),
    path('homeLogado/', views.homeLogado, name="homeLogado"),
    path('definirSenha/<str:nomeusuario>', views.definirSenha, name="definirSenha"),
]