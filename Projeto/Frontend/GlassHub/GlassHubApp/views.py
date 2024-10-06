from pyexpat.errors import messages
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_django
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .models import CustomUser

# Create your views here.
@login_required
def monitoramento(request):
    return render(request, 'monitoramento.html')
@login_required
def alarmes(request):
    context = {
        'range': range(6),
    }
    return render(request, 'alarmes.html', context)

@login_required
def cadastro(request):
    return render(request, 'cadastro.html')

def registro(request):
    if request.method == "GET":
        return render(request, 'registro.html')  
    else:
        username = request.POST.get('username')
        email = request.POST.get('email')
        senha = request.POST.get('senha') 

        # Check if the user already exists
        if User.objects.filter(username=username).exists():
            return HttpResponse('Já existe um usuário com esse nome')

        # Create the user if it doesn't exist
        user = User.objects.create_user(username=username, email=email, password=senha)
        user.save()

        return HttpResponse(f'Usuário {username} cadastrado com sucesso')

@login_required
def dashbord(request):
    return render(request, 'dashbord.html')

def login(request):
    if request.method == "GET":
        return render(request, 'login.html')
    else:
        username = request.POST.get('username')  # Obtém o nome de usuário
        email = request.POST.get('email')        # Obtém o e-mail
        password = request.POST.get('password')   # Obtém a senha

        # Tenta autenticar usando o nome de usuário
        user = authenticate(username=username, password=password)

        # Se a autenticação falhar, tenta autenticar usando o e-mail
        if not user:
            try:
                user = CustomUser.objects.get(email=email)  # Tenta encontrar o usuário pelo e-mail
                user = authenticate(username=user.username, password=password)  # Autentica com o nome de usuário
            except CustomUser.DoesNotExist:
                user = None  # Se o usuário não existir, define como None

        if user:
            login_django(request, user)
            print(f'User {username} logged in successfully.')
            return redirect('dashbord')  
        else:
            print('Invalid login attempt.')
            messages.error(request, 'Nome, e-mail ou senha inválidos')
            return render(request, 'login.html')
        
def logout_view(request):
    logout(request)  # Desloga o usuário
    return redirect('login')
        
@login_required        
def faturamento(request):
    return render(request, 'faturamento.html')

@login_required
def parametrizacao(request):
    return render(request, 'parametrizacao.html')

