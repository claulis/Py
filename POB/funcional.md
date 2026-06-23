# Programação Funcional em Python

## O que é Programação Funcional?

Quem já estudou POO aprendeu a organizar o código em torno de **objetos** que guardam estado e expõem comportamento. A **Programação Funcional (PF)** propõe uma visão diferente: o programa é construído como uma sequência de **transformações de dados** por meio de funções — sem modificar estado e sem efeitos colaterais.

Os dois paradigmas não são opostos. Python suporta ambos, e boas soluções frequentemente combinam os dois.

> **Analogia:** Em POO, você contrata um funcionário e diz "mantenha o saldo desta conta e siga estas regras". Em PF, você passa um dado por uma linha de montagem: cada estação recebe o dado, produz algo novo e devolve — sem alterar o que entrou.

---

## Conceitos Fundamentais

### 1. Funções Puras

Uma **função pura** tem duas propriedades:

1. Para os mesmos argumentos, sempre retorna o mesmo resultado.
2. Não produz **efeitos colaterais** — não altera variáveis externas, não escreve em disco, não imprime nada.

```python
# Função pura: o resultado depende apenas dos parâmetros
def somar(a, b):
    return a + b

print(somar(3, 4))  # sempre 7, sem importar quantas vezes chamar
```

```python
# Função impura: depende e modifica estado externo
total = 0

def acumular(valor):
    global total
    total += valor  # efeito colateral: altera variável externa
    return total

acumular(5)  # total vira 5
acumular(5)  # total vira 10 — resultado diferente com o mesmo argumento
```

**Por que funções puras importam?**

| Característica | Função pura | Função impura |
|---|---|---|
| Testabilidade | Alta — sem dependências externas | Baixa — precisa de estado configurado |
| Previsibilidade | Total | Depende do momento da chamada |
| Reutilização | Alta | Acoplada ao contexto onde vive |

---

### 2. Imutabilidade

Em PF, dados não são modificados — novas versões deles são criadas. Em Python, os tipos mais usados nesse estilo são **tuplas** (imutáveis) em vez de listas (mutáveis).

```python
# Estilo imperativo (mutável): modifica a lista original
numeros = [1, 2, 3, 4, 5]
numeros.append(6)   # altera o objeto original
numeros[0] = 99     # altera o objeto original

# Estilo funcional (imutável): cria uma nova estrutura
numeros = (1, 2, 3, 4, 5)
novos_numeros = numeros + (6,)  # cria uma nova tupla, a original não muda

print(numeros)       # (1, 2, 3, 4, 5) — intacta
print(novos_numeros) # (1, 2, 3, 4, 5, 6)
```

> A imutabilidade evita uma classe inteira de bugs: aqueles onde um objeto é modificado por acidente em algum ponto distante do código.

---

### 3. Funções de Primeira Classe

Em Python, funções são **objetos como qualquer outro**. Isso significa que uma função pode ser:

- atribuída a uma variável
- passada como argumento para outra função
- retornada como resultado de outra função

```python
def saudar(nome):
    return f"Olá, {nome}!"

# Atribuindo a uma variável
cumprimento = saudar
print(cumprimento("Ana"))  # Olá, Ana!

# Passando como argumento
def executar(funcao, valor):
    return funcao(valor)

print(executar(saudar, "Bruno"))  # Olá, Bruno!
```

Quem já conhece POO pode pensar nisso como "objetos que são chamáveis". A diferença é que uma função não carrega estado — apenas transforma o que entra.

> Em POO, um objeto carrega atributos de instância que persistem e mudam entre as chamadas. O objeto  lembra o que aconteceu nas chamadas anteriores. Isso é estado. Não há nenhum "self." escondido dentro da função que vá mudando. Tudo o que ela usa vem dos parâmetros, e tudo o que produz vai no retorno. Entre uma chamada e a próxima, ela não guarda nada.

---

### 4. Funções de Ordem Superior

Uma **função de ordem superior** é aquela que recebe outra função como argumento **ou** retorna uma função como resultado. Esse é o mecanismo central da programação funcional.

