# Sistema tarefas com prazo

## 1. Criar Banco de Dados

Abra **phpMyAdmin** ou **MySQL Workbench** e rode:

```sql
CREATE DATABASE db_tarefas CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
```

---

## 2. Criar Projeto

```bash
mkdir tarefas 
cd tarefas
poetry init
poetry env activate
```

---

## 3. Instalar Dependências

```bash
poetry add "django~=4.1.0"
poetry add mysqlclient
poetry add python-dotenv
```

---

## 4. Criar Projeto + App

```bash
poetry run django-admin startproject config .
poetry run python manage.py startapp tarefas_app
```

---

## 5. Arquivo `.env` (na pasta raiz do projeto)

```bash

SECRET_KEY=django-insecure-troque-por-uma-chave-forte
DEBUG=True
DB_NAME=db_tarefas
DB_USER=root
DB_PASSWORD=
DB_HOST=127.0.0.1
DB_PORT=3306

```

---

## 6. `config/settings.py` (substitua todo o conteúdo)

```python
import os
from pathlib import Path
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(BASE_DIR / '.env')

SECRET_KEY = os.getenv('SECRET_KEY')
DEBUG = os.getenv('DEBUG', 'False') == 'True'
ALLOWED_HOSTS = []

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'tarefas_app',
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
        'DIRS': [BASE_DIR / 'templates'],
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

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.getenv('DB_NAME'),
        'USER': os.getenv('DB_USER'),
        'PASSWORD': os.getenv('DB_PASSWORD'),
        'HOST': os.getenv('DB_HOST'),
        'PORT': os.getenv('DB_PORT'),
        'OPTIONS': {'init_command': "SET sql_mode='STRICT_TRANS_TABLES'"},
    }
}

LANGUAGE_CODE = 'pt-br'
TIME_ZONE = 'America/Sao_Paulo'
USE_I18N = True
USE_TZ = True
STATIC_URL = 'static/'
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
```

---

## 7. Modelo (`tarefas_app/models.py`)

```python
from django.db import models
from django.utils import timezone

class Tarefa(models.Model):
    titulo = models.CharField("Título", max_length=200)
    descricao = models.TextField("Descrição", blank=True, null=True)
    prazo = models.DateField("Prazo", null=True, blank=True)
    concluida = models.BooleanField("Concluída", default=False)
    data_criacao = models.DateTimeField("Criada em", auto_now_add=True)

    def prazo_vencido(self):
        if self.prazo and not self.concluida:
            return self.prazo < timezone.now().date()
        return False

    def __str__(self):
        return self.titulo

    class Meta:
        ordering = ['prazo', '-data_criacao']
        verbose_name = "Tarefa"
        verbose_name_plural = "Tarefas"
```

---

## 8. Admin (`tarefas_app/admin.py`)

```python
from django.contrib import admin
from .models import Tarefa

@admin.register(Tarefa)
class TarefaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'prazo', 'concluida', 'prazo_vencido')
    list_filter = ('concluida', 'prazo')
    search_fields = ('titulo',)
    date_hierarchy = 'prazo'
```

---

## 9. URLs

### `config/urls.py`

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('tarefas_app.urls')),
]
```

### `tarefas_app/urls.py` (crie o arquivo)

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_tarefas, name='lista_tarefas'),
    path('toggle/<int:pk>/', views.toggle_concluida, name='toggle_concluida'),
    path('deletar/<int:pk>/', views.deletar_tarefa, name='deletar_tarefa'),
]
```

---

## 10. Views (`tarefas_app/views.py`)

```python
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from django.utils import timezone
from .models import Tarefa

def lista_tarefas(request):
    if request.method == 'POST':
        titulo = request.POST.get('titulo')
        prazo_str = request.POST.get('prazo')
        prazo = None
        if prazo_str:
            from datetime import datetime
            prazo = datetime.strptime(prazo_str, '%Y-%m-%d').date()
        if titulo:
            Tarefa.objects.create(titulo=titulo, prazo=prazo)
        return redirect('lista_tarefas')

    tarefas = Tarefa.objects.all()
    return render(request, 'tarefas_app/lista_tarefas.html', {
        'tarefas': tarefas,
        'hoje': timezone.now().date(),
    })

@require_POST
def toggle_concluida(request, pk):
    tarefa = get_object_or_404(Tarefa, pk=pk)
    tarefa.concluida = not tarefa.concluida
    tarefa.save()
     return redirect(request.POST.get('next', 'lista_tarefas'))

@require_POST
def deletar_tarefa(request, pk):
    tarefa = get_object_or_404(Tarefa, pk=pk)
    tarefa.delete()
    return redirect('lista_tarefas')
```

