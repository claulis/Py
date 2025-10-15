
# Projeto Django com Poetry

## 1. Criar o Projeto com Poetry

```bash
poetry new meu_projeto_django
cd meu_projeto_django
```

> Isso cria a estrutura básica do projeto com `pyproject.toml`.

## 2. Adicionar Django como Dependência

```bash
poetry add django
```

## 3. Ativar o Ambiente Virtual

```bash
poetry shell
```

## 4. Criar o Projeto Django

```bash
django-admin startproject config .
```

> O ponto final (`.`) garante que os arquivos do Django sejam criados na raiz do projeto.

## 5. Configurar o Banco de Dados

```bash
python manage.py migrate
```

## 6. Criar Superusuário

```bash
python manage.py createsuperuser
```

## 7. Rodar o Servidor

```bash
python manage.py runserver
```

Acesse: [http://127.0.0.1:8000](http://127.0.0.1:8000)

## 8. Criar um App Django

```bash
python manage.py startapp core
```

Adicione `'core'` em `INSTALLED_APPS` no `config/settings.py`.

---

## 9. Estrutura Final Esperada

```
meu_projeto_django/
├── config/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── core/
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   └── views.py
├── pyproject.toml
└── manage.py
```

