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
from json import loads, dumps
from .models import eventos
from asgiref.sync import sync_to_async
from channels.generic.websocket import AsyncWebsocketConsumer
from .models import eventos
from django.contrib.auth.hashers import make_password

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

@login_required
def dashbord(request):
    # Obter todos os eventos do banco de dados
    all_eventos = eventos.objects.all()

    # Criar os gráficos
    graph1 = graficos1.criar_grafico()
    graph2 = graficos2.criar_grafico()
    graph3 = graficos3.criar_grafico()
    graph4 = graficos4.criar_grafico_bolhas()
    graph5 = graficos5.criar_grafico_barras()
    graph6 = graficos6.criar_treemap()
    graph7 = graficos7.criar_grafico_barras_empilhadas()

    # Preparar o contexto
    context = {
        'graph1': graph1,
        'graph2': graph2,
        'graph3': graph3,
        'graph4': graph4,
        'graph5': graph5,
        'graph6': graph6,
        'graph7': graph7,
        'eventos': all_eventos,
    }

    # Renderizar a resposta com o contexto
    response = render(request, 'dashboard.html', context)
    response['Cache-Control'] = 'no-cache'

    return response

def registro(request): 
    if request.method == "GET":
        return render(request, 'registro.html')  
    else:
        username = request.POST.get('username')
        email = request.POST.get('email')
        senha = request.POST.get('password')  # Nome correto do campo no formulário

        # Verificar se o nome de usuário já existe
        if User.objects.filter(username=username).exists():
            return HttpResponse('Já existe um usuário com esse nome')

        # Criptografando a senha antes de salvar
        senha_criptografada = make_password(senha)

        # Criar o usuário com a senha criptografada
        user = User.objects.create(username=username, email=email, password=senha_criptografada)
        user.save()

        return HttpResponse(f'Usuário {username} cadastrado com sucesso')
    
def login(request):
    if request.method == "GET":
        return render(request, 'login.html')
    else:
        username = request.POST.get('username')  
        email = request.POST.get('email')     
        password = request.POST.get('password')  # Nome correto do campo no formulário

        # Tentar autenticar o usuário pelo nome de usuário
        user = authenticate(request, username=username, password=password)

        # Caso o usuário não seja encontrado pelo nome, tenta pelo e-mail
        if not user:
            try:
                user = User.objects.get(email=email)  # Busca o usuário pelo e-mail
                user = authenticate(request, username=user.username, password=password)  # Tenta autenticar com o nome de usuário
            except User.DoesNotExist:
                user = None

        if user:
            login_django(request, user)  # Realiza o login
            return redirect('dashbord')  # Redireciona para o painel de controle
        else:
            messages.error(request, 'Nome, e-mail ou senha inválidos')  # Mensagem de erro
            return render(request, 'login.html')

def logout_view(request):
    logout(request)  # Realiza o logout
    return redirect('login')  # Redireciona para a página de login
        
@login_required        
def faturamento(request):
    return render(request, 'faturamento.html')

@login_required
def parametrizacao(request):
    return render(request, 'parametrizacao.html')

class EventConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.group_name = "temperlandia"
        await self.channel_layer.group_add(self.group_name, self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.group_name, self.channel_name)

    async def receive(self, text_data):
        data = loads(text_data)
        
        # Salva o evento no banco de dados SQLite
        await self.save_event(data)

        await self.channel_layer.group_send(
            self.group_name,
            {
                'type': 'send_message',
                'message': data
            }
        )

    async def send_message(self, event):
        message = event['message']
        await self.send(text_data=dumps(message))

@sync_to_async
def save_event(self, data):
        # Aqui você salva os dados no SQLite, com base nos campos fornecidos
        eventos.objects.create(
            name=data.get("name"),
            width=data.get("width"),
            height=data.get("height"),
            code=data.get("code"),
            order_id=data.get("order_id")
        )
        
def dashbord_view(request):
    # Buscando todos os eventos do banco de dados
    eventos_data = eventos.objects.all()
    
    # Processando os dados para gráficos
    data = {
        'eventos': eventos_data
    }

    return render(request, 'dashbord.html', data)

def api_eventos(request):
    eventos_data = list(eventos.objects.values())
    return JsonResponse(eventos_data, safe=False)