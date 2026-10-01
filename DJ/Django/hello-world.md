# Primeiro site em Django no Windows com VS Code

Passo a passo para instalar o Django no **Windows**, usando o **Visual Studio Code**, e criar uma página com um campo de texto e um botão. Ao clicar, a mesma página mostra **"Hello, <nome>!"**.


## Instalar as extensões
 
Abra o VS Code, clique no ícone de extensões (`Ctrl + Shift + X`) e instale:
 
| Extensão | Autor | Para que serve |
|---|---|---|
| **Python** | Microsoft | Suporte a Python, seleção de interpretador e debug |
| **Django** | Baptiste Darthenay | Realce de sintaxe e snippets para templates `{% %}` (opcional) |
---

## Criar o projeto

### Criar e abrir a pasta

Pelo Explorador de Arquivos, crie uma pasta, por exemplo `C:\projetos\meu_site`. Depois:

- Clique com o botão direito na pasta > **Abrir com Code**, ou
- No VS Code: **Arquivo > Abrir Pasta...** e selecione a pasta.

Se preferir pelo terminal:

```powershell
mkdir C:\projetos\meu_site
cd C:\projetos\meu_site
code .
```

### Abrir o terminal integrado

No VS Code, use o atalho `` Ctrl + ` `` (crase) ou o menu **Terminal > Novo Terminal**. Ele abre já dentro da pasta do projeto, normalmente em PowerShell.

### Criar o ambiente virtual

```powershell
python -m venv venv
```

Isso cria a pasta `venv` com uma cópia isolada do Python para este projeto.

### Selecionar o interpretador no VS Code

1. Pressione `Ctrl + Shift + P` para abrir a Paleta de Comandos.
2. Digite **Python: Select Interpreter** e pressione Enter.
3. Escolha o que tem `.\venv\Scripts\python.exe`.

Se o VS Code perguntar sobre o novo ambiente virtual, clique em **Sim**.

### Ativar o ambiente virtual

Feche o terminal atual (ícone da lixeira) e abra um novo com `` Ctrl + ` ``. Com o interpretador selecionado, o VS Code costuma ativar o venv automaticamente. Você deve ver `(venv)` no início da linha.

Se não aparecer, ative manualmente:

```powershell
.\venv\Scripts\Activate.ps1
```

**Erro "a execução de scripts foi desabilitada neste sistema"?** Rode uma vez:

```powershell
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
```

Confirme com `S` e ative novamente. Alternativa: troque o terminal para **Command Prompt** (seta ao lado do `+` no painel do terminal > **Command Prompt**) e use `venv\Scripts\activate.bat`.

### Instalar o Django

```powershell
pip install django
```

Verifique:

```powershell
python -m django --version
```

### Criar o projeto Django

```powershell
django-admin startproject config .
```

- `config` é o nome da pasta de configurações.
- O ponto final (`.`) cria o projeto na pasta atual, sem uma subpasta extra.

### Criar a aplicação

```powershell
python manage.py startapp hello
```

No painel **Explorer** do VS Code (`Ctrl + Shift + E`) você deve ver:

```
MEU_SITE
├── config/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
├── hello/
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   └── views.py
├── venv/
└── manage.py
```

---

## Escrever o código

### Registrar a app no projeto

Abra `config/settings.py` e adicione `'hello'` ao final de `INSTALLED_APPS`:

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'hello',  # <- nossa app
]
```

### Criar a view

Abra `hello/views.py` e substitua o conteúdo por:

```python
from django.shortcuts import render


def index(request):
    nome = ""

    if request.method == "POST":
        nome = request.POST.get("nome", "").strip()

    return render(request, "hello/index.html", {"nome": nome})
```

**Como funciona:**

1. Ao abrir a página, o navegador faz uma requisição `GET`. O `nome` fica vazio.
2. Ao clicar no botão, o navegador faz uma requisição `POST`. A view lê o campo `nome`.
3. Nos dois casos a view devolve o mesmo template, passando `nome` como variável.

### Criar as rotas da app

No Explorer, clique com o botão direito na pasta `hello` > **Novo Arquivo** e nomeie como `urls.py`. Conteúdo:

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
]
```

### Ligar as rotas da app ao projeto

Abra `config/urls.py` e deixe assim:

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('hello.urls')),
]
```

### Criar o template

No Explorer, crie esta estrutura de pastas e arquivo:

```
hello/
└── templates/
    └── hello/
        └── index.html
