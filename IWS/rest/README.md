# API de Gerenciamento de Pedidos

[![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.141.1-green?logo=fastapi)](https://fastapi.tiangolo.com/)
[![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-2.0.52-red?logo=python)](https://docs.sqlalchemy.org/)
[![Uvicorn](https://img.shields.io/badge/Uvicorn-0.52.4-purple?logo=python)](https://www.uvicorn.org/)
[![Pydantic](https://img.shields.io/badge/Pydantic-2.13.4-blue?logo=python)](https://docs.pydantic.dev/)

---

## Descrição

Este projeto é uma API REST para gerenciamento de pedidos e clientes, construída com FastAPI, SQLAlchemy e Pydantic. O banco de dados é configurável: **SQLite** (arquivo local, sem instalação) ou **MySQL**, escolhido por variável de ambiente, sem alterar código. O código é organizado em camadas (model, repository, service, controller, schema), cada uma com responsabilidade única.

---

## Sumário

1. [Arquitetura e camadas](#arquitetura-e-camadas)
2. [Padrões de projeto utilizados](#padrões-de-projeto-utilizados)
3. [Protocolo REST/HTTP utilizado](#protocolo-resthttp-utilizado)
4. [Estrutura de pastas e arquivos](#estrutura-de-pastas-e-arquivos)
5. [Instalação e configuração no Windows](#instalação-e-configuração-no-windows)
6. [Escolhendo o banco de dados: SQLite ou MySQL](#escolhendo-o-banco-de-dados-sqlite-ou-mysql)
7. [Executando a aplicação](#executando-a-aplicação)
8. [Autenticação](#autenticação)
9. [Rotas disponíveis](#rotas-disponíveis)

---

## Arquitetura e camadas

A aplicação segue uma arquitetura em camadas, onde cada uma só conhece a camada imediatamente abaixo dela. Uma requisição atravessa o sistema nesta ordem:

```
Cliente HTTP
     │
     ▼
Controller   → recebe a chamada da rota, delega ao service, converte erros de
               negócio (ValueError) em respostas HTTP (404, 400, 401...)
     │
     ▼
Service      → regras de negócio: o que é obrigatório, o que pode ou não ser
               atualizado, como um pedido se relaciona com seus itens
     │
     ▼
Repository   → acesso ao banco de dados (CRUD puro), sem nenhuma regra de
               negócio embutida
     │
     ▼
Model (ORM)  → tabelas do banco, mapeadas como classes Python via SQLAlchemy
```

**Por que separar assim?** Cada camada pode ser substituída isoladamente. Por exemplo, o repository pode trocar de MySQL para SQLite (como este projeto agora permite) sem que service, controller ou rota percebam qualquer diferença — todos dependem apenas da *interface* do repository, não da implementação concreta.

| Camada | Pasta | Conhece o banco? | Conhece regra de negócio? | Conhece HTTP? |
|---|---|:---:|:---:|:---:|
| Model | `models/` | sim (é a tabela) | não | não |
| Repository | `repositories/` | sim | não | não |
| Service | `services/` | não (fala com o repository) | sim | não |
| Controller | `controllers/` | não | não (delega ao service) | sim |
| Schema | `schemas/` | não | não | sim (formato de entrada/saída) |

---

## Padrões de projeto utilizados

- **Repository Pattern** ([repositories/igeneric_repository.py](repositories/igeneric_repository.py), [repositories/generic_repository.py](repositories/generic_repository.py)): isola o acesso a dados atrás de uma interface (`IGenericRepository`). O service depende da interface, não da implementação — por isso trocar o banco de dados não exige alterar nenhum service.
- **Generic Repository** (`Generic[T]`, `TypeVar`): uma única implementação de CRUD (`GenericRepository`) serve tanto para `Pedido` quanto para `Cliente`. `PedidoRepository` e `ClienteRepository` apenas informam qual modelo usar — evita duplicar create/read/update/delete para cada entidade.
- **Factory Pattern** ([controllers/factory.py](controllers/factory.py)): `ControllerFactory` centraliza a montagem da cadeia `repository → service → controller` para cada requisição, evitando repetir esse código em cada rota do `app.py`.
- **Dependency Injection**: o `Depends()` do FastAPI injeta a sessão de banco (`get_db`) e os controllers automaticamente, por requisição — cada requisição recebe sua própria sessão, fechada ao final mesmo se ocorrer erro.
- **DTO / separação schema-model**: os dados que entram (`*CreateSchema`, `*UpdateSchema`) e saem (`*OutSchema`) pela API nunca são o objeto ORM diretamente — são schemas Pydantic dedicados, o que evita expor detalhes internos da tabela (e permite validar o formato antes de qualquer regra de negócio rodar).
- **Strategy implícita na configuração de banco** ([config/database.py](config/database.py)): a função `_build_database_url()` decide, a partir da variável `DB_BACKEND`, qual string de conexão montar — SQLite ou MySQL —, sem que o restante da aplicação precise saber qual dos dois está em uso.

---

## Protocolo REST/HTTP utilizado

A API segue os princípios REST sobre HTTP/1.1, conforme descrito em [IWS/readme.md](../readme.md):

- **Recursos identificados por URL**: `/pedidos`, `/pedidos/{id}`, `/clientes`, `/clientes/{id}`.
- **Verbos HTTP com significado semântico**:
  | Verbo | Uso no projeto |
  |---|---|
  | `GET` | ler um recurso (não altera estado) |
  | `POST` | criar um novo recurso |
  | `PUT` | atualizar um recurso existente |
  | `DELETE` | remover um recurso |
- **Stateless**: cada requisição carrega tudo o que o servidor precisa (inclusive a chave de API no header) — nenhuma sessão é mantida em memória entre requisições.
- **Corpo em JSON**: tanto o corpo de entrada (`POST`/`PUT`) quanto o de saída são JSON, validados por schemas Pydantic.
- **Códigos de status HTTP com significado**:
  | Código | Situação |
  |---|---|
  | `200 OK` | leitura ou atualização bem-sucedida |
  | `201 Created` | recurso criado com sucesso |
  | `204 No Content` | remoção bem-sucedida (sem corpo de resposta) |
  | `400 Bad Request` | dado de negócio inválido (ex.: pedido sem itens) |
  | `401 Unauthorized` | header `X-API-Key` ausente ou incorreto |
  | `404 Not Found` | recurso inexistente |
  | `422 Unprocessable Entity` | corpo da requisição não corresponde ao schema esperado (gerado automaticamente pelo FastAPI/Pydantic) |
- **Documentação auto-descritiva**: o FastAPI gera a especificação OpenAPI automaticamente a partir das rotas e schemas, exposta em `/docs` (Swagger UI) e `/redoc`.

---

## Estrutura de pastas e arquivos

```
IWS/
└── rest/
    ├── app.py                        # Ponto de entrada: rotas FastAPI e injeção de dependências
    ├── config/
    │   ├── database.py                # Monta a conexão (SQLite ou MySQL) conforme DB_BACKEND
    │   └── security.py                # Verificação da chave de API
    ├── models/
    │   ├── base.py                    # Base declarativa do SQLAlchemy
    │   ├── cliente.py                 # Tabela `cliente`
    │   ├── pedido.py                  # Tabela `pedido`
    │   └── item_pedido.py             # Tabela `item_pedido`
    ├── repositories/
    │   ├── igeneric_repository.py     # Contrato genérico de acesso a dados
    │   ├── generic_repository.py      # Implementação genérica do CRUD
    │   ├── icliente_repository.py / cliente_repository.py
    │   └── ipedido_repository.py / pedido_repository.py
    ├── services/
    │   ├── cliente_service.py         # Regras de negócio de cliente
    │   └── pedido_service.py          # Regras de negócio de pedido
    ├── controllers/
    │   ├── cliente_controller.py      # Ponte entre rota e service, traduz erros em HTTP
    │   ├── pedido_controller.py
    │   └── factory.py                 # Monta a cadeia repository → service → controller
    ├── schemas/
    │   └── schema.py                  # Schemas Pydantic de entrada e saída
    ├── requirements.txt                # Dependências de execução
    └── .env.example                    # Modelo de variáveis de ambiente
```

---

## Instalação e configuração no Windows

Todos os comandos abaixo são para **PowerShell**. O caminho do projeto é `IWS\rest` dentro do repositório clonado.

### 1. Instalar o Python

Este projeto é validado com **Python 3.12**. Se ainda não tiver essa versão instalada:

```powershell
winget install --id Python.Python.3.12 --source winget
```

### 2. Criar e ativar um ambiente virtual

Um ambiente virtual isola as dependências deste projeto do restante do sistema.

```powershell
cd caminho\para\IWS\rest
py -3.12 -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Se o PowerShell bloquear a ativação por política de execução de scripts, rode uma vez (como usuário atual, não exige administrador):

```powershell
Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
```

Com o ambiente ativado, o prompt passa a exibir `(.venv)` no início da linha.

### 3. Instalar as dependências

```powershell
pip install -r requirements.txt
```

Isso instala FastAPI, Uvicorn, SQLAlchemy, Pydantic, `python-dotenv` e o driver do MySQL. **O driver do MySQL só é necessário se você for usar `DB_BACKEND=mysql`** — para rodar apenas com SQLite (o padrão), esse pacote fica instalado mas inerte, não é preciso removê-lo.

### 4. Criar o arquivo de configuração

```powershell
Copy-Item .env.example .env
```

Abra o `.env` gerado em um editor de texto e ajuste os valores conforme a seção seguinte.

---

## Escolhendo o banco de dados: SQLite ou MySQL

A variável `DB_BACKEND` no `.env` decide qual banco a aplicação usa. Nenhuma outra alteração de código é necessária para trocar de um para o outro.

### Opção A — SQLite (recomendada para começar)

Não exige instalar nem configurar nenhum servidor de banco de dados — é um único arquivo local.

```ini
DB_BACKEND=sqlite
SQLITE_PATH=./db_pedidos.db
```

Ao rodar a aplicação, o arquivo `db_pedidos.db` (e as tabelas dentro dele) são criados automaticamente na primeira execução, no diretório onde o comando for executado.

### Opção B — MySQL

Use quando quiser um comportamento mais próximo de um ambiente de produção real, ou já tiver um MySQL disponível.

1. Instale o MySQL, se necessário:
   ```powershell
   winget install --id Oracle.MySQL --source winget
   ```
2. Crie o banco de dados (via MySQL Workbench, `mysql` CLI, ou outra ferramenta de sua preferência):
   ```sql
   CREATE DATABASE db_pedidos;
   ```
3. No `.env`:
   ```ini
   DB_BACKEND=mysql
   DB_USER=root
   DB_PASSWORD=sua_senha
   DB_HOST=localhost
   DB_NAME=db_pedidos
   ```

As tabelas (`cliente`, `pedido`, `item_pedido`) também são criadas automaticamente na primeira execução, caso ainda não existam.

> O `.env` nunca deve ser versionado no Git — ele já está listado no `.gitignore`.

---

## Executando a aplicação

Com o ambiente virtual ativado e o `.env` configurado:

```powershell
python app.py
```

Saída esperada: o Uvicorn informa que o servidor está no ar em `http://localhost:8000`.

Acesse a documentação interativa, gerada automaticamente a partir das rotas e schemas:

- **Swagger UI:** [http://localhost:8000/docs](http://localhost:8000/docs)
- **Redoc:** [http://localhost:8000/redoc](http://localhost:8000/redoc)

Para parar o servidor, pressione `Ctrl+C` no terminal.

### Testando pela linha de comando

```powershell
# Sem autenticação
Invoke-RestMethod -Uri http://localhost:8000/health

# Com autenticação (X-API-Key deve bater com o valor de API_KEY no .env)
$headers = @{ "X-API-Key" = "changeme" }
Invoke-RestMethod -Uri http://localhost:8000/clientes -Headers $headers

Invoke-RestMethod -Uri http://localhost:8000/clientes -Method Post -Headers $headers `
    -ContentType "application/json" -Body '{"nome":"Ana","idade":30}'
```

---

## Autenticação

Todas as rotas de `/pedidos` e `/clientes` exigem o header `X-API-Key`, com o valor configurado em `API_KEY` no `.env`. Requisições sem a chave, ou com uma chave incorreta, recebem `401 Unauthorized`. O endpoint `GET /health` é público, para uso por ferramentas de monitoramento.

---

## Rotas disponíveis

| Método | Rota                  | Autenticação | Descrição                                    |
|--------|------------------------|:---:|-----------------------------------------------|
| GET    | `/health`              | não | Verifica se a aplicação está no ar             |
| GET    | `/pedidos`             | sim | Lista pedidos (aceita `skip` e `limit`)        |
| GET    | `/pedidos/{id}`        | sim | Detalha um pedido                              |
| POST   | `/pedidos`             | sim | Cria um novo pedido com seus itens             |
| PUT    | `/pedidos/{id}`        | sim | Atualiza cliente, data e/ou itens de um pedido |
| DELETE | `/pedidos/{id}`        | sim | Remove um pedido                               |
| GET    | `/clientes`            | sim | Lista clientes (aceita `skip` e `limit`)       |
| GET    | `/clientes/{id}`       | sim | Detalha um cliente                             |
| POST   | `/clientes`            | sim | Cria um novo cliente                           |
| PUT    | `/clientes/{id}`       | sim | Atualiza nome e/ou idade de um cliente         |
| DELETE | `/clientes/{id}`       | sim | Remove um cliente                              |

A paginação (`skip`/`limit`) evita carregar a tabela inteira em uma única resposta; os valores padrão são `skip=0` e `limit=100`.

