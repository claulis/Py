# Website Django no Windows com VS Code usando Poetry

[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)](https://www.djangoproject.com/)
[![Poetry](https://img.shields.io/badge/Poetry-60A5FA?style=for-the-badge&logo=poetry&logoColor=white)](https://python-poetry.org/)
[![Bootstrap](https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white)](https://getbootstrap.com/)
[![VS Code](https://img.shields.io/badge/VS%20Code-007ACC?style=for-the-badge&logo=visual-studio-code&logoColor=white)](https://code.visualstudio.com/)

## Índice

1. [Configuração do Ambiente com Poetry](#configuração-do-ambiente-com-poetry)
2. [Criação do Projeto Django](#criação-do-projeto-django)
3. [Estrutura do Projeto](#estrutura-do-projeto)
4. [Implementação das Páginas](#implementação-das-páginas)
5. [Execução Local](#execução-local)
6. [Solução de Problemas](#solução-de-problemas)

## Configuração do Ambiente com Poetry

### 1. Instalar Poetry

1. **Instalar Poetry (Método recomendado):**

   ```cmd
   curl -sSL https://install.python-poetry.org | python3 -
   ```

   **Ou usando pip (alternativo):**

   ```cmd
   pip install poetry
   ```

   **Ou usando pipx (alternativo):**

   ```cmd
   pipx install poetry
   ```

2. **Verificar instalação:**

   ```cmd
   poetry --version
   ```

3. **Configurar Poetry (opcional):**

   ```cmd
   # Criar ambientes virtuais dentro do projeto
   poetry config virtualenvs.in-project true
   ```

### 2. Criar pasta do projeto

```cmd
mkdir meu_projeto_django
cd meu_projeto_django
```

### 3. Inicializar projeto Poetry

```cmd
poetry init
```

Durante a inicialização, responda as perguntas:

- **Package name:** exemplo-django
- **Version:** 0.1.0
- **Description:** Website Django de exemplo
- **Author:** Seu Nome <seu.email@exemplo.com>
- **License:** MIT
- **Compatible Python versions:** ^3.8
- **Define main dependencies interactively:** n
- **Define development dependencies interactively:** n
- **Do you confirm generation:** yes

### 3. Adicionar Django como dependência

```cmd
poetry add django
```

### 4. Ativar ambiente virtual

```cmd
poetry env activate
```

**Nota:** Você deve ver o nome do ambiente virtual no início da linha de comando quando estiver ativo.

### 5. Verificar instalação

```cmd
poetry jango-admin --version
```

## Criação do Projeto Django

### 1. Criar projeto Django

```cmd
poetry run django-admin startproject exemplo_django .
```

### 2. Criar aplicação

```cmd
poetry run python manage.py startapp saudacao
```

### 3. Abrir no VS Code

```cmd
code .
```

## Estrutura do Projeto

Após os comandos acima, sua estrutura deve ficar assim:

```plaintext
meu_projeto_django/
├── .venv/                    # Ambiente virtual do Poetry
├── exemplo_django/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── saudacao/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   └── views.py
├── pyproject.toml           # Arquivo de configuração do Poetry
├── poetry.lock             # Lock file das dependências
└── manage.py
```

## Implementação das Páginas

### 1. Configurar settings.py

Edite `exemplo_django/settings.py` e adicione a aplicação:

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'saudacao',  # Adicione esta linha
]
```

### 2. Criar formulário (saudacao/forms.py)

Crie o arquivo `saudacao/forms.py`:

```python
from django import forms
import re

class NomeForm(forms.Form):
    nome = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Digite seu nome'
        }),
        label='Nome'
    )
    
    def clean_nome(self):
        nome = self.cleaned_data['nome']
        # Validar se contém apenas letras e espaços
        if not re.match("^[a-zA-ZÀ-ÿ\s]+$", nome):
            raise forms.ValidationError("O nome deve conter apenas letras.")
        return nome
```

### 3. Criar views (saudacao/views.py)

Edite `saudacao/views.py`:

```python
from django.shortcuts import render, redirect
from .forms import NomeForm

def pagina_inicial(request):
    if request.method == 'POST':
        form = NomeForm(request.POST)
        if form.is_valid():
            nome = form.cleaned_data['nome']
            return redirect('saudacao', nome=nome)
    else:
        form = NomeForm()
    
    return render(request, 'saudacao/inicial.html', {'form': form})

def pagina_saudacao(request, nome):
    return render(request, 'saudacao/saudacao.html', {'nome': nome})
```

### 4. Configurar URLs

**Criar `saudacao/urls.py`:**

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.pagina_inicial, name='inicial'),
    path('saudacao/<str:nome>/', views.pagina_saudacao, name='saudacao'),
]
```

**Editar `exemplo_django/urls.py`:**

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('saudacao.urls')),
]
```

### 5. Criar templates

**Criar pasta de templates:**

```cmd
mkdir saudacao\templates
mkdir saudacao\templates\saudacao
```

**Criar template base (`saudacao/templates/saudacao/base.html`):**

```html
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{% block title %}Exemplo Django{% endblock %}</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet">
    <style>
        .banner {
            background-color: #007bff;
            color: white;
            padding: 20px;
            text-align: center;
            margin-bottom: 30px;
        }
        .container-custom {
            max-width: 600px;
            margin: 0 auto;
            padding: 20px;
        }
    </style>
</head>
<body>
    <div class="banner">
        <h1>Exemplo em Django</h1>
    </div>
    
    <div class="container-custom">
        {% block content %}
        {% endblock %}
    </div>
    
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>
```

**Criar página inicial (`saudacao/templates/saudacao/inicial.html`):**

```html
{% extends 'saudacao/base.html' %}

{% block title %}Página Inicial - Exemplo Django{% endblock %}

{% block content %}
<div class="card">
    <div class="card-header">
        <h2>Digite seu nome</h2>
    </div>
    <div class="card-body">
        <form method="post">
            {% csrf_token %}
            <div class="mb-3">
                {{ form.nome.label_tag }}
                {{ form.nome }}
                {% if form.nome.errors %}
                    <div class="alert alert-danger mt-2">
                        {{ form.nome.errors }}
                    </div>
                {% endif %}
            </div>
            <button type="submit" class="btn btn-primary">Dizer Olá</button>
        </form>
    </div>
</div>
{% endblock %}
```

**Criar página de saudação (`saudacao/templates/saudacao/saudacao.html`):**

```html
{% extends 'saudacao/base.html' %}

{% block title %}Saudação - Exemplo Django{% endblock %}

{% block content %}
<div class="card">
    <div class="card-header">
        <h2>Saudação</h2>
    </div>
    <div class="card-body text-center">
        <h3 class="text-success">Olá, {{ nome }}!</h3>
        <p class="mt-3">É um prazer conhecê-lo!</p>
        <a href="{% url 'inicial' %}" class="btn btn-secondary">Voltar</a>
    </div>
</div>
{% endblock %}
```

## Execução Local

### 1. Aplicar migrações

```cmd
poetry run python manage.py migrate
```

### 2. Executar servidor de desenvolvimento

```cmd
poetry run python manage.py runserver
```

### 3. Acessar o site

Abra seu navegador e acesse: `http://127.0.0.1:8000/`

### 4. Parar o servidor

Pressione `Ctrl + C` no terminal

## Funcionalidades Implementadas

✅ **Página inicial com input para nome**
✅ **Botão "Dizer Olá"**
✅ **Validação do input (apenas letras)**
✅ **Página de saudação personalizada**
✅ **Template com banner "Exemplo em Django"**
✅ **Design responsivo com Bootstrap**
✅ **Gerenciamento de dependências com Poetry**

## Comandos Úteis com Poetry

### Ativar ambiente virtual

```cmd
poetry shell
```

### Desativar ambiente virtual

```cmd
exit
```

### Adicionar nova dependência

```cmd
poetry add nome-do-pacote
```

### Adicionar dependência de desenvolvimento

```cmd
poetry add --group dev nome-do-pacote
```

### Instalar todas as dependências

```cmd
poetry install
```

### Atualizar dependências

```cmd
poetry update
```

### Mostrar dependências instaladas

```cmd
poetry show
```

### Executar comandos no ambiente virtual

```cmd
poetry run python manage.py comando
```

### Gerar requirements.txt (se necessário)

```cmd
poetry export -f requirements.txt --output requirements.txt
```

### Remover dependência

```cmd
poetry remove nome-do-pacote
```

## Arquivo pyproject.toml

Após seguir os passos, seu `pyproject.toml` deve ficar assim:

```toml
[tool.poetry]
name = "exemplo-django"
version = "0.1.0"
description = "Website Django de exemplo"
authors = ["Seu Nome <seu.email@exemplo.com>"]
license = "MIT"
readme = "README.md"

[tool.poetry.dependencies]
python = "^3.8"
django = "^4.2.0"

[tool.poetry.group.dev.dependencies]

[build-system]
requires = ["poetry-core"]
build-backend = "poetry.core.masonry.api"
```

## Solução de Problemas

### Problema: "poetry não é reconhecido"

**Solução:**

1. Reinicie o terminal após a instalação
2. Verifique se Poetry foi adicionado ao PATH
3. Tente reinstalar usando o método oficial

### Problema: Erro de permissão no PowerShell

**Solução:** Execute o PowerShell como administrador e execute:

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### Problema: Poetry não encontra Python

**Solução:**

```cmd
poetry env use python
```

### Problema: Dependências não instaladas

**Solução:**

```cmd
poetry install --no-root
```

### Problema: Página não carrega

**Solução:**

1. Verifique se o servidor está rodando (`poetry run python manage.py runserver`)
2. Confirme o endereço: `http://127.0.0.1:8000/`
3. Verifique se não há erros no terminal

### Problema: Template não encontrado

**Solução:** Verifique se a pasta `templates` foi criada no local correto e se a aplicação foi adicionada em `INSTALLED_APPS`.

## Vantagens do Poetry

✅ **Gerenciamento simplificado de dependências**
✅ **Resolução automática de conflitos**
✅ **Lock file para reprodutibilidade**
✅ **Ambientes virtuais automáticos**
✅ **Publicação de pacotes facilitada**
✅ **Configuração em arquivo único (pyproject.toml)**

## Próximos Passos

Após implementar este exemplo básico, você pode:

1. **Adicionar dependências de desenvolvimento:**

   ```cmd
   poetry add --group dev pytest django-debug-toolbar
   ```

2. **Implementar testes:**

   ```cmd
   poetry add --group dev pytest-django
   ```

3. **Adicionar linting:**

   ```cmd
   poetry add --group dev flake8 black
   ```

4. **Configurar pre-commit hooks**
5. **Deploy para produção**

## Estrutura Final do Projeto

```plaintext
meu_projeto_django/
├── .venv/                    # Ambiente virtual do Poetry
├── exemplo_django/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── saudacao/
│   ├── templates/
│   │   └── saudacao/
│   │       ├── base.html
│   │       ├── inicial.html
│   │       └── saudacao.html
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── pyproject.toml           # Configuração do Poetry
├── poetry.lock             # Lock file das dependências
└── manage.py
```

### **exemplo_django/** - Pasta do PROJETO Django

Esta é a pasta principal do projeto Django que contém:

- `settings.py` - Configurações globais do projeto
- `urls.py` - URLs principais do projeto (roteamento geral)
- `wsgi.py` - Configuração para deploy em produção
- `__init__.py` - Marca como pacote Python

**Função:** Gerencia configurações globais, URLs principais e coordena todas as aplicações.

### **saudacao/** - Pasta da APLICAÇÃO Django

Esta é uma aplicação específica dentro do projeto que contém:

- `views.py` - Lógica das páginas (funções que processam requests)
- `urls.py` - URLs específicas desta aplicação
- `models.py` - Modelos de dados (tabelas do banco)
- `forms.py` - Formulários (validação de dados)
- `templates/` - Templates HTML desta aplicação

**Função:** Implementa uma funcionalidade específica (no caso, o sistema de saudação).

### **Por que duas pastas?**

**Django segue o conceito de "Projeto vs Aplicações":**

**UM PROJETO** pode ter **VÁRIAS APLICAÇÕES** onde cada aplicação tem uma responsabilidade específica e isso permite reutilização e organização modular

**Exemplo prático:**

```plaintext
meu_site_django/           # Projeto principal
├── exemplo_django/        # Configurações do projeto
├── saudacao/             # App: sistema de saudação
├── blog/                 # App: sistema de blog
├── loja/                 # App: sistema de e-commerce
└── usuarios/             # App: sistema de usuários
```

## **Poderia ter apenas uma pasta?**

**Tecnicamente sim, mas não é recomendado** porque:

- ❌ Mistura configurações globais com lógica específica
- ❌ Dificulta manutenção em projetos maiores
- ❌ Impede reutilização de código
- ❌ Vai contra as boas práticas do Django