```python
def aplicar_duas_vezes(funcao, valor):
    return funcao(funcao(valor))

def dobrar(x):
    return x * 2

print(aplicar_duas_vezes(dobrar, 3))  # dobrar(dobrar(3)) → dobrar(6) → 12
```

---

## Ferramentas Funcionais do Python

Python disponibiliza três funções de ordem superior fundamentais: `map`, `filter` e `reduce`. Elas operam sobre sequências sem modificá-las, produzindo novos valores.

### `map` — Transformar

`map(funcao, sequencia)` aplica a função a **cada elemento** da sequência e retorna um iterador com os resultados.

```python
numeros = [1, 2, 3, 4, 5]

def ao_quadrado(x):
    return x ** 2

resultado = list(map(ao_quadrado, numeros))
print(resultado)  # [1, 4, 9, 16, 25]

# A lista original não foi alterada:
print(numeros)    # [1, 2, 3, 4, 5]
```

**Analogia com POO:** é como chamar o mesmo método em todos os objetos de uma lista, mas sem alterar nenhum deles — apenas coletar o valor retornado.

---

### `filter` — Selecionar

`filter(funcao, sequencia)` mantém apenas os elementos para os quais a função retorna `True`.

```python
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def e_par(x):
    return x % 2 == 0

pares = list(filter(e_par, numeros))
print(pares)  # [2, 4, 6, 8, 10]
```

---

### `reduce` — Acumular

`reduce(funcao, sequencia)` combina todos os elementos em um único valor, aplicando a função acumulativamente da esquerda para a direita. Está no módulo `functools`.

```python
from functools import reduce

numeros = [1, 2, 3, 4, 5]

def somar(acumulador, elemento):
    return acumulador + elemento

total = reduce(somar, numeros)
print(total)  # 15

# O processo interno é:
# somar(1, 2) → 3
# somar(3, 3) → 6
# somar(6, 4) → 10
# somar(10, 5) → 15
```

---

### Visualizando a diferença entre as três

```text
Entrada:  [1, 2, 3, 4, 5]

map    → transforma cada elemento → [1, 4, 9, 16, 25]
                                     ↑  ↑  ↑   ↑   ↑
                                    x²  x²  x²  x²  x²

filter → seleciona alguns elementos → [2, 4]
                                        ↑  ↑
                                      par par

reduce → combina todos em um → 15
              1+2+3+4+5
```

---

## Funções Lambda (Anônimas)

Uma **lambda** é uma função sem nome, definida em uma única expressão. É útil quando a função é simples e usada apenas uma vez — especialmente como argumento para `map`, `filter` ou `sort`.

**Sintaxe:**

```python
lambda parametros: expressao
```

```python
# Função nomeada:
def ao_quadrado(x):
    return x ** 2

# Lambda equivalente:
ao_quadrado = lambda x: x ** 2

print(ao_quadrado(4))  # 16
```

**Uso direto em `map` e `filter`:**

```python
numeros = [1, 2, 3, 4, 5]

quadrados = list(map(lambda x: x ** 2, numeros))
print(quadrados)  # [1, 4, 9, 16, 25]

impares = list(filter(lambda x: x % 2 != 0, numeros))
print(impares)  # [1, 3, 5]
```

**Ordenando com lambda:**

```python
produtos = [
    {"nome": "Teclado", "preco": 150},
    {"nome": "Mouse",   "preco": 80},
    {"nome": "Monitor", "preco": 900},
]

ordenados = sorted(produtos, key=lambda p: p["preco"])
for p in ordenados:
    print(p["nome"], p["preco"])
# Mouse 80
# Teclado 150
# Monitor 900
```

> **Limitação:** lambdas só aceitam **uma expressão**. Para lógica mais complexa, use uma função nomeada — o código fica mais legível.

---

## Compreensões de Lista

As **compreensões de lista** (*list comprehensions*) são a forma mais pythônica de expressar transformações e filtragens. Internamente, equivalem a um `map` + `filter`, mas com sintaxe mais concisa.

**Sintaxe:**

```python
[expressao for elemento in sequencia if condicao]
```

