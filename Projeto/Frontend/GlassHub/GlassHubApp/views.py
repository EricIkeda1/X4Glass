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
    # Create graphs
    graph1_html = graficos1.criar_grafico()
    graph2_html = graficos2.criar_grafico()
    graph3_html = graficos3.criar_grafico()
    graph4_html = graficos4.criar_grafico_bolhas()
    graph5_html = graficos5.criar_grafico_barras()
    graph6_html = graficos6.criar_treemap()
    graph7_html = graficos7.criar_grafico_barras_empilhadas()
    
    context = {
        'graph1': graph1_html,
        'graph2': graph2_html,
        'graph3': graph3_html,
        'graph4': graph4_html,
        'graph5': graph5_html,
        'graph6': graph6_html,
        'graph7': graph7_html,
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

@login_required
def temp_plot_view(request):
    return HttpResponse("A página temp-plot está desativada.")