```

**Dica no VS Code:** clique com o botão direito em `hello` > **Nova Pasta** > `templates`. Depois clique com o botão direito em `templates` > **Nova Pasta** > `hello`. Por fim, em `hello` (a interna) > **Novo Arquivo** > `index.html`.

Ou pelo terminal:

```powershell
mkdir hello	emplates\hello
New-Item hello	emplates\hello\index.html
```

Conteúdo do `index.html`:

```html
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Hello Django</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background: #f4f6f8;
            margin: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
        }
        .card {
            background: #fff;
            padding: 32px 40px;
            border-radius: 12px;
            box-shadow: 0 4px 16px rgba(0, 0, 0, 0.1);
            text-align: center;
            width: 320px;
        }
        h1 {
            margin-top: 0;
            color: #0c4b33;
        }
        input {
            width: 100%;
            padding: 10px;
            margin-bottom: 12px;
            border: 1px solid #ccc;
            border-radius: 6px;
            box-sizing: border-box;
            font-size: 16px;
        }
        button {
            width: 100%;
            padding: 10px;
            background: #0c4b33;
            color: #fff;
            border: none;
            border-radius: 6px;
            font-size: 16px;
            cursor: pointer;
        }
        button:hover {
            background: #093826;
        }
        .resultado {
            margin-top: 20px;
            font-size: 20px;
            color: #222;
        }
    </style>
</head>
<body>
    <div class="card">
        <h1>Meu primeiro Django</h1>

        <form method="post">
            {% csrf_token %}
            <input type="text" name="nome" placeholder="Digite seu nome" required>
            <button type="submit">Enviar</button>
        </form>

        {% if nome %}
            <p class="resultado">Hello, {{ nome }}!</p>
        {% endif %}
    </div>
</body>
</html>
```

**Pontos importantes:**

| Trecho | Função |
|---|---|
| `<form method="post">` | Envia os dados para a mesma página usando POST |
| `{% csrf_token %}` | Token de segurança obrigatório em formulários POST. Sem ele o Django retorna erro 403 |
| `name="nome"` | É o nome que a view lê em `request.POST.get("nome")` |
| `{% if nome %} ... {% endif %}` | Só mostra o resultado se houver um nome |
| `{{ nome }}` | Imprime o valor da variável enviada pela view |

> O Django escapa automaticamente o conteúdo de `{{ nome }}`, o que protege contra injeção de HTML e JavaScript.

### Salvar tudo

Use `Ctrl + K` e depois `S` para salvar todos os arquivos, ou ative **Arquivo > Salvamento Automático**. Arquivos não salvos aparecem com um ponto no lugar do `X` na aba.

---

## Rodar o site

No terminal integrado (com `(venv)` ativo):

```powershell
python manage.py runserver
```

Mantenha `Ctrl` pressionado e clique no link `http://127.0.0.1:8000/` que aparece no terminal, ou abra manualmente no navegador.

Digite um nome, clique em **Enviar** e veja **Hello, <nome>!** abaixo do botão.

Para parar o servidor: `Ctrl + C` no terminal.

> O servidor reinicia sozinho quando você salva alterações em arquivos `.py`. Em arquivos `.html` basta atualizar a página (`F5`).

> Na primeira execução o terminal pode avisar sobre "unapplied migrations". É normal e não afeta este exemplo. Se quiser aplicar, rode `python manage.py migrate`.

---

## Evoluindo o projeto

O site já funciona. Agora vamos melhorá-lo em duas etapas pequenas, sem mudar o comportamento: primeiro tiramos o CSS de dentro do HTML, depois separamos a estrutura comum da página em um template base. Mantenha o servidor rodando e atualize o navegador a cada etapa para confirmar que a página continua igual.

### Etapa 1: Separar o CSS em um arquivo estático

Arquivos CSS, JavaScript e imagens ficam em uma pasta `static/` dentro da app. O Django já a encontra sozinho, porque `django.contrib.staticfiles` está em `INSTALLED_APPS` e o `STATIC_URL` já vem configurado no `settings.py`.

**1. Criar a estrutura**

```
hello/
└── static/
    └── hello/
        └── style.css
```

Pelo terminal:

```powershell
mkdir hello\static\hello
New-Item hello\static\hello\style.css
```

> A subpasta repetida (`static/hello/`) evita conflito de nomes caso outra app também tenha um `style.css`. É a mesma lógica da pasta `templates/hello/`.

**2. Mover o CSS**

Recorte tudo o que está entre `<style>` e `</style>` no `index.html` (sem as tags) e cole no `style.css`, tirando a indentação extra:

