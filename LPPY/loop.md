# Laços de Repetição (loop)

## Introdução

Laços de repetição, ou *loops*, são estruturas fundamentais em programação que permitem executar um bloco de código várias vezes, com base em uma condição ou uma sequência de elementos. Em Python, os principais laços são `for` e `while`. Eles são amplamente usados para processar coleções de dados, como listas, conjuntos e arrays (geralmente representados por listas em Python).

## 1. Laço `for`

O laço `for` é usado para iterar sobre uma sequência de elementos, como listas, conjuntos, tuplas, strings ou intervalos numéricos. Ele percorre cada item da sequência automaticamente, sem a necessidade de controlar manualmente a iteração.

```python
for variavel in sequencia:
    # Bloco de código a ser executado
```

### Como funciona

- A `variavel` assume, a cada iteração, o valor de um elemento da `sequencia`.
- O bloco de código dentro do laço é executado para cada elemento.
- Quando todos os elementos da sequência forem processados, o laço termina.

### Exemplo 1: Iterando sobre uma lista

```python
frutas = ["maçã", "banana", "laranja", "uva"]
for fruta in frutas:
    print(f"Fruta: {fruta}")
```

**Saída:**

```plaintext
Fruta: maçã
Fruta: banana
Fruta: laranja
Fruta: uva
```

### Exemplo 2: Iterando sobre um conjunto

Conjuntos (`set`) são coleções não ordenadas de elementos únicos. O laço `for` pode ser usado para percorrer seus elementos, mas a ordem não é garantida.

```python
numeros = {1, 2, 3, 4, 5}
for num in numeros:
    print(f"Número: {num}")
```

**Saída (ordem pode variar):**

```plaintext
Número: 1
Número: 2
Número: 3
Número: 4
Número: 5
```

### Exemplo 3: Usando `range()` para números

O `range()` é uma função que gera uma sequência de números, ideal para iterações baseadas em índices.

```python
for i in range(5):  # Gera números de 0 a 4
    print(f"Índice: {i}")
```

**Saída:**

```plaintext
Índice: 0
Índice: 1
Índice: 2
Índice: 3
Índice: 4
```

## 2. Laço `while`

O laço `while` executa um bloco de código enquanto uma condição específica for verdadeira. Ele é útil quando o número de iterações não é conhecido previamente.

### Sintaxe

```python
while condicao:
    # Bloco de código a ser executado
```

### Como funciona

- A `condicao` é avaliada antes de cada iteração.
- Se a condição for `True`, o bloco de código é executado.
- Se a condição for `False`, o laço termina.
- **Cuidado**: Um laço `while` mal configurado pode resultar em um *loop infinito*.

### Exemplo 1: Contagem com lista

```python
numeros = [10, 20, 30, 40, 50]
indice = 0
while indice < len(numeros):
    print(f"Elemento: {numeros[indice]}")
    indice += 1
```

**Saída:**

```
Elemento: 10
Elemento: 20
Elemento: 30
Elemento: 40
Elemento: 50
```

### Exemplo 2: Filtrando elementos de um conjunto

```python
numeros = {2, 4, 6, 8, 10}
soma = 0
while numeros:
    num = numeros.pop()  # Remove e retorna um elemento do conjunto
    if num % 2 == 0:
        soma += num
    print(f"Soma parcial: {soma}")
```

**Saída (ordem pode variar):**

```plaintext
Soma parcial: 2
Soma parcial: 6
Soma parcial: 12
Soma parcial: 20
Soma parcial: 30
```

---

## 3. Laços aninhados

Laços podem ser aninhados, ou seja, um laço dentro de outro. Isso é útil para trabalhar com estruturas de dados complexas, como listas de listas.

### Exemplo: Matriz (lista de listas)

```python
matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for linha in matriz:
    for elemento in linha:
        print(f"Elemento: {elemento}")
```

**Saída:**

```
Elemento: 1
Elemento: 2
Elemento: 3
Elemento: 4
Elemento: 5
Elemento: 6
Elemento: 7
Elemento: 8
Elemento: 9
```

---

## 4. Controle de laços

Python oferece instruções para controlar o fluxo dos laços:

- `break`: Interrompe o laço imediatamente.
- `continue`: Pula para a próxima iteração, ignorando o restante do bloco atual.
- `else`: Executado quando o laço termina normalmente (sem `break`).

### Exemplo com `break` e `continue`

```python
numeros = [1, 2, 3, 4, 5, 6]
for num in numeros:
    if num == 4:
        print("Encontramos o 4, parando o laço!")
        break
    if num % 2 == 0:
        continue
    print(f"Número ímpar: {num}")
```

**Saída:**

```plaintext
Número ímpar: 1
Número ímpar: 3
Encontramos o 4, parando o laço!
```

### Exemplo com `else`

```python
numeros = [1, 3, 5, 7]
for num in numeros:
    if num % 2 == 0:
        print("Encontramos um número par!")
        break
else:
    print("Nenhum número par encontrado.")
```

**Saída:**

```plaintext
Nenhum número par encontrado.
```
