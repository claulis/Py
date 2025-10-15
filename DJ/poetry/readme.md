# Tutorial Poetry - Direto ao Ponto

## 1. O que é Poetry?

Poetry é um gerenciador de dependências Python que substitui pip + venv + setuptools. Gerencia dependências, resolve conflitos, cria ambientes virtuais e publica pacotes. Usa `pyproject.toml` como arquivo único de configuração e `poetry.lock` para versões exatas.

>Poetry elimina `requirements.txt`, `Pipfile`, `setup.py` e `venv` manual. Um comando faz tudo.

## 2. Instalação

Se estiver apenas com o `pip` instalado precisa atualizar o `pip` para o `pipx`

```bash
# Instala via pip
python -m pip install --user pipx
python -m pipx ensurepath

# Ou via winget (Windows 10+)
winget install pipx.pipx
```

Agora reinicie o Vs Code e execute o comando no terminal `pipx --version` para verificar a correta instalação

Se estiver correto agora pode-se instalar o poetry

```bash
pipx install poetry
poetry --version
poetry config virtualenvs.in-project true  # Cria .venv/ no projeto
```

## 3. Comandos Essenciais

### Iniciar Projeto

```bash
poetry new meu_projeto    # Cria estrutura completa
poetry init              # Inicializa diretório atual caso o projeto já exista
```

### Dependências

```bash
poetry add requests                    # Dependência principal
poetry add --group dev pytest          # Dependências de dev
poetry add "requests>=2.25,<3.0"       # Versão específica
poetry remove requests                 # Remove dependência
poetry install                         # Instala tudo
poetry install --no-dev                # Sem dev deps
```

### Execução

```bash
poetry shell               # Ativa ambiente virtual
poetry run python app.py   # Executa no ambiente
poetry run pytest          # Roda testes
poetry show --tree         # Mostra dependências
poetry env info            # Info do ambiente
```

### Lock e Update

```bash
poetry lock                # Gera/atualiza poetry.lock
poetry update              # Atualiza dependências
poetry update requests     # Atualiza pacote específico
```

## 4. pyproject.toml

`pyproject.toml` é o arquivo de configuração padrão do Python (PEP 518/621) que substitui setup.py, requirements.txt e outros arquivos fragmentados. É um arquivo TOML que centraliza toda a configuração do projeto Python.

```toml
[tool.poetry]
name = "meu-projeto"
version = "0.1.0"
description = "Descrição"
authors = ["Nome <email>"]
license = "MIT"
readme = "README.md"
packages = [{include = "meu_projeto"}]

[build-system]
requires = ["poetry-core>=1.0.0"]
build-backend = "poetry.core.masonry.api"

[tool.poetry.dependencies]
python = "^3.8"
requests = "^2.28.0"
flask = {version = "^2.0", optional = true}

[tool.poetry.group.dev.dependencies]
pytest = "^7.0"
black = "^22.0"
flake8 = "^5.0"

[tool.poetry.group.docs.dependencies]
sphinx = "^4.0"
mkdocs = "^1.2"

[tool.poetry.extras]
web = ["flask"]

[tool.poetry.scripts]
start = "meu_projeto.main:start"
test = "pytest"
```

### Explicação das Seções

- **`[tool.poetry]`**: Metadados do pacote (nome, versão, autor)
- **`[tool.poetry.dependencies]`**: Dependências de produção
- **`[tool.poetry.group.*.dependencies]`**: Grupos (dev, docs, test)
- **`[tool.poetry.extras]`**: Dependências opcionais
- **`[tool.poetry.scripts]`**: Comandos executáveis
- **`poetry.lock`**: Versões exatas de todas dependências (commit sempre)

## 6. Sintaxe de Versões

- `^2.28.0` = >=2.28.0 <3.0.0 (compatível)
- `~2.28.0` = >=2.28.0 <2.29.0 (patch only)
- `>=2.25,<3.0` = intervalo explícito
- `python = "^3.8"` = Python 3.8+

## 7. Workflow Completo

```bash
# 1. Iniciar
mkdir app && cd app
poetry init

# 2. Adicionar dependências
poetry add flask requests redis
poetry add --group dev pytest pytest-cov black

# 3. Instalar
poetry install

# 4. Usar
poetry run python -c "import flask; print('OK')"
poetry run pytest

# 5. Lock para produção
poetry lock --no-update
git add pyproject.toml poetry.lock
```

## Estrutura de Projeto

```plaintext
meu_projeto/
├── pyproject.toml
├── poetry.lock
├── README.md
├── src/
│   └── meu_projeto/
│       ├── __init__.py
│       └── main.py
├── tests/
│   └── test_main.py
└── .venv/  # Criado automaticamente
```

## Vantagens vs Pip

1. **Resolução automática de conflitos**
2. **Lockfile determinístico**
3. **Ambiente virtual automático**
4. **Um arquivo de configuração**
5. **Build e publish integrados**
6. **Grupos de dependências**
7. **Scripts declarativos**

## Dicas Importantes

- Sempre commit `pyproject.toml` e `poetry.lock`
- Nunca edite `poetry.lock` manualmente
- Use `--no-dev` em produção
- `poetry run` para comandos isolados
- `poetry shell` para desenvolvimento interativo
- Exporte requirements.txt só quando necessário (Docker)