```python
numeros = [1, 2, 3, 4, 5, 6]

# Com map e filter:
pares_ao_quadrado = list(map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, numeros)))

# Com compreensão de lista (equivalente, mais legível):
pares_ao_quadrado = [x ** 2 for x in numeros if x % 2 == 0]

print(pares_ao_quadrado)  # [4, 16, 36]
```

**Compreensões de dicionário e conjunto:**

```python
nomes = ["ana", "bruno", "carla"]

# Dicionário: nome → comprimento
comprimentos = {nome: len(nome) for nome in nomes}
print(comprimentos)  # {'ana': 3, 'bruno': 5, 'carla': 5}

# Conjunto (sem duplicatas):
letras_unicas = {letra for nome in nomes for letra in nome}
print(letras_unicas)  # {'a', 'n', 'b', 'r', 'u', 'o', 'c', 'l'}
```

---

## Closures

Uma **closure** é uma função que "lembra" o ambiente em que foi criada, mesmo depois que esse ambiente deixou de existir.

```python
def criar_multiplicador(fator):
    def multiplicar(numero):
        return numero * fator  # "lembra" o valor de fator
    return multiplicar

dobrar  = criar_multiplicador(2)
triplicar = criar_multiplicador(3)

print(dobrar(5))    # 10
print(triplicar(5)) # 15
```

`criar_multiplicador` é chamada e termina, mas `multiplicar` continua a carregar o valor de `fator` consigo. Isso é uma closure.

**Por que isso importa?** Closures permitem criar funções especializadas a partir de funções genéricas, sem usar classes.

```python
# Versão OO equivalente:
class Multiplicador:
    def __init__(self, fator):
        self.fator = fator

    def __call__(self, numero):
        return numero * self.fator

dobrar = Multiplicador(2)
print(dobrar(5))  # 10
```

A closure é mais concisa quando não há necessidade de múltiplos métodos ou herança.

---

## Decoradores

Um **decorador** é uma função de ordem superior que envolve outra função para adicionar comportamento **sem modificá-la**. É uma das aplicações mais práticas do estilo funcional em Python.

```python
def registrar(funcao):
    def envoltorio(*args, **kwargs):
        print(f"Chamando: {funcao.__name__}")
        resultado = funcao(*args, **kwargs)
        print(f"Resultado: {resultado}")
        return resultado
    return envoltorio

@registrar
def somar(a, b):
    return a + b

somar(3, 4)
# Chamando: somar
# Resultado: 7
```

A sintaxe `@registrar` é equivalente a escrever `somar = registrar(somar)`. O decorador recebe a função original e retorna uma nova com comportamento estendido.

**Exemplo prático — medir tempo de execução:**

```python
import time

def medir_tempo(funcao):
    def envoltorio(*args, **kwargs):
        inicio = time.time()
        resultado = funcao(*args, **kwargs)
        fim = time.time()
        print(f"{funcao.__name__} levou {fim - inicio:.4f}s")
        return resultado
    return envoltorio

@medir_tempo
def processar(n):
    return sum(range(n))

processar(1_000_000)
# processar levou 0.0312s
```

---

## Compondo Funções

Na PF, problemas complexos são resolvidos **compondo funções simples** — a saída de uma vira entrada da próxima.

```python
def remover_espacos(texto):
    return texto.strip()

def para_maiusculas(texto):
    return texto.upper()

def adicionar_ponto(texto):
    return texto + "."

def compor(*funcoes):
    def pipeline(valor):
        for f in funcoes:
            valor = f(valor)
        return valor
    return pipeline

formatar = compor(remover_espacos, para_maiusculas, adicionar_ponto)

print(formatar("  olá mundo  "))  # OLÁ MUNDO.
```

Cada função faz uma única coisa. A composição faz o trabalho complexo.

---

## Exemplo Integrado: Processamento de Dados

O estilo funcional brilha em pipelines de transformação de dados. O exemplo abaixo processa uma lista de pedidos sem modificar nenhum dado original.