```css
body {
    font-family: Arial, sans-serif;
    background: #f4f6f8;
    margin: 0;
    display: flex;
    justify-content: center;
    align-items: center;
    min-height: 100vh;
}

.card {
    background: #fff;
    padding: 32px 40px;
    border-radius: 12px;
    box-shadow: 0 4px 16px rgba(0, 0, 0, 0.1);
    text-align: center;
    width: 320px;
}

h1 {
    margin-top: 0;
    color: #0c4b33;
}

input {
    width: 100%;
    padding: 10px;
    margin-bottom: 12px;
    border: 1px solid #ccc;
    border-radius: 6px;
    box-sizing: border-box;
    font-size: 16px;
}

button {
    width: 100%;
    padding: 10px;
    background: #0c4b33;
    color: #fff;
    border: none;
    border-radius: 6px;
    font-size: 16px;
    cursor: pointer;
}

button:hover {
    background: #093826;
}

.resultado {
    margin-top: 20px;
    font-size: 20px;
    color: #222;
}
```

**3. Ligar o CSS ao template**

No `index.html`, adicione `{% load static %}` na primeira linha e troque o bloco `<style>...</style>` por um `<link>`:

```html
{% load static %}
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Hello Django</title>
    <link rel="stylesheet" href="{% static 'hello/style.css' %}">
</head>
<body>
    <div class="card">
        <h1>Meu primeiro Django</h1>

        <form method="post">
            {% csrf_token %}
            <input type="text" name="nome" placeholder="Digite seu nome" required>
            <button type="submit">Enviar</button>
        </form>

        {% if nome %}
            <p class="resultado">Hello, {{ nome }}!</p>
        {% endif %}
    </div>
</body>
</html>
```

| Trecho | Função |
|---|---|
| `{% load static %}` | Habilita a tag `{% static %}`. Precisa vir no topo de todo template que a usa |
| `{% static 'hello/style.css' %}` | Gera a URL do arquivo (`/static/hello/style.css`) |

**4. Testar**

Pare o servidor (`Ctrl + C`) e inicie de novo com `python manage.py runserver`. O servidor só descobre a pasta `static/` ao iniciar. Atualize a página com `Ctrl + F5` (sem cache). Ela deve ficar idêntica a antes, mas agora o estilo vem de um arquivo separado.

### Etapa 2: Criar um template base com `{% extends %}`

Quando o site tiver mais páginas, todas repetirão o mesmo `<head>`, o mesmo CSS e a mesma estrutura. O template base guarda essa parte comum, e cada página só preenche o que muda.

**1. Criar o `base.html`**

Crie `hello/templates/hello/base.html`:

```powershell
New-Item hello\templates\hello\base.html
```

```html
{% load static %}
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{% block title %}Hello Django{% endblock %}</title>
    <link rel="stylesheet" href="{% static 'hello/style.css' %}">
</head>
<body>
    <div class="card">
        {% block content %}{% endblock %}
    </div>
</body>
</html>
```

- `{% block title %}` e `{% block content %}` são os pontos que as páginas filhas podem preencher.
- O texto dentro de `{% block title %}...{% endblock %}` é o valor padrão, usado se a página filha não definir o bloco.

**2. Simplificar o `index.html`**

Substitua todo o conteúdo do `index.html` por:

```html
{% extends "hello/base.html" %}

{% block title %}Hello Django{% endblock %}

{% block content %}
    <h1>Meu primeiro Django</h1>

    <form method="post">
        {% csrf_token %}
        <input type="text" name="nome" placeholder="Digite seu nome" required>
        <button type="submit">Enviar</button>
    </form>

    {% if nome %}
        <p class="resultado">Hello, {{ nome }}!</p>
    {% endif %}
{% endblock %}
```

| Trecho | Função |
|---|---|
| `{% extends "hello/base.html" %}` | Herda a estrutura do template base. Deve ser a **primeira linha** do arquivo |
| `{% block content %} ... {% endblock %}` | Substitui o bloco `content` do base pelo conteúdo desta página |

> Tudo o que estiver fora de um `{% block %}` em uma página filha é ignorado.

**3. Testar**

Atualize a página (`F5`). O resultado visual é o mesmo. Para ver a vantagem, crie uma segunda página que reaproveita o `base.html` com apenas algumas linhas, por exemplo `sobre.html`, que só define o `title` e o `content`.

### Como ficou

```
hello/
├── views.py
├── urls.py
├── static/
│   └── hello/
│       └── style.css
└── templates/
    └── hello/
        ├── base.html
        └── index.html
```

```
Navegador  --GET /------------------------>  views.index  --> index.html (extends base.html)
Navegador  --GET /static/hello/style.css-->  arquivo CSS servido pelo staticfiles
```

O `index.html` herda o `base.html` (`{% extends %}`), e o `base.html` aponta para o CSS com `{% static %}`. Por isso o navegador faz uma segunda requisição para buscar o `style.css`.

