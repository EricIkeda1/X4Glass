# Instalação de todos os Frameworks do Frontend X4Glass
- Para instalar todas as dependências do projeto, utilize o seguinte comando:
```pip install -r requirements.txt```

## 1. Crie um Superusuário
- Para acessar o painel de administração do Django e gerenciar os usuários, você precisará criar um superusuário. Execute o seguinte comando:
```python manage.py createsuperuser``` 

## 2. Inicie o Servidor de Desenvolvimento
### Explicação:
## Onde executar os comandos:
- Depois de configurar o superusuário, inicie o servidor de desenvolvimento do Django com o comando:
- Para rodar o servidor, você deve estar na pasta principal do projeto (onde o arquivo 'manage.py'está localizado). Esse é o diretório que contém a configuração principal do Django e onde o comando 'python manage.py runserver' deve ser executado.
- **Estrutura de pastas**: A árvore mostra onde o arquivo `manage.py` está localizado e destaca que é a partir dessa pasta que o servidor deve ser iniciado.
- O servidor estará disponível em http://127.0.0.1:8000/.

## Estrutura de Pastas
```bash
GlassHub/
│
├── GlassHub/                   # Configurações principais do projeto Django
│   ├── __init__.py
│   ├── asgi.py
│   ├── routing.py
│   ├── settings.py             # Configurações do Django (GlassHub/settings.py)
│   ├── urls.py                 # URLs principais do projeto
│   └── wsgi.py
│
├── GlassHubApp/                # Aplicação Django principal
│   ├── __init__.py
│   ├── admin.py                # Administração da aplicação
│   ├── apps.py                 # Configurações da aplicação
│   ├── broker.py
│   ├── consumers.py
│   ├── migrations/             # Migrações do banco de dados
│   ├── models.py               # Modelos do banco de dados
│   ├── static/                 # Arquivos estáticos (CSS, JS, imagens)
│   ├── tests.py                # Arquivos de teste da aplicação
│   ├── views.py                # Funções de visualização
│   └── templates/              # Templates HTML da aplicação
│       ├── login.html
│       ├── register.html
│       └── outras_paginas.html
│
├── db.sqlite3                  # Banco de dados SQLite
├── manage.py                   # Script de gerenciamento do Django (iniciar o projeto)
├── requirements.txt            # Arquivo com as dependências do projeto
└── README.md                   # Este arquivo README