```python
from functools import reduce

pedidos = [
    {"produto": "Teclado", "preco": 150.0, "quantidade": 2, "ativo": True},
    {"produto": "Mouse",   "preco": 80.0,  "quantidade": 1, "ativo": False},
    {"produto": "Monitor", "preco": 900.0, "quantidade": 1, "ativo": True},
    {"produto": "Cabo",    "preco": 25.0,  "quantidade": 3, "ativo": True},
]

# 1. Filtrar apenas pedidos ativos
ativos = list(filter(lambda p: p["ativo"], pedidos))

# 2. Calcular o subtotal de cada pedido
com_subtotal = list(map(
    lambda p: {**p, "subtotal": p["preco"] * p["quantidade"]},
    ativos
))

# 3. Somar todos os subtotais
total = reduce(lambda acc, p: acc + p["subtotal"], com_subtotal, 0)

print(f"Total: R$ {total:.2f}")  # Total: R$ 1125.00

# Usando compreensão de lista (alternativa mais legível):
total_alt = sum(
    p["preco"] * p["quantidade"]
    for p in pedidos
    if p["ativo"]
)
print(f"Total (alt): R$ {total_alt:.2f}")  # Total (alt): R$ 1125.00
```

---

## Programação Funcional vs. POO

Os dois paradigmas têm focos diferentes e se complementam:

| Aspecto | POO | Programação Funcional |
|---|---|---|
| Unidade principal | Objetos com estado | Funções puras |
| Estado | Distribuído nos objetos | Evitado; dados são imutáveis |
| Reutilização | Herança e composição de objetos | Composição de funções |
| Efeitos colaterais | Aceitos (métodos alteram estado) | Minimizados |
| Ideal para | Modelar entidades do mundo real | Processar e transformar dados |

**Na prática:** Python não impõe um paradigma. É comum modelar entidades com classes (POO) e processar coleções de dados com `map`, `filter` e compreensões (PF).

```python
# Exemplo híbrido: classe (POO) + processamento funcional (PF)
class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

estoque = [
    Produto("Notebook", 3500),
    Produto("SSD", 400),
    Produto("RAM",  250),
]

# Processamento funcional sobre objetos POO
caros = [p.nome for p in estoque if p.preco > 300]
print(caros)  # ['Notebook', 'SSD']
```

---

## Exercícios

### Exercício 1 — Funções puras

Identifique quais das funções abaixo são puras. Para cada função impura, explique o motivo e reescreva-a como pura.

```python
historico = []

def registrar_nota(nota):
    historico.append(nota)      # (a)

def calcular_media(notas):
    return sum(notas) / len(notas)  # (b)

import random
def nota_aleatoria():
    return random.randint(0, 10)    # (c)
```

---

### Exercício 2 — `map` e `filter`

Dada a lista de temperaturas em Celsius, use `map` e `filter` (sem compreensão de lista) para:

1. Converter todas as temperaturas para Fahrenheit. Fórmula: `(c * 9/5) + 32`
2. Manter apenas as temperaturas originais (em Celsius) **acima de 30°C**

```python
temperaturas_c = [15, 22, 31, 8, 35, 28, 42, 19]
```

**Saída esperada:**
```
Fahrenheit: [59.0, 71.6, 87.8, 46.4, 95.0, 82.4, 107.6, 66.2]
Quentes:    [31, 35, 42]
```

---

### Exercício 3 — Closure

Crie uma função `criar_validador(minimo, maximo)` que retorna uma função. A função retornada deve receber um número e retornar `True` se ele estiver no intervalo `[minimo, maximo]` ou `False` caso contrário.

```python
# Exemplo de uso:
validar_nota   = criar_validador(0, 10)
validar_idade  = criar_validador(0, 150)

print(validar_nota(7.5))   # True
print(validar_nota(11))    # False
print(validar_idade(25))   # True
```

---

### Exercício 4 — Pipeline funcional

Dada a lista de frases abaixo, construa um pipeline usando `map` e `filter` (ou compreensão de lista) que:

1. Remove espaços do início e do fim de cada frase
2. Converte para minúsculas
3. Mantém apenas as frases com mais de 10 caracteres (após limpeza)

```python
frases = [
    "  Python é incrível  ",
    " OK ",
    "   Programação Funcional   ",
    "Oi",
    "  Funções de ordem superior  ",
]
```

**Saída esperada:**
```
['python é incrível', 'programação funcional', 'funções de ordem superior']
```

