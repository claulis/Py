# Tutorial uv - Direto ao Ponto (Windows + VS Code)

## 1. O que é uv?

uv é um gerenciador de pacotes e projetos Python escrito em Rust, criado pela Astral (a mesma equipe do Ruff). Ele substitui `pip`, `venv`, `pip-tools`, `pipx`, `pyenv` e boa parte do Poetry em uma única ferramenta, e é muito mais rápido.

O uv:

- Instala e gerencia versões do Python
- Cria ambientes virtuais (`.venv`) automaticamente
- Resolve dependências e gera lockfile (`uv.lock`)
- Usa o `pyproject.toml` padrão (PEP 621)
- Executa ferramentas isoladas (`uvx`, equivalente ao `pipx`)

> Você não precisa ter Python instalado antes: o uv baixa o Python que o projeto precisa.

## 2. Instalação no Windows

Abra o **PowerShell** (ou o terminal integrado do VS Code com `` Ctrl+` ``) e execute uma das opções:

```powershell
# Opção 1: winget (recomendada)
winget install --id=astral-sh.uv -e

# Opção 2: instalador oficial
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"

# Opção 3: via pip (se já tiver Python)
pip install uv
```

Feche e reabra o VS Code (para atualizar o `PATH`) e verifique:

```powershell
uv --version
```

Para atualizar o uv no futuro:

```powershell
uv self update   # instalador oficial
winget upgrade astral-sh.uv   # se instalou via winget
```

## 3. Preparando o VS Code

1. Instale a extensão **Python** (Microsoft) e a **Pylance**.
2. Opcional: instale a extensão **Even Better TOML** para editar o `pyproject.toml`.
3. Abra a pasta do projeto (`File > Open Folder`).
4. Selecione o interpretador: `Ctrl+Shift+P` → **Python: Select Interpreter** → escolha o `.venv\Scripts\python.exe` do projeto.

O VS Code detecta o `.venv` na raiz do projeto automaticamente e ativa o ambiente em novos terminais.

> **Erro de execução de scripts no PowerShell?** Se aparecer "a execução de scripts foi desabilitada neste sistema" ao ativar o `.venv`, rode uma vez:
> `Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned`
> Ou evite o problema usando sempre `uv run`, que não exige ativar o ambiente.

## 4. Comandos Essenciais

### Iniciar projeto

```powershell
uv init meu_projeto        # Cria pasta nova com projeto
cd meu_projeto
code .                     # Abre no VS Code

uv init                    # Inicializa na pasta atual (projeto já existente)
uv init --python 3.12      # Define a versão do Python
```

Arquivos criados: `pyproject.toml`, `main.py`, `README.md`, `.python-version` e `.gitignore`. O `.venv` e o `uv.lock` aparecem no primeiro `uv add` ou `uv run`.

### Dependências

```powershell
uv add requests                    # Dependência principal
uv add --dev pytest                # Dependência de desenvolvimento
uv add "requests>=2.25,<3.0"       # Versão específica
uv add --group docs mkdocs         # Grupo personalizado
uv add --optional web flask        # Dependência opcional (extra)
uv remove requests                 # Remove dependência
uv sync                            # Instala tudo conforme o lockfile
uv sync --no-dev                   # Sem dependências de dev (produção)
```

### Execução

```powershell
uv run python main.py      # Executa no ambiente do projeto
uv run pytest              # Roda testes
uv run ruff check .        # Roda qualquer ferramenta instalada
uv tree                    # Mostra árvore de dependências
uv pip list                # Lista pacotes instalados
```

`uv run` cria o ambiente e sincroniza as dependências se necessário. Não é preciso ativar o `.venv` manualmente.

### Lock e atualização

```powershell
uv lock                              # Gera/atualiza uv.lock
uv lock --upgrade                    # Atualiza todas as versões permitidas
uv lock --upgrade-package requests   # Atualiza um pacote específico
```

### Gerenciar versões do Python

```powershell
uv python list             # Versões disponíveis
uv python install 3.12     # Baixa e instala o Python 3.12
uv python pin 3.12         # Fixa a versão no projeto (.python-version)
```

### Ferramentas globais (substitui o pipx)

```powershell
uv tool install ruff       # Instala ferramenta de forma isolada
uvx ruff check .           # Executa sem instalar (tool run)
uv tool list               # Lista ferramentas instaladas
```

## 5. pyproject.toml

O uv usa o formato padrão do Python (PEP 621), sem seções `[tool.poetry]`:

```toml
[project]
name = "meu-projeto"
version = "0.1.0"
description = "Descrição"
readme = "README.md"
requires-python = ">=3.12"
license = { text = "MIT" }
authors = [{ name = "Nome", email = "email@exemplo.com" }]
dependencies = [
    "requests>=2.28.0",
]

[project.optional-dependencies]
web = ["flask>=2.0"]

[dependency-groups]
dev = [
    "pytest>=7.0",
    "ruff>=0.5",
]
docs = [
    "mkdocs>=1.2",
]

[project.scripts]
start = "meu_projeto.main:start"
```

### Explicação das seções

- **`[project]`**: Metadados e dependências de produção
- **`[project.optional-dependencies]`**: Extras opcionais, publicados com o pacote
- **`[dependency-groups]`**: Grupos locais (dev, docs, test), não vão para o pacote publicado
- **`[project.scripts]`**: Comandos executáveis
- **`uv.lock`**: Versões exatas de todas as dependências (sempre no Git)

## 6. Sintaxe de Versões

O uv usa a sintaxe padrão PEP 440 (diferente do `^` do Poetry):

- `>=2.28.0,<3.0.0` = compatível (equivale ao `^2.28.0` do Poetry)
- `~=2.28.0` = >=2.28.0, <2.29.0 (só patch)
- `==2.28.1` = versão exata
- `requires-python = ">=3.12"` = Python 3.12 ou superior

Ao rodar `uv add requests`, o uv grava `requests>=2.32.3` (limite inferior) e o `uv.lock` fixa a versão exata.

## 7. Workflow Completo (Django)

```powershell
# 1. Iniciar
uv init meu_site --python 3.12
cd meu_site

# 2. Adicionar dependências
uv add django
uv add --dev pytest pytest-django ruff

# 3. Criar o projeto Django na pasta atual (note o ponto final)
uv run django-admin startproject config .

# 4. Migrar e rodar
uv run python manage.py migrate
uv run python manage.py runserver

# 5. Commit
git add pyproject.toml uv.lock .python-version
```

Abra `http://127.0.0.1:8000` no navegador para ver o Django funcionando.

> O `main.py` criado pelo `uv init` não é necessário em projetos Django e pode ser apagado.

### Depurar Django no VS Code

Crie `.vscode/launch.json`:

```json
{
  "version": "0.2.0",
  "configurations": [
    {
      "name": "Django",
      "type": "debugpy",
      "request": "launch",
      "program": "${workspaceFolder}/manage.py",
      "args": ["runserver"],
      "django": true,
      "justMyCode": true
    }
  ]
}
```

Com o interpretador `.venv` selecionado, aperte `F5`.

## 8. Estrutura de Projeto

```plaintext
meu_site/
├── .venv/               # Criado automaticamente (não vai para o Git)
├── .vscode/
│   └── launch.json
├── config/
│   ├── settings.py
│   └── urls.py
├── manage.py
├── pyproject.toml
├── uv.lock
├── .python-version
└── README.md
```

## 9. Migrando do Poetry ou requirements.txt

```powershell
# De requirements.txt
uv add -r requirements.txt

# Exportar para requirements.txt (Docker, deploy)
uv export --no-dev -o requirements.txt

# De Poetry: converta o pyproject.toml para o formato [project]
# e rode:
uv lock
uv sync
```

Para converter automaticamente o `pyproject.toml` do Poetry, existe a ferramenta `migrate-to-uv`:

```powershell
uvx migrate-to-uv
```

## 10. Equivalência Poetry → uv

| Poetry | uv |
|---|---|
| `poetry new meu_projeto` | `uv init meu_projeto` |
| `poetry add requests` | `uv add requests` |
| `poetry add --group dev pytest` | `uv add --dev pytest` |
| `poetry remove requests` | `uv remove requests` |
| `poetry install` | `uv sync` |
| `poetry run python app.py` | `uv run python app.py` |
| `poetry shell` | `.venv\Scripts\Activate.ps1` (ou apenas `uv run`) |
| `poetry lock` | `uv lock` |
| `poetry update` | `uv lock --upgrade` e `uv sync` |
| `poetry show --tree` | `uv tree` |
| `pipx install poetry` | Não precisa: uv já é standalone |

## 11. Vantagens vs Pip e Poetry

1. **Velocidade**: 10 a 100 vezes mais rápido que pip
2. **Ferramenta única**: pip, venv, pipx e pyenv em um só executável
3. **Gerencia o Python**: baixa a versão correta sozinho
4. **Lockfile multiplataforma**: o mesmo `uv.lock` funciona em Windows, Linux e macOS
5. **Padrão PEP 621**: sem formato proprietário de configuração
6. **Ambiente automático**: `uv run` cria e sincroniza o `.venv`
7. **Cache global**: pacotes reutilizados entre projetos, economizando disco

## 12. Dicas Importantes

- Sempre faça commit de `pyproject.toml`, `uv.lock` e `.python-version`
- Nunca edite `uv.lock` manualmente
- Não faça commit da pasta `.venv`
- Prefira `uv add` a `uv pip install`, para que o `pyproject.toml` seja atualizado
- Use `uv sync --no-dev` em produção e `uv sync --frozen` em CI (não altera o lock)
- Se o VS Code não achar o ambiente, use **Python: Select Interpreter** e aponte para `.venv\Scripts\python.exe`
- Se o terminal não reconhecer `uv`, feche e reabra o VS Code para atualizar o `PATH`
- Em projetos pequenos ou scripts soltos, use `uv run --with requests script.py` ou o bloco de metadados inline (PEP 723)
