import smtplib
import email.message
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from .models import *
from random import randint
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
    if request.user.is_authenticated:
        return render(request,'Voleibol.html',{"caso1": True})
    else:
        return render(request,'Voleibol.html',{"caso1": False})
    
def homeLogado(request):
    return render(request,'Voleibol.html',{"caso1": True})

def openUser(request):
    return render(request,'cadastrar_user.html')

def openMsg(request):
    return render(request,'mandar_msg.html')

def openHistory(request):
    if request.user.is_authenticated:
        return render(request,'Historia.html',{"caso1": True})
    else:
        return render(request,'Historia.html',{"caso1": False})

def openFundamentos(request, caso):
    if request.user.is_authenticated:
        return render(request,'Fundamentos.html',{"caso1": True, "caso": caso})
    else:
        return render(request,'Fundamentos.html',{"caso1": False, "caso": caso})

def openCurious(request):
    if request.user.is_authenticated:
        return render(request,'curiosidades.html',{"caso1": True})
    else:
        return render(request,'curiosidades.html',{"caso1": False})

def openRefs(request):
    if request.user.is_authenticated:
        return render(request,'references.html',{"caso1": True})
    else:
        return render(request,'references.html',{"caso1": False})

@login_required(login_url="openLogin")
def openChat(request):
    mensages = Mensage.objects.all()

    return render(request,'chat.html',{"caso1": True, "mensagens": mensages})

def openLogin(request):
    return render(request,'realizar_login.html')

def esqueceuSenha(request):
    return render(request,'configuracao.html', {"caso": 1})

def openConf(request):
    return render(request,'configuracao.html', {"caso": 5})

def openRegras(request):
    if request.user.is_authenticated:
        return render(request,'Regras.html', {"caso1": True})
    else:
        return render(request,'Regras.html', {"caso1": False})

def getMensages(request):
    msg = Mensage.objects.all()
    return JsonResponse({"Msgs":list(msg.values())})

def cadastrar_user(request):
    nomeForm = request.POST.get("user")
    senhaForm = request.POST.get("password")
    emailForm = request.POST.get("mail")

    if nomeForm:
        if len(nomeForm) > 1:
            if emailForm:
                if "@gmail.com" in emailForm or "@yahoo.com" in emailForm:
                    if senhaForm:
                        if len(senhaForm) >= 5:
                            if senhaForm.isalpha():
                                erro = "!!  Insira ao menos um número ou símbolo !!"
                                return render(request, 'cadastrar_user.html', {"erro": erro})         
                            users = User.objects.all() 
                            for i in users:
                                if i.username == nomeForm or i.email == nomeForm:
                                    erro = "!!  Este usuário já existe  !!"
                                    return render(request, 'cadastrar_user.html', {"erro": erro})
                            user = User.objects.create_user(nomeForm, emailForm, senhaForm)
                        else:
                            erro = "!!  Senha deve conter ao menos 5 carateres !!"
                            return render(request, 'cadastrar_user.html', {"erro": erro})
                    else:
                        erro = "!!  Preenha Todos os campos !!"
                        return render(request, 'cadastrar_user.html', {"erro": erro})
                else:
                    erro = "!!  Insira um email válido  !!"
                    return render(request, 'cadastrar_user.html', {"erro": erro})   
            else:
                erro = "!!  Preenha Todos os campos  !!"
                return render(request, 'cadastrar_user.html', {"erro": erro}) 
        else:
            erro = "!!  Usuário deve conter mais de 1 letra  !!"
            return render(request, 'cadastrar_user.html', {"erro": erro})
    else:
        erro = "!!  Preenha Todos os campos  !!"
        return render(request, 'cadastrar_user.html', {"erro": erro})
    
    user.save()
    return render(request, 'realizar_login.html')

@login_required(login_url="openLogin")
def envia_msg(request):
    mensagemForm = request.POST.get("msg")
    idMensagem = request.POST.get("idresponse")
    idUser = f"{request.user}"
    
    numberMensages = Mensage.objects.all()
    idM = len(numberMensages) + 1
    if idMensagem == "":
        mensagem = Mensage(id=idM,mensage=mensagemForm,
                        id_user=idUser)
    else:
        mensagem = Mensage(id=idM,mensage=mensagemForm,
                        id_user=idUser, key=Mensage.objects.get(id=idMensagem))
        

    mensagem.save()

    return redirect("openChat")

