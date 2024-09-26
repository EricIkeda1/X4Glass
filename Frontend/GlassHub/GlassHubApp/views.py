from django.shortcuts import render

# Create your views here.
def monitoramento(request):
    return render(request, 'monitoramento.html')

def alarmes(request):
    context = {
        'range': range(6),
    }
    return render(request, 'alarmes.html', context)

def cadastro(request):
    return render(request, 'cadastro.html')

def dashbord(request):
    return render(request, 'dashbord.html')

def login(request):
    return render(request, 'login.html')

def faturamento(request):
    return render(request, 'faturamento.html')

def parametrizacao(request):
    return render(request, 'parametrizacao.html')

