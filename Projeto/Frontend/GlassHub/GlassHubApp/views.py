from pyexpat.errors import messages
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_django
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .models import CustomUser
from .graficos import graficos1, graficos2, graficos3, graficos4, graficos5, graficos6, graficos7
import plotly.offline as pyo
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

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

def obter_dados_eventos():
    # Exemplo de dados de eventos no formato especificado.
    return [
        {'sector': 'LAPIDAÇÃO', 'product': 'PORTA CORRER VERDE 10MM TEMPERADO', 'date': '2024-10-08 23:33:49.458547+00:00'},
        {'sector': 'LAPIDAÇÃO', 'product': 'PORTA CORRER VERDE 10MM TEMPERADO', 'date': '2024-10-08 23:35:12.790716+00:00', 'max_idle': 3600},
    ]

@login_required
def dashbord(request):
    eventos = obter_dados_eventos()  # Coletando dados de eventos

    context = {
        'graph1': graficos1.criar_grafico(),
        'graph2': graficos2.criar_grafico(),
        'graph3': graficos3.criar_grafico(),
        'graph4': graficos4.criar_grafico_bolhas(),
        'graph5': graficos5.criar_grafico_barras(),
        'graph6': graficos6.criar_treemap(),
        'graph7': graficos7.criar_grafico_barras_empilhadas(),
        'eventos': eventos,
    }
    
    return render(request, 'dashbord.html', context)
    
def login(request):
    if request.method == "GET":
        return render(request, 'login.html')
    else:
        username = request.POST.get('username')  
        email = request.POST.get('email')     
        password = request.POST.get('password')   
        
        user = authenticate(username=username, password=password)

        if not user:
            try:
                user = CustomUser.objects.get(email=email)  
                user = authenticate(username=user.username, password=password) 
            except CustomUser.DoesNotExist:
                user = None  

        if user:
            login_django(request, user)
            print(f'User {username} logged in successfully.')
            return redirect('dashbord')  
        else:
            print('Invalid login attempt.')
            messages.error(request, 'Nome, e-mail ou senha inválidos')
            return render(request, 'login.html')
        
def logout_view(request):
    logout(request)  
    return redirect('login')
        
@login_required        
def faturamento(request):
    return render(request, 'faturamento.html')

@login_required
def parametrizacao(request):
    return render(request, 'parametrizacao.html')