---

## 11. Templates (CRIAÇÃO AUTOMÁTICA)

1. Crie na pasta raiz a pasta `/templates/tarefas_app/`:
2. Depois crie na pasta `/templates/` o arquivo `base.html`

```html
<!doctype html>
<html lang="pt-br">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>{% block title %}Tarefas{% endblock %}</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/font/bootstrap-icons.min.css">
    <style>
        .vencida { color: #dc3545; font-weight: 600; }
        .task-done { text-decoration: line-through; opacity: 0.7; }
    </style>
</head>
<body class="bg-light">
    <nav class="navbar navbar-dark bg-primary mb-4 shadow">
        <div class="container">
            <a class="navbar-brand" href="{% url 'lista_tarefas' %}">
                Tarefas com Prazo
            </a>
        </div>
    </nav>
    <main class="container">{% block content %}{% endblock %}</main>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap bundle.min.js"></script>
</body>
</html>
```
3. Agora crie na pasta `/templates/tarefas_app/` o arquivo `lista_tarefas.html`
```html
{% extends 'base.html' %}
{% block title %}Minhas Tarefas{% endblock %}
{% block content %}
<div class="row justify-content-center">
    <div class="col-lg-8">
        <!-- Nova Tarefa -->
        <div class="card mb-4 shadow-sm">
            <div class="card-body">
                <h5 class="card-title">Nova Tarefa</h5>
                <form method="POST" class="row g-3">
                    {% csrf_token %}
                    <div class="col-md-7">
                        <input type="text" name="titulo" class="form-control" placeholder="O que precisa fazer?" required>
                    </div>
                    <div class="col-md-3">
                        <input type="date" name="prazo" class="form-control">
                    </div>
                    <div class="col-md-2">
                        <button class="btn btn-primary w-100">Adicionar</button>
                    </div>
                </form>
            </div>
        </div>

        <!-- Lista -->
        <div class="card shadow-sm">
            <div class="card-header bg-white">
                <h5 class="mb-0">Tarefas <span class="badge bg-secondary">{{ tarefas|length }}</span></h5>
            </div>
            <ul class="list-group list-group-flush">
                {% for t in tarefas %}
                <li class="list-group-item {% if t.prazo_vencido %}vencida{% endif %}">
                    <div class="d-flex align-items-center">
                        <form method="POST" action="{% url 'toggle_concluida' t.pk %}" class="me-3">
                            {% csrf_token %}
                            <input type="checkbox" class="btn-check" id="c{{ t.pk }}" {% if t.concluida %}checked{% endif %}>
                            <label class="btn btn-outline-success" for="c{{ t.pk }}"></label>
                        </form>
                        <div class="flex-grow-1 {% if t.concluida %}task-done{% endif %}">
                            <strong>{{ t.titulo }}</strong>
                            {% if t.prazo %}
                            <small class="d-block text-muted">
                                Prazo: {{ t.prazo|date:"d/m/Y" }}
                                {% if t.prazo_vencido %} <span class="text-danger fw-bold">(VENCIDA)</span>{% endif %}
                            </small>
                            {% endif %}
                        </div>
                        <form method="POST" action="{% url 'deletar_tarefa' t.pk %}"
                              onsubmit="return confirm('Excluir?');">
                            {% csrf_token %}
                            <button class="btn btn-sm btn-outline-danger"></button>
                        </form>
                    </div>
                </li>
                {% empty %}
                <li class="list-group-item text-center text-muted">Nenhuma tarefa ainda.</li>
                {% endfor %}
            </ul>
            <div class="card-footer text-center small text-muted">
                Hoje: {{ hoje|date:"d/m/Y" }}
            </div>
        </div>
    </div>
</div>
{% endblock %}

```

---

## 12. Migrações

```bash
poetry run python manage.py makemigrations
poetry run python manage.py migrate
poetry run python manage.py createsuperuser
```

---

## 13. Rodar

```bash
poetry run python manage.py runserver
```

Abrir: **http://127.0.0.1:8000**

---