def realizar_login(request):
    global nomeUser
    nomeForm = request.POST.get("name")
    senhaForm = request.POST.get("password")

    if nomeForm:
        if senhaForm:
            user = authenticate(request, username=nomeForm, password=senhaForm)
            if user:
                login(request,user)
                user.save()
                nomeUser = nomeForm
                return render(request, 'Voleibol.html', {"caso1": True, "caso2": "Configurações"})
    return render(request, 'realizar_login.html', {"erro": "Usuário ou senha incorretos"})

def deslogar(request):
    logout(request)
    return render(request,'realizar_login.html')

def gerarCode(): 
    global code
    code = ""
    for i in range(0,5):
        code += str(randint(0,9)) 
    return code

def recuperarSenha(request):
    userForm = request.POST.get("nome")
    try:
        user = User.objects.get(username=userForm)
    except:
        user = False   
    
    if "@" in userForm:
        usuario = User.objects.get(email = userForm)
    else:
        usuario = User.objects.get(username = userForm)

    if user:
        corpo_email = f"""
        Seu código de recuperação é {gerarCode()}
        """
        remetente = "voleiboltccif@gmail.com"
        msg = email.message.Message()
        msg['Subject'] = "Redeinição de Senha"
        msg['From'] = remetente#'remetente'
        msg['To'] = usuario.email
        password = 'bbfz gjgr cqsy xuuq'#'senha'#nao e a senha do seu email
    
        msg.add_header('Content-Type', 'text/html')
        msg.set_payload(corpo_email )

        s = smtplib.SMTP('smtp.gmail.com: 587')
        s.starttls()
        # Login Credentials for sending the mail
        s.login(msg['From'], password)
        s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))

        return render(request,'configuracao.html',{"caso":2, "nome":userForm})
    return render(request,'configuracao.html',{"caso":1, "erro":"Usuário Inexistente"})

def conferirCode(request,nomeusuario):
    codeForm = request.POST.get("code")
    if codeForm == "":  
        return render(request,'configuracao.html',{"caso":2,"erro":"Código Incorreto"})
    if codeForm == code:
       return render(request,'configuracao.html',{"caso":3, "nome": nomeusuario})
    return render(request,'configuracao.html',{"caso":2,"erro":"Código Incorreto"})

def definirSenha(request,nomeusuario):
    codeForm = request.POST.get("code")
    confirmacaoForm = request.POST.get("code2")
    
    parametro = User.objects.get(username = nomeusuario)
    
    if codeForm == confirmacaoForm:
        parametro.set_password(codeForm)
        parametro.save()
        return render(request,'configuracao.html',{"caso":4})
    return render(request,'configuracao.html',{"caso":3,"erro":"Senhas Diferentes"})

@login_required(login_url="openLogin")        
def excluirConta(request):
    usuario = request.user
    userDel = User.objects.get(username = usuario)
    
    userDel.delete()
    return render(request,'Voleibol.html', {"caso1": False})

@login_required(login_url="openLogin")
def mudarNome(request):
    newName = request.POST.get("newName")
    usuario = request.user
    userName = User.objects.get(username = usuario)
    users = User.objects.all()
    if len(newName) > 1:
        for i in users:
            if i.username == newName:
                erro = "!!  Este usuário já existe  !!"
                return render(request, 'configuracao.html', {"caso":5,"erro": erro})
        userName.username = newName
        userName.save()
    else:
        erro = "!!  Usuário deve conter mais de 1 letra  !!"
        return render(request, 'configuracao.html', {"caso": 5,"erro": erro})
    return render(request,'configuracao.html', {"caso": 5})

@login_required(login_url="openLogin")
def definirSenhaConf(request):
    codeForm = request.POST.get("code")
    confirmacaoForm = request.POST.get("code2")
    usuario = request.user
    
    parametro = User.objects.get(username = usuario)
    
    if codeForm == confirmacaoForm:
        parametro.set_password(codeForm)
        parametro.save()
        return render(request,'configuracao.html',{"caso":5, "erro": "Senha alterada com sucesso"})
    return render(request,'configuracao.html',{"caso":5,"erro":"Senhas Diferentes"})