# Programação Assíncrona em Python

## O problema que a programação assíncrona resolve

A maioria dos programas passa grande parte do tempo **esperando**: esperando uma resposta de uma API, esperando um arquivo ser lido do disco, esperando o banco de dados retornar uma consulta.

Durante essa espera, o programa fica parado — mesmo que o processador esteja completamente livre.

```python
import time
import requests  # pip install requests

def buscar_dados(url):
    resposta = requests.get(url)   # ← programa trava aqui até a resposta chegar
    return resposta.json()

inicio = time.time()

# Três requisições feitas uma após a outra:
buscar_dados("https://httpbin.org/delay/1")  # espera 1 segundo
buscar_dados("https://httpbin.org/delay/1")  # espera mais 1 segundo
buscar_dados("https://httpbin.org/delay/1")  # espera mais 1 segundo

print(f"Tempo total: {time.time() - inicio:.1f}s")  # ~3.0s
```

Esse é o modelo **síncrono** (ou bloqueante): cada operação precisa terminar para a próxima começar. Com três requisições de 1 segundo cada, o tempo total é 3 segundos.

A programação assíncrona resolve isso: em vez de esperar, o programa **suspende a tarefa atual** e vai executar outra. Quando a espera termina, retoma de onde parou.

> **Analogia:** Um garçom síncrono anota o pedido da mesa 1, vai até a cozinha, fica parado esperando o prato ficar pronto, volta, entrega, só então vai à mesa 2. Um garçom assíncrono anota o pedido da mesa 1, deixa a cozinha preparando e já vai anotar o pedido da mesa 2. Quando o prato da mesa 1 fica pronto, ele entrega. O trabalho real (cozinhar) leva o mesmo tempo — mas o garçom não fica ocioso.

---

## Conceitos Fundamentais

### Síncrono vs. Assíncrono

| Modelo | O que faz enquanto espera? | Quando usar |
|---|---|---|
| **Síncrono** | Para e aguarda | Operações rápidas, sem I/O |
| **Assíncrono** | Suspende e executa outra tarefa | I/O intenso: rede, disco, banco |
| **Threads** | Executa em paralelo (outro fio) | CPU intenso ou código legado |

> **Importante:** programação assíncrona em Python **não executa código em paralelo**. Ela permite que o programa **alterne** entre tarefas durante os momentos de espera. Para paralelismo real de CPU, usam-se threads ou processos.

---

### O Loop de Eventos (*Event Loop*)

O coração da programação assíncrona em Python é o **loop de eventos** (`asyncio`). Ele é um gerenciador que:

1. Mantém uma fila de tarefas a executar.
2. Executa uma tarefa até ela precisar esperar por algo.
3. Suspende essa tarefa, coloca outra para rodar.
4. Quando a espera termina, retoma a tarefa suspensa.

```text
Loop de eventos:
┌──────────────────────────────────────────┐
│                                          │
│  Tarefa A → executa → suspende (I/O)    │
│                 ↓                        │
│  Tarefa B → executa → suspende (I/O)    │
│                 ↓                        │
│  Tarefa A → I/O pronto → retoma → fim   │
│                 ↓                        │
│  Tarefa B → I/O pronto → retoma → fim   │
│                                          │
└──────────────────────────────────────────┘
```

O módulo `asyncio` é a implementação padrão do loop de eventos em Python.

---

### Corrotinas

Uma **corrotina** é uma função que pode ser suspensa no meio da execução e retomada depois. Em Python, é definida com `async def`.

```python
import asyncio

async def dizer_oi(nome):
    print(f"Oi, {nome}!")
    await asyncio.sleep(1)   # suspende aqui por 1 segundo
    print(f"Tchau, {nome}!")

# Uma corrotina não executa ao ser chamada — ela retorna um objeto corrotina:
resultado = dizer_oi("Ana")
print(type(resultado))  # <class 'coroutine'>

# Para executar, é preciso passar ao loop de eventos:
asyncio.run(dizer_oi("Ana"))
# Substitua asyncio.run() por await diretamente em um ambiente de notebook:
# await dizer_oi("Ana")
```

**Saída:**
```
Olá, Ana!
(1 segundo de espera)
Tchau, Ana!
```

> **Analogia com POO:** uma corrotina se parece com um método, mas em vez de executar do início ao fim sem parar, ela pode ser "pausada" em pontos específicos marcados com `await`.

---

### `async def` e `await`

- **`async def`** declara que a função é uma corrotina — ela pode ser suspensa.
- **`await`** marca o ponto de suspensão: "espere por isso, mas libere o loop enquanto aguarda".

`await` só pode ser usado **dentro de uma função `async def`**. E só funciona com objetos "aguardáveis" (*awaitables*): outras corrotinas, `Task`s e `Future`s.

```python
import asyncio

async def buscar_simulado(id):
    print(f"Buscando item {id}...")
    await asyncio.sleep(1)           # simula I/O (rede, disco, etc.)
    print(f"Item {id} recebido.")
    return f"dados do item {id}"

async def principal():
    resultado = await buscar_simulado(42)
    print(resultado)

asyncio.run(principal())
```

**Saída:**
```
Buscando item 42...
(1 segundo)
Item 42 recebido.
dados do item 42
```

---

## Executando Tarefas Concorrentemente

O `await` sozinho executa uma corrotina por vez — não há ganho de tempo. Para ganhar velocidade, as tarefas precisam rodar **de forma concorrente**.

### `asyncio.gather` — Executar várias ao mesmo tempo

`asyncio.gather(*corrotinas)` agenda todas as corrotinas e aguarda que **todas** terminem, rodando-as de forma concorrente.

```python
import asyncio
import time

async def buscar(id, demora):
    print(f"Iniciando busca {id}")
    await asyncio.sleep(demora)
    print(f"Busca {id} concluída")
    return f"resultado {id}"

async def principal():
    inicio = time.time()

    # Sequencial (sem ganho):
    r1 = await buscar(1, 1)
    r2 = await buscar(2, 1)
    r3 = await buscar(3, 1)
    # Tempo: ~3 segundos
    resultados = [r1, r2, r3] # Define resultados for the sequential case

    #desmarque aqui em baixo e comente a parte sequancial sem ganho
    # Concorrente (com ganho):
    #resultados = await asyncio.gather(
    #    buscar(1, 1),
    #    buscar(2, 1),
    #    buscar(3, 1),
    #)

    print(f"Resultados: {resultados}")
    print(f"Tempo total: {time.time() - inicio:.1f}s")
# em notebook desmarque esta linha abaixo
# await principal()
asyncio.run(principal())
```

**Saída:**
```
Iniciando busca 1
Iniciando busca 2
Iniciando busca 3
Busca 1 concluída
Busca 2 concluída
Busca 3 concluída
Resultados: ['resultado 1', 'resultado 2', 'resultado 3']
Tempo total: 1.0s
```

Três operações de 1 segundo rodando concorrentemente completam em ~1 segundo — não 3.

---

### `asyncio.create_task` — Agendar sem esperar imediatamente

`create_task` agenda a corrotina para rodar no loop de eventos, mas não espera por ela na hora. Isso permite iniciar uma tarefa e continuar fazendo outras coisas antes de coletar o resultado.

```python
import asyncio

async def preparar(nome, tempo):
    print(f"Preparando {nome}...")
    await asyncio.sleep(tempo)
    print(f"{nome} pronto!")
    return nome

async def principal():
    # Agenda as tarefas — elas já começam a correr
    tarefa1 = asyncio.create_task(preparar("Relatório", 4))
    tarefa2 = asyncio.create_task(preparar("E-mail", 1))
    tarefa3 = asyncio.create_task(preparar("Outro Relatório",8))


    print("Tarefas iniciadas. Fazendo outra coisa...")
    await asyncio.sleep(0)  # cede o controle para o loop de eventos

    # Agora coleta os resultados (aguarda o que ainda não terminou)
    r1 = await tarefa1
    r2 = await tarefa2
    r3 = await tarefa3
    print(f"Concluído: {r1}, {r2}, {r3}")
# em notebook desmarque esta linha abaixo
#await principal()
asyncio.run(principal())
```

**Saída:**
```
Tarefas iniciadas. Fazendo outra coisa...
Preparando Relatório...
Preparando E-mail...
Preparando Outro Relatório...
E-mail pronto!
Relatório pronto!
Outro Relatório pronto!
Concluído: Relatório, E-mail, Outro Relatório
```

---

### `gather` vs. `create_task`

| | `gather` | `create_task` |
|---|---|---|
| Quando agendar | Na chamada de `gather` | Imediatamente ao criar |
| Quando aguardar | Aguarda todas ao mesmo tempo | Aguarda individualmente com `await` |
| Resultado | Lista com todos os retornos | Resultado da tarefa específica |
| Uso típico | Processar um lote de tarefas | Tarefas independentes com lógica entre elas |

---

## Tratamento de Erros

Erros em corrotinas se propagam normalmente com `try/except`.

```python
import asyncio

async def operacao_arriscada(valor):
    await asyncio.sleep(0.5)
    if valor < 0:
        raise ValueError(f"Valor inválido: {valor}")
    return valor * 2

async def principal():
    try:
        resultado = await operacao_arriscada(-1)
    except ValueError as e:
        print(f"Erro capturado: {e}")

    # Com gather, erros em qualquer tarefa cancelam as demais por padrão.
    # Use return_exceptions=True para capturar sem cancelar:
    resultados = await asyncio.gather(
        operacao_arriscada(3),
        operacao_arriscada(-1),
        operacao_arriscada(5),
        return_exceptions=True,
    )

    for r in resultados:
        if isinstance(r, Exception):
            print(f"Falhou: {r}")
        else:
            print(f"Sucesso: {r}")

await principal()
#asyncio.run(principal())
```

**Saída:**
```
Erro capturado: Valor inválido: -1
Sucesso: 6
Falhou: Valor inválido: -1
Sucesso: 10
```

---

## `async with` — Gerenciadores de Contexto Assíncronos

Quando uma operação de entrada/saída precisa de setup e teardown (como abrir e fechar uma conexão), usa-se `async with`. Funciona exatamente como o `with` comum, mas permite suspensão durante a abertura e o fechamento.

```python
import asyncio

class ConexaoSimulada:
    async def __aenter__(self):
        print("Abrindo conexão...")
        await asyncio.sleep(0.1)   # simula handshake de rede
        print("Conexão aberta.")
        return self

    async def __aexit__(self, *args):
        print("Fechando conexão...")
        await asyncio.sleep(0.1)
        print("Conexão fechada.")

    async def buscar(self, query):
        await asyncio.sleep(0.2)   # simula consulta
        return f"resultado para '{query}'"

async def principal():
    async with ConexaoSimulada() as conn:
        dados = await conn.buscar("usuários ativos")
        print(dados)

await principal()
#asyncio.run(principal())
```

**Saída:**
```
Abrindo conexão...
Conexão aberta.
resultado para 'usuários ativos'
Fechando conexão...
Conexão fechada.
```

Na prática, bibliotecas como `aiohttp` (HTTP) e `asyncpg` (PostgreSQL) já implementam `__aenter__` e `__aexit__` — basta usar `async with`.

---

## `async for` — Iteradores Assíncronos

`async for` permite iterar sobre uma fonte de dados que entrega os elementos de forma assíncrona (como um stream de rede ou linhas de um arquivo grande).

```python
import asyncio

class StreamSimulado:
    def __init__(self, itens):
        self.itens = itens
        self.indice = 0

    def __aiter__(self):
        return self

    async def __anext__(self):
        if self.indice >= len(self.itens):
            raise StopAsyncIteration
        await asyncio.sleep(0.1)   # simula chegada gradual de dados
        item = self.itens[self.indice]
        self.indice += 1
        return item

async def principal():
    stream = StreamSimulado(["linha 1", "linha 2", "linha 3"])
    async for linha in stream:
        print(linha)

await principal()
#asyncio.run(principal())
```

**Saída:**
```
linha 1
linha 2
linha 3
```

---

## Exemplo Integrado: Buscador de Dados Concorrente

O exemplo abaixo simula um sistema que busca informações de três fontes diferentes (banco de dados, API externa, cache) de forma concorrente, combinando os resultados no final.

```python
import asyncio
import time

async def buscar_banco(usuario_id):
    print(f"[BD] Consultando usuário {usuario_id}...")
    await asyncio.sleep(1.5)   # simula consulta ao banco
    return {"id": usuario_id, "nome": "Ana Silva", "plano": "premium"}

async def buscar_api(usuario_id):
    print(f"[API] Buscando histórico do usuário {usuario_id}...")
    await asyncio.sleep(1.0)   # simula chamada à API externa
    return {"compras": 42, "ultimo_acesso": "2026-06-23"}

async def buscar_cache(usuario_id):
    print(f"[Cache] Verificando preferências do usuário {usuario_id}...")
    await asyncio.sleep(0.3)   # cache é mais rápido
    return {"tema": "escuro", "idioma": "pt-BR"}

async def montar_perfil(usuario_id):
    inicio = time.time()

    # Três fontes consultadas ao mesmo tempo
    dados_bd, dados_api, dados_cache = await asyncio.gather(
        buscar_banco(usuario_id),
        buscar_api(usuario_id),
        buscar_cache(usuario_id),
    )

    perfil = {**dados_bd, **dados_api, **dados_cache}

    print(f"\nPerfil montado em {time.time() - inicio:.1f}s:")
    for chave, valor in perfil.items():
        print(f"  {chave}: {valor}")

# await montar_perfil(101)

asyncio.run(montar_perfil(101))
```

