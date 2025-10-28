# Python + Mysql

## Passo 0: Pré-requisitos (Seu Ambiente Windows)

Antes de começar, garanta que você tenha:

1. **Python:** Instalado no Windows. (Você pode baixar no [python.org](https://www.python.org/downloads/)).
2. **Poetry:** Instalado. Se não tiver, instale com o PowerShell:

    ```powershell
    (Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | py
    ```

3. **MySQL Server:** Instalado e rodando. Para Windows, a forma mais fácil é usar um pacote como **XAMPP** ou **WAMP**, que já vem com o MySQL e o phpMyAdmin (uma interface gráfica para gerenciar o banco). Como alternativa, instale o [link suspeito removido] oficial.
      * Anote o **usuário** (geralmente `root`) e a **senha** que você definir durante a instalação.


## Passo 1: Criação do Banco de Dados no MySQL

Antes de mexer no código, vamos criar o banco de dados.

1. Abra seu cliente MySQL (pode ser o `mysql.exe` pelo terminal, o HeidiSQL, ou o phpMyAdmin do XAMPP).

2. Execute o seguinte comando SQL para criar o banco. Usaremos `utf8mb4` para suportar emojis e caracteres especiais.

    ```sql
    CREATE DATABASE db_tarefas CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
    ```

## Passo 2: Inicialização do Projeto com Poetry

1. Abra seu terminal (PowerShell ou CMD).

2. Crie uma pasta para o projeto e entre nela:

    ```bash
    mkdir tarefas
    cd tarefas
    ```

3. Inicie o Poetry no projeto. Ele fará algumas perguntas; você pode apenas pressionar Enter para aceitar os padrões.

    ```bash
    poetry init
    ```

4. Ative o ambiente virtual criado pelo Poetry. Isso é crucial\!

    ```bash
    poetry env activate
    ```

## Passo 3: Instalação das Dependências

Com o ambiente ativo, vamos adicionar os pacotes Python necessários:

```bash
# Adiciona o Django
poetry add "django~=4.1.0"

poetry add mysqlclient

poetry add python-dotenv
```

## Passo 4: Estrutura do Projeto Django

1. Crie o projeto Django. Usaremos `config` para o nome do projeto principal e `.` para criá-lo na pasta atual.

    ```bash
    poetry run django-admin startproject config .
    ```

2. Crie nosso aplicativo de tarefas, que chamaremos de `tarefas_app`:

    ```bash
    poetry run python manage.py startapp tarefas_app
    ```

Sua estrutura de pastas deve se parecer com isto:

```
tarefas/
├── config/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── tarefas_app/
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   └── views.py
├── manage.py
├── pyproject.toml
└── poetry.lock
```

## Passo 5: Configuração (settings.py e .env)

Vamos configurar o Django para usar nosso app `` e o banco de dados MySQL.

1. **Crie um arquivo `.env`** na raiz do projeto (mesmo local do `manage.py`) para guardar suas senhas.

    **`.env`**

    ```ini
    # Chave secreta do Django (pode ser qualquer coisa)
    SECRET_KEY=django-insecure-@#seu-segredo-aleatorio-aqui#@

    # Modo Debug
    DEBUG=True

    # Configuração do Banco de Dados
    DB_NAME=db_tarefas
    DB_USER=root
    DB_PASSWORD=
    DB_HOST=127.0.0.1
    DB_PORT=3306
    ```

2. **Edite o arquivo `config/settings.py`** para ler o `.env` e configurar o banco.

    **`config/settings.py`**

    ```python
    import os
    from pathlib import Path
    from dotenv import load_dotenv # Importe o dotenv

    # Build paths inside the project like this: BASE_DIR / 'subdir'.
    BASE_DIR = Path(__file__).resolve().parent.parent

    # Carrega as variáveis do arquivo .env
    load_dotenv(BASE_DIR / '.env')

    # Quick-start development settings - unsuitable for production
    # See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

    # Pegue a SECRET_KEY do .env
    SECRET_KEY = os.getenv('SECRET_KEY')

    # Pegue o DEBUG do .env
    DEBUG = os.getenv('DEBUG', 'False') == 'True'

    ALLOWED_HOSTS = []


    # Application definition

    INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'tarefas_app', # <--- ADICIONE NOSSO APP AQUI
    ]

    MIDDLEWARE = [
        'django.middleware.security.SecurityMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
    ]

    ROOT_URLCONF = 'config.urls'

    TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            # Adicione o diretório de templates da raiz do projeto
            'DIRS': [BASE_DIR / 'templates'], # <--- ADICIONE ISSO
            'APP_DIRS': True,
            'OPTIONS': {
                'context_processors': [
                    'django.template.context_processors.debug',
                    'django.template.context_processors.request',
                    'django.contrib.auth.context_processors.auth',
                    'django.contrib.messages.context_processors.messages',
                ],
            },
        },
    ]

    WSGI_APPLICATION = 'config.wsgi.application'


    # Database
    # https://docs.djangoproject.com/en/5.0/ref/settings/#databases

    # Substitua a configuração padrão do SQLite
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': os.getenv('DB_NAME'),
            'USER': os.getenv('DB_USER'),
            'PASSWORD': os.getenv('DB_PASSWORD'),
            'HOST': os.getenv('DB_HOST'),
            'PORT': os.getenv('DB_PORT'),
            'OPTIONS': {
                # Garante o modo estrito do MySQL
                'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
            },
        }
    }


    # Password validation
    # https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

    AUTH_PASSWORD_VALIDATORS = [
        # ... (pode deixar como está)
    ]


    # Internationalization
    # https://docs.djangoproject.com/en/5.0/topics/i18n/

    LANGUAGE_CODE = 'pt-br' # <--- MUDE AQUI

    TIME_ZONE = 'America/Sao_Paulo' # <--- MUDE AQUI

    USE_I18N = True

    USE_TZ = True


    # Static files (CSS, JavaScript, Images)
    # https://docs.djangoproject.com/en/5.0/howto/static-files/

    STATIC_URL = 'static/'

    # Default primary key field type
    # https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

    DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
    ```

## Passo 6: Modelo de Dados (Model)

Vamos definir como uma "Tarefa" será no banco de dados.

**`tarefas_app/models.py`**

```python
from django.db import models

class Tarefa(models.Model):
    titulo = models.CharField(max_length=200)
    # blank=True e null=True tornam este campo opcional
    descricao = models.TextField(blank=True, null=True) 
    concluida = models.BooleanField(default=False)
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        # Isso é o que aparecerá no painel Admin
        return self.titulo
    
    class Meta:
        # Ordena as tarefas pela data de criação por padrão
        ordering = ['data_criacao']
```

## Passo 7: Migrações e Admin

Agora, vamos aplicar esse modelo ao nosso banco MySQL.

1. Crie os arquivos de migração:

    ```bash
    python manage.py makemigrations tarefas_app
    ```

2. Aplique as migrações no banco de dados (isso criará a tabela `tarefas_app_tarefa`):

    ```bash
    python manage.py migrate
    ```

3. (Opcional, mas recomendado) Crie um superusuário para acessar o Admin:

    ```bash
    python manage.py createsuperuser
    ```

    (Siga as instruções para criar seu usuário admin)

4. (Opcional) Registre seu modelo no Admin para poder gerenciá-lo.

    **`tarefas_app/admin.py`**

    ```python
    from django.contrib import admin
    from .models import Tarefa

    @admin.register(Tarefa)
    class TarefaAdmin(admin.ModelAdmin):
        list_display = ('titulo', 'concluida', 'data_criacao')
        list_filter = ('concluida', 'data_criacao')
        search_fields = ('titulo', 'descricao')
    ```

## Passo 8: URLs (Rotas)

Precisamos definir quais URLs acionarão quais funções (Views).

1. Primeiro, no arquivo principal de URLs, vamos incluir as URLs do nosso app `tarefas_app`.

    **`config/urls.py`**

    ```python
    from django.contrib import admin
    from django.urls import path, include # Adicione 'include'

    urlpatterns = [
        path('admin/', admin.site.urls),
        path('', include('tarefas_app.urls')), # <--- ADICIONE ISSO
    ]
    ```

2. Agora, crie o arquivo de URLs específico do app `tarefas_app`.

    **Crie o arquivo `tarefas_app/urls.py`**

    ```python
    from django.urls import path
    from . import views

    urlpatterns = [
        # Rota principal (ex: http://127.0.0.1:8000/)
        path('', views.lista_tarefas, name='lista_tarefas'),
        
        # Rota para atualizar (marcar/desmarcar) uma tarefa
        # ex: /atualizar/5/
        path('atualizar/<int:pk>/', views.atualizar_tarefa, name='atualizar_tarefa'),
        
        # Rota para deletar uma tarefa
        # ex: /deletar/5/
        path('deletar/<int:pk>/', views.deletar_tarefa, name='deletar_tarefa'),
    ]
    ```

## Passo 9: Views (A Lógica)

As views processam as requisições do usuário e retornam uma resposta (nosso HTML).

**`tarefas_app/views.py`**

```python
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from .models import Tarefa

def lista_tarefas(request):
    # Se a requisição for POST, significa que o formulário de "Nova Tarefa" foi enviado
    if request.method == 'POST':
        titulo = request.POST.get('titulo')
        if titulo: # Só cria se o título não estiver vazio
            Tarefa.objects.create(titulo=titulo)
        return redirect('lista_tarefas') # Redireciona para a mesma página (GET)

    # Se for GET, apenas buscamos e exibimos as tarefas
    tarefas_pendentes = Tarefa.objects.filter(concluida=False).order_by('-data_criacao')
    tarefas_concluidas = Tarefa.objects.filter(concluida=True).order_by('data_criacao')
    
    context = {
        'tarefas_pendentes': tarefas_pendentes,
        'tarefas_concluidas': tarefas_concluidas,
    }
    return render(request, 'tarefas_app/lista_tarefas.html', context)


# Garante que esta view só possa ser acessada via POST (pelo formulário)
@require_POST
def atualizar_tarefa(request, pk):
    # Busca a tarefa pelo ID (pk) ou retorna erro 404 se não existir
    tarefa = get_object_or_404(Tarefa, pk=pk)
    
    # Inverte o status de 'concluida'
    # Se era False, vira True. Se era True, vira False.
    tarefa.concluida = not tarefa.concluida
    tarefa.save()
    
    return redirect('lista_tarefas')


# Garante que esta view só possa ser acessada via POST
@require_POST
def deletar_tarefa(request, pk):
    tarefa = get_object_or_404(Tarefa, pk=pk)
    tarefa.delete()
    return redirect('lista_tarefas')
```

## Passo 10: Templates (Frontend com Bootstrap)

Vamos criar o visual da nossa aplicação. Crie a pasta `templates` na raiz do projeto (mesmo nível do `manage.py`).

1. **Crie a pasta `templates/`**
2. **Crie a pasta `templates/tarefas_app/`** (é uma boa prática manter os templates dentro de uma pasta com o nome do app).

### Arquivo Base (com Bootstrap)

Este será o "molde" do nosso site.

**`templates/base.html`**

```html
<!doctype html>
<html lang="pt-br">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    
    <title>{% block title %}Sistema de Tarefas{% endblock %}</title>

    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
    
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/font/bootstrap-icons.min.css">
    
    <style>
        /* Estilo para tarefas concluídas */
        .task-done {
            text-decoration: line-through;
            opacity: 0.7;
        }
    </style>
</head>
<body class="bg-light">

    <nav class="navbar navbar-expand-lg navbar-dark bg-dark mb-4 shadow-sm">
        <div class="container">
            <a class="navbar-brand" href="{% url 'lista_tarefas' %}">
                <i class="bi bi-check2-square"></i>
                Meu tarefas_app List (Django + MySQL)
            </a>
        </div>
    </nav>

    <main class="container">
        {% block content %}
        {% endblock %}
    </main>
    
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz" crossorigin="anonymous"></script>
</body>
</html>
```

### Página da Lista de Tarefas

Este arquivo vai "herdar" o `base.html` e mostrar o conteúdo dinâmico.

**`templates/tarefas_app/lista_tarefas.html`**

```html
{% extends 'base.html' %}

{% block title %}Minhas Tarefas{% endblock %}

{% block content %}
<div class="row">
    <div class="col-md-10 offset-md-1 col-lg-8 offset-lg-2">
        
        <div class="card mb-4 shadow-sm">
            <div class="card-body">
                <h5 class="card-title">Nova Tarefa</h5>
                <form action="{% url 'lista_tarefas' %}" method="POST" autocomplete="off">
                    {% csrf_token %} <div class="input-group">
                        <input type="text" class="form-control" name="titulo" 
                               placeholder="O que precisa ser feito?" required>
                        <button class="btn btn-primary" type="submit">
                            <i class="bi bi-plus-lg"></i> Adicionar
                        </button>
                    </div>
                </form>
            </div>
        </div>

        <div class="card shadow-sm mb-4">
            <div class="card-header bg-white">
                <h5 class="mb-0">Pendentes</h5>
            </div>
            <ul class="list-group list-group-flush">
                {% for tarefa in tarefas_pendentes %}
                    <li class="list-group-item d-flex justify-content-between align-items-center">
                        <div>
                            <form action="{% url 'atualizar_tarefa' tarefa.pk %}" method="POST" class="d-inline">
                                {% csrf_token %}
                                <button type="submit" class="btn btn-outline-success btn-sm me-2 border-0">
                                    <i class="bi bi-check-circle"></i>
                                </button>
                            </form>
                            {{ tarefa.titulo }}
                        </div>

                        <form action="{% url 'deletar_tarefa' tarefa.pk %}" method="POST" class="d-inline">
                            {% csrf_token %}
                            <button type="submit" class="btn btn-outline-danger btn-sm border-0" 
                                    onclick="return confirm('Tem certeza que deseja excluir esta tarefa?');">
                                <i class="bi bi-trash"></i>
                            </button>
                        </form>
                    </li>
                {% empty %}
                    <li class="list-group-item text-muted text-center">Nenhuma tarefa pendente!</li>
                {% endfor %}
            </ul>
        </div>

        <div class="card shadow-sm">
            <div class="card-header bg-white">
                <h5 class="mb-0">Concluídas</h5>
            </div>
            <ul class="list-group list-group-flush">
                {% for tarefa in tarefas_concluidas %}
                    <li class="list-group-item d-flex justify-content-between align-items-center task-done">
                        <div>
                            <form action="{% url 'atualizar_tarefa' tarefa.pk %}" method="POST" class="d-inline">
                                {% csrf_token %}
                                <button type="submit" class="btn btn-outline-secondary btn-sm me-2 border-0">
                                    <i class="bi bi-arrow-counterclockwise"></i>
                                </button>
                            </form>
                            {{ tarefa.titulo }}
                        </div>

                        <form action="{% url 'deletar_tarefa' tarefa.pk %}" method="POST" class="d-inline">
                            {% csrf_token %}
                            <button type="submit" class="btn btn-outline-danger btn-sm border-0"
                                    onclick="return confirm('Tem certeza que deseja excluir esta tarefa?');">
                                <i class="bi bi-trash"></i>
                            </button>
                        </form>
                    </li>
                {% empty %}
                    <li class="list-group-item text-muted text-center">Nenhuma tarefa concluída ainda.</li>
                {% endfor %}
            </ul>
        </div>

    </div>
</div>
{% endblock %}
```

## Passo 11: Rodando o Projeto

Seu projeto está completo. Volte ao terminal (com o `poetry shell` ativo) e execute o servidor:

```bash
python manage.py runserver
```

Abra seu navegador e acesse: **[http://127.0.0.1:8000/](https://www.google.com/url?sa=E&source=gmail&q=http://127.0.0.1:8000/)**
