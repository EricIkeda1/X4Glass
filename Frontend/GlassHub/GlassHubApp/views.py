from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'monitoramento.html')

def dashbord(request):
    return render(request, 'dashbord.html')

def login(request):
    return render(request, 'login.html')