---

## : Configurações úteis do VS Code

### 5.1 Reconhecer templates Django no HTML

Com a extensão **Django** instalada, associe os templates à linguagem `django-html`. Abra `Ctrl + Shift + P` > **Preferences: Open Workspace Settings (JSON)** e adicione:

```json
{
    "files.associations": {
        "**/templates/**/*.html": "django-html"
    },
    "emmet.includeLanguages": {
        "django-html": "html"
    }
}
```

Isso dá realce para `{% %}` e `{{ }}` e mantém os atalhos Emmet (como digitar `!` + `Tab`) funcionando.

### Rodar com o depurador (F5)

1. Abra a aba **Executar e Depurar** (`Ctrl + Shift + D`).
2. Clique em **criar um arquivo launch.json**.
3. Escolha **Python Debugger** > **Django**.

O VS Code gera um `.vscode/launch.json` parecido com este:

```json
{
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Python Debugger: Django",
            "type": "debugpy",
            "request": "launch",
            "args": ["runserver"],
            "django": true,
            "autoStartBrowser": false,
            "program": "${workspaceFolder}\\manage.py"
        }
    ]
}
```

Agora `F5` inicia o servidor em modo debug. Clique na margem esquerda de uma linha da `views.py` para criar um ponto de parada (breakpoint) e acompanhe o valor de `nome` quando enviar o formulário.

---

## Estrutura final

```
meu_site/
├── .vscode/              (opcional)
│   ├── launch.json
│   └── settings.json
├── venv/
├── manage.py
├── config/
│   ├── settings.py
│   ├── urls.py
│   └── ...
└── hello/
    ├── views.py
    ├── urls.py
    └── templates/
        └── hello/
            └── index.html
```

---

## Como o fluxo funciona

```
Navegador  --GET /------------>  config/urls.py > hello/urls.py > views.index
Navegador  <-- index.html (sem nome) --------------------------------------

Navegador  --POST (nome=Ana)-->  config/urls.py > hello/urls.py > views.index
Navegador  <-- index.html ("Hello, Ana!") ---------------------------------
```

---

## Problemas comuns no Windows

| Erro | Causa provável | Solução |
|---|---|---|
| `'python' não é reconhecido como comando` | Python fora do PATH | Reinstale marcando **Add python.exe to PATH**, ou use `py` |
| Abre a Microsoft Store ao digitar `python` | Alias de execução da Store | Desative os aliases `python.exe` e `python3.exe` nas Configurações do Windows |
| `a execução de scripts foi desabilitada` | Política do PowerShell | `Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned` |
| `(venv)` não aparece no terminal | Interpretador não selecionado | `Ctrl + Shift + P` > **Python: Select Interpreter** e abra um terminal novo |
| `ModuleNotFoundError: No module named 'django'` | Django instalado fora do venv ou venv inativo | Ative o venv e rode `pip install django` de novo |
| `'code' não é reconhecido` | VS Code fora do PATH | Reinstale o VS Code marcando **Adicionar ao PATH**, ou abra a pasta pelo menu **Arquivo > Abrir Pasta** |
| `TemplateDoesNotExist` | Pasta do template errada ou app não registrada | Confirme `hello/templates/hello/index.html` e o `INSTALLED_APPS` |
| `Invalid block tag: 'static'` | Faltou `{% load static %}` | Adicione `{% load static %}` no topo do template |
| `extends must be the first tag` | Algo vem antes do `{% extends %}` | Deixe `{% extends %}` como primeira linha do `index.html` |
| Página sem estilo (CSS não carrega) | Caminho do `static` errado ou servidor iniciado antes da pasta | Confirme `hello/static/hello/style.css`, reinicie o servidor e use `Ctrl + F5` |
| `403 CSRF verification failed` | Faltou `{% csrf_token %}` | Adicione a tag dentro do `<form>` |
| `Page not found (404)` | Rotas não ligadas | Confira `hello/urls.py` e o `include` em `config/urls.py` |
| `Error: That port is already in use` | Outro servidor rodando | Use `python manage.py runserver 8080` |
| Sublinhado amarelo em `from django...` | VS Code usando outro interpretador | Selecione o interpretador do `venv` (passo 2.4) |

---

## Resumo dos comandos

```powershell
mkdir C:\projetos\meu_site
cd C:\projetos\meu_site
code .

python -m venv venv
.\venv\Scripts\Activate.ps1
pip install django

django-admin startproject config .
python manage.py startapp hello

# editar settings.py, views.py, urls.py (hello e config) e criar o template

python manage.py runserver
```

---