**Saída:**
```
[BD] Consultando usuário 101...
[API] Buscando histórico do usuário 101...
[Cache] Verificando preferências do usuário 101...

Perfil montado em 1.5s:
  id: 101
  nome: Ana Silva
  plano: premium
  compras: 42
  ultimo_acesso: 2026-06-23
  tema: escuro
  idioma: pt-BR
```

Sem concorrência, o tempo seria 1.5 + 1.0 + 0.3 = **2.8 segundos**. Com `gather`, o tempo é determinado pela operação **mais lenta**: **1.5 segundos**.



## Quando Usar (e Quando Não Usar)

### Use programação assíncrona quando:

- O programa faz muitas requisições de rede (APIs, web scraping).
- O programa lê e escreve arquivos ou banco de dados com frequência.
- É necessário atender múltiplos clientes simultaneamente (servidor web, chat).

### Não use programação assíncrona quando:

- O gargalo é o **processador** (cálculos matemáticos pesados, compressão de dados). Para isso, use `multiprocessing`.
- O código já é rápido o suficiente. Async adiciona complexidade — não use sem necessidade.
- Todas as bibliotecas que você precisa são síncronas e não têm versão async.

```text
Tipo de gargalo         Solução recomendada
──────────────────────  ───────────────────────────────────
I/O (rede, disco, BD)   asyncio (programação assíncrona)
CPU (cálculo intenso)   multiprocessing (processos paralelos)
Código legado/simples   threading (threads)
```



## Erros Comuns

### 1. Esquecer o `await`

```python
async def exemplo():
    await asyncio.sleep(1)
    return 42

async def principal():
    resultado = exemplo()       # ERRADO: retorna objeto corrotina, não executa
    resultado = await exemplo() # CORRETO
```

### 2. Usar funções bloqueantes dentro de corrotinas

```python
import time

async def errado():
    time.sleep(2)              # ERRADO: bloqueia o loop inteiro por 2 segundos
    await asyncio.sleep(2)     # CORRETO: suspende sem bloquear o loop
```

### 3. Chamar `asyncio.run` dentro de uma corrotina

```python
async def principal():
    asyncio.run(outra())       # ERRADO: asyncio.run não pode ser aninhado

async def principal():
        await outra()              # CORRETO
```

---

## Exercícios

### Exercício 1 — Primeira corrotina

Crie uma corrotina `contar(nome, ate)` que imprime números de 1 até `ate`, aguardando 0.5 segundo entre cada número. Em seguida, use `asyncio.gather` para rodar `contar("A", 3)` e `contar("B", 3)` ao mesmo tempo e observe a intercalação das saídas.

**Saída esperada (aproximada):**
```
A: 1
B: 1
A: 2
B: 2
A: 3
B: 3
```

---

### Exercício 2 — Tempo com e sem concorrência

Crie uma função assíncrona `processar(id, segundos)` que simula uma operação demorada com `asyncio.sleep`.

1. Execute cinco chamadas **sequencialmente** (com `await` um por um) e meça o tempo.
2. Execute as mesmas cinco chamadas com `asyncio.gather` e meça o tempo.
3. Compare e explique a diferença.

```python
tarefas = [(1, 1.0), (2, 0.5), (3, 1.5), (4, 0.8), (5, 1.2)]
# Tempo sequencial esperado: ~5.0s
# Tempo concorrente esperado: ~1.5s (a mais longa)
```

---

### Exercício 3 — Tratamento de erros com `gather`

Crie uma corrotina `validar(valor)` que:
- Aguarda 0.3 segundos.
- Lança `ValueError` se `valor` for negativo.
- Retorna `valor * 10` caso contrário.

Use `asyncio.gather` com `return_exceptions=True` para validar a lista `[-1, 5, -3, 8, 2]` de forma concorrente e imprima separadamente os sucessos e as falhas.

**Saída esperada:**
```
Sucessos: [50, 80, 20]
Falhas: [ValueError(-1), ValueError(-3)]
```



