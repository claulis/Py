# Coleções em Python

> **Recomendação:** execute cada exemplo no seu ambiente Python conforme avança na leitura.
> 
## 1. O que são coleções?

Em Python, uma **coleção** é uma estrutura de dados capaz de armazenar múltiplos valores em uma única variável. Sem esse recurso, seria necessário declarar uma variável separada para cada valor — abordagem inviável em qualquer programa real.

Considere o seguinte problema: armazenar as notas de 40 alunos sem usar coleções.

```python
# Sem coleções — impraticável
nota_aluno1 = 7.5
nota_aluno2 = 8.0
nota_aluno3 = 6.5
# ... e assim por diante até nota_aluno40
```

Com uma lista, o mesmo problema é resolvido em uma única linha:

```python
# Com coleção
notas = [7.5, 8.0, 6.5, 9.0, ...]  # todos os valores em uma estrutura
```

Python oferece cinco tipos principais de coleções, cada uma com características distintas:

| Coleção | Sintaxe | Mutável | Ordenada | Duplicatas | Acesso |
|---|---|---|---|---|---|
| `list` | `[a, b, c]` | Sim | Sim | Sim | Por índice |
| `tuple` | `(a, b, c)` | Não | Sim | Sim | Por índice |
| `dict` | `{k: v}` | Sim | Sim (Python 3.7+) | Chaves únicas | Por chave |
| `set` | `{a, b, c}` | Sim | Não | Não | Sem índice |
| `frozenset` | `frozenset({...})` | Não | Não | Não | Sem índice |
| `array` | `array('f', [...])` | Sim | Sim | Sim | Por índice |


>Mutável significa que o objeto pode ser alterado após sua criação — seus elementos podem ser adicionados, removidos ou modificados sem que um novo objeto seja criado na memória.

>Imutável é o oposto: uma vez criado, o objeto não pode ser alterado. Qualquer operação que pareça modificá-lo na verdade cria um novo objeto.

>Ordenado significa que a coleção preserva a sequência em que os elementos foram inseridos — e que essa sequência pode ser acessada por posição (índice).

>Não ordenado significa que a coleção não garante nenhuma ordem de armazenamento interno. Você não pode dizer "quero o segundo elemento", porque o conceito de posição não existe.
---

## 2. Lista (`list`)

A lista é a coleção mais utilizada em Python. Trata-se de uma sequência **mutável** e **ordenada** que aceita elementos de qualquer tipo. Por ser mutável, seus elementos podem ser adicionados, removidos ou alterados após a criação.

### Criação e acesso

```python
# Criação com colchetes
turma = ["Ana", "Bruno", "Carla", "Diego"]

# Indexação começa em zero
print(turma[0])   # Ana   — primeiro elemento
print(turma[2])   # Carla — terceiro elemento
print(turma[-1])  # Diego — último elemento (índice negativo)

# Fatiamento (slicing): [início:fim] — fim não é incluído
print(turma[1:3])  # ['Bruno', 'Carla']
```

### Operações de modificação

```python
notas = [7.0, 8.5, 6.0]

notas.append(9.5)         # insere no final:      [7.0, 8.5, 6.0, 9.5]
notas.insert(0, 10.0)     # insere na posição 0:  [10.0, 7.0, 8.5, 6.0, 9.5]
notas.remove(6.0)         # remove pelo valor:    [10.0, 7.0, 8.5, 9.5]
notas.pop()               # remove e retorna o último:   9.5
notas.pop(0)              # remove e retorna o da pos 0: 10.0
notas[0] = 7.5            # altera o elemento na posição 0
```

### Iteração com `for` e `enumerate`

```python
notas = [8.5, 6.0, 9.5, 7.0]

# Iteração simples
for nota in notas:
    print(nota)

# Iteração com índice — útil quando a posição importa
for i, nota in enumerate(notas):
    situacao = "aprovado" if nota >= 7.0 else "reprovado"
    print(f"Aluno {i + 1}: {nota} — {situacao}")

# Saída:
# Aluno 1: 8.5 — aprovado
# Aluno 2: 6.0 — reprovado
# Aluno 3: 9.5 — aprovado
# Aluno 4: 7.0 — aprovado
```

### List comprehension

List comprehension é uma sintaxe compacta para construir listas a partir de sequências existentes. É amplamente utilizada em código Python profissional.

```python
# Forma convencional
quadrados = []
for n in range(1, 6):
    quadrados.append(n ** 2)

# Com list comprehension — equivalente e mais conciso
quadrados = [n ** 2 for n in range(1, 6)]
print(quadrados)  # [1, 4, 9, 16, 25]

# Com filtro: apenas números pares
pares = [n for n in range(1, 11) if n % 2 == 0]
print(pares)  # [2, 4, 6, 8, 10]
```

### Exemplo aplicado: controle de frequência

```python
turma = ["Ana", "Bruno", "Carla", "Diego", "Emília"]
presentes = ["Ana", "Carla", "Emília"]

ausentes = [aluno for aluno in turma if aluno not in presentes]
print(f"Ausentes: {ausentes}")
print(f"Frequência: {len(presentes)}/{len(turma)} alunos presentes")

# Saída:
# Ausentes: ['Bruno', 'Diego']
# Frequência: 3/5 alunos presentes
```

### Métodos de referência

```python
numeros = [3, 1, 4, 1, 5, 9, 2, 6]

len(numeros)          # 8     — quantidade de elementos
numeros.sort()        # ordena a lista no lugar (modifica o original)
sorted(numeros)       # retorna nova lista ordenada (não modifica o original)
numeros.reverse()     # inverte a ordem no lugar
numeros.count(1)      # 2     — ocorrências do valor 1
numeros.index(5)      # posição da primeira ocorrência do valor 5
numeros.copy()        # retorna uma cópia independente da lista
```

---

## 3. Tupla (`tuple`)

A tupla é uma sequência **imutável** e **ordenada**. Uma vez criada, seus elementos não podem ser alterados. Essa característica não é uma limitação — é uma garantia de integridade: ao usar uma tupla, o desenvolvedor declara que aquele conjunto de dados não deve ser modificado.

```python
# Criação com parênteses
coordenadas_brasilia = (-15.7801, -47.9292)  # latitude, longitude
cor_verde_ifb = (78, 176, 40)               # valores RGB

# Acesso por índice, como nas listas
print(coordenadas_brasilia[0])  # -15.7801

# Desempacotamento: atribuição de cada elemento a uma variável
latitude, longitude = coordenadas_brasilia
print(f"Latitude: {latitude} | Longitude: {longitude}")

# Tentativa de modificação resulta em erro — comportamento intencional
# coordenadas_brasilia[0] = 0.0  # TypeError: 'tuple' object does not support item assignment
```

### Casos de uso recomendados

- Dados que representam uma unidade conceitual fixa, como coordenadas `(lat, lon)` ou cores `(R, G, B)`
- Retorno de múltiplos valores em funções
- Chaves de dicionários (listas não podem ser chaves, tuplas podem)

```python
# Retornando múltiplos valores de uma função
def analisar_notas(notas):
    media = sum(notas) / len(notas)
    maior = max(notas)
    menor = min(notas)
    return media, maior, menor  # Python empacota automaticamente como tupla

media, maior, menor = analisar_notas([7.0, 8.5, 6.0, 9.5])
print(f"Média: {media:.2f} | Maior: {maior} | Menor: {menor}")
# Saída: Média: 7.75 | Maior: 9.5 | Menor: 6.0
```

---

## 4. Dicionário (`dict`)

O dicionário armazena pares **chave → valor**. As chaves devem ser únicas e de tipo imutável (strings, números, tuplas). Os valores podem ser de qualquer tipo, incluindo outras coleções.

É a estrutura mais adequada para representar entidades do mundo real: um aluno possui matrícula, nome, curso e notas; um produto possui código, descrição e preço.

```python
aluno = {
    "matricula": "2024001",
    "nome": "Ana Silva",
    "curso": "Informática para Internet",
    "notas": [8.5, 7.0, 9.0]
}

# Acesso por chave
print(aluno["nome"])        # Ana Silva
print(aluno["notas"][0])    # 8.5 — primeira nota da lista de notas

# .get() retorna None (ou valor padrão) se a chave não existir
# Evita o KeyError que ocorreria com aluno["email"]
print(aluno.get("email", "não informado"))  # não informado
```

### Modificação

```python
aluno = {"nome": "Bruno", "nota": 7.0}

aluno["email"] = "bruno@ifb.edu.br"     # adiciona nova chave
aluno["nota"] = 8.5                      # atualiza valor existente
del aluno["email"]                       # remove chave

aluno.update({"nota": 9.0, "turma": "2A"})  # atualiza múltiplos pares de uma vez
```

### Iteração

```python
produto = {"codigo": "NB-001", "nome": "Notebook", "preco": 3400.00, "estoque": 5}

for chave, valor in produto.items():
    print(f"  {chave}: {valor}")
```

### Dicionário de dicionários

Esta estrutura é amplamente usada para representar registros de banco de dados ou respostas de APIs.

```python
turma = {
    "2024001": {"nome": "Ana",   "nota": 8.5},
    "2024002": {"nome": "Bruno", "nota": 6.0},
    "2024003": {"nome": "Carla", "nota": 9.5},
}

for matricula, dados in turma.items():
    situacao = "aprovado" if dados["nota"] >= 7.0 else "reprovado"
    print(f"{matricula} | {dados['nome']:<10} | {dados['nota']} | {situacao}")

# Saída:
# 2024001 | Ana        | 8.5 | aprovado
# 2024002 | Bruno      | 6.0 | reprovado
# 2024003 | Carla      | 9.5 | aprovado
```

### Dict comprehension

```python
# Gerar um dicionário de quadrados para valores de 1 a 5
quadrados = {n: n ** 2 for n in range(1, 6)}
print(quadrados)  # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# Filtrar apenas alunos aprovados a partir de um dicionário existente
turma = {"Ana": 8.5, "Bruno": 6.0, "Carla": 9.5, "Diego": 5.0}
aprovados = {nome: nota for nome, nota in turma.items() if nota >= 7.0}
print(aprovados)  # {'Ana': 8.5, 'Carla': 9.5}
```

---

## 5. Conjunto (`set` e `frozenset`)

O conjunto é uma coleção **não ordenada** de elementos **únicos**. Não suporta indexação e elimina duplicatas automaticamente. Sua implementação é baseada em tabela hash, o que torna as operações de pertencimento (`in`) muito eficientes.

As operações de conjunto correspondem diretamente à teoria dos conjuntos da matemática.

```python
linguagens_ana   = {"Python", "JavaScript", "SQL"}
linguagens_bruno = {"Python", "Java", "SQL", "C++"}

# Interseção: elementos presentes em ambos
em_comum = linguagens_ana & linguagens_bruno
print(em_comum)   # {'Python', 'SQL'}

# União: todos os elementos sem repetição
todas = linguagens_ana | linguagens_bruno
print(todas)      # {'Python', 'JavaScript', 'SQL', 'Java', 'C++'}

# Diferença: o que está em Ana e não está em Bruno
exclusivo_ana = linguagens_ana - linguagens_bruno
print(exclusivo_ana)  # {'JavaScript'}

# Diferença simétrica: o que está em um ou outro, mas não em ambos
exclusivos = linguagens_ana ^ linguagens_bruno
print(exclusivos)  # {'JavaScript', 'Java', 'C++'}
```

### Remoção de duplicatas

Um uso comum de `set` é eliminar valores repetidos de uma lista.

```python
registros = ["2024001", "2024002", "2024001", "2024003", "2024002"]

unicos = list(set(registros))
print(f"Registros originais: {len(registros)}")
print(f"Registros únicos:    {len(unicos)}")

# Saída:
# Registros originais: 5
# Registros únicos:    3
```

### `frozenset`

Versão imutável do `set`. Por ser imutável, pode ser utilizada como chave de dicionário.

```python
dias_letivos = frozenset({"segunda", "terça", "quarta", "quinta", "sexta"})

# frozenset pode ser chave de dicionário — set comum não pode
calendario = {dias_letivos: "semana regular"}

# Tentativa de modificação resulta em erro
# dias_letivos.add("sábado")  # AttributeError: 'frozenset' object has no attribute 'add'
```

---

## 6. Array (`array.array`)

O `array` do módulo padrão aceita apenas elementos de **um único tipo numérico**, o que reduz o consumo de memória em relação às listas. É adequado para armazenar grandes volumes de dados numéricos homogêneos.

Na prática profissional, bibliotecas como `numpy` oferecem funcionalidades mais completas para esse tipo de trabalho. Ainda assim, compreender `array.array` é útil para entender os fundamentos de estruturas homogêneas.

```python
from array import array

# Código de tipo 'f' = float de 32 bits
# Outros códigos: 'i' (inteiro), 'd' (float de 64 bits)
temperaturas = array('f', [23.5, 24.0, 22.8, 25.1, 19.3])
temperaturas.append(26.0)

total = sum(temperaturas)
media = total / len(temperaturas)

print(f"Registros:  {len(temperaturas)}")
print(f"Média:      {media:.1f}°C")
print(f"Máxima:     {max(temperaturas):.1f}°C")
print(f"Mínima:     {min(temperaturas):.1f}°C")

# Saída:
# Registros:  6
# Média:      23.5°C
# Máxima:     26.0°C
# Mínima:     19.3°C
```

---

## 7. Critérios para escolha da coleção

A escolha inadequada de coleção compromete a legibilidade e a eficiência do código. O diagrama a seguir resume os critérios de decisão:

```
Precisa armazenar múltiplos valores em ordem, com possibilidade de modificação?
  └─ Sim → list

Os dados formam uma unidade conceitual fixa (ex: coordenadas, cores RGB)?
  └─ Sim → tuple

Precisa associar valores a identificadores (chave → valor)?
  └─ Sim → dict

Precisa garantir unicidade dos elementos ou realizar operações de conjunto?
  └─ Sim → set (mutável) ou frozenset (imutável)

Precisa armazenar grande volume de dados numéricos homogêneos com eficiência de memória?
  └─ Sim → array (ou numpy para operações matemáticas avançadas)
```

---

## 8. Erros frequentes e como evitá-los

### `IndexError`: índice fora do intervalo

```python
frutas = ["maçã", "banana", "uva"]

# INCORRETO — a lista tem índices 0, 1 e 2; o índice 5 não existe
print(frutas[5])  # IndexError: list index out of range

# CORRETO — verificar o tamanho antes de acessar
indice = 5
if indice < len(frutas):
    print(frutas[indice])
else:
    print(f"Índice {indice} fora do intervalo válido (0 a {len(frutas) - 1}).")
```

### Modificação de lista durante iteração

Remover elementos de uma lista enquanto ela está sendo percorrida com `for` produz comportamento incorreto: elementos são pulados silenciosamente.

```python
# INCORRETO — elementos pares podem ser ignorados
numeros = [1, 2, 3, 4, 5, 6]
for n in numeros:
    if n % 2 == 0:
        numeros.remove(n)  # modifica a lista durante a iteração
print(numeros)  # [1, 3, 5, 6] — o 6 não foi removido

# CORRETO — construir uma nova lista com os elementos desejados
numeros = [1, 2, 3, 4, 5, 6]
numeros = [n for n in numeros if n % 2 != 0]
print(numeros)  # [1, 3, 5]
```

### `KeyError`: acesso a chave inexistente

```python
aluno = {"nome": "Ana", "nota": 8.5}

# INCORRETO — lança KeyError se a chave não existir
email = aluno["email"]  # KeyError: 'email'

# CORRETO — usar .get() com valor padrão
email = aluno.get("email", "não informado")
print(email)  # não informado

# Alternativa: verificar antes com o operador 'in'
if "email" in aluno:
    print(aluno["email"])
```

---

## 9. Referência dos métodos principais

### Lista

| Método | Descrição |
|---|---|
| `append(x)` | Insere `x` ao final da lista |
| `insert(i, x)` | Insere `x` na posição `i` |
| `remove(x)` | Remove a primeira ocorrência de `x` |
| `pop(i)` | Remove e retorna o elemento na posição `i` (padrão: último) |
| `sort()` | Ordena a lista no lugar |
| `sorted(lista)` | Retorna uma nova lista ordenada, sem modificar a original |
| `index(x)` | Retorna o índice da primeira ocorrência de `x` |
| `count(x)` | Conta as ocorrências de `x` |
| `copy()` | Retorna uma cópia independente da lista |

### Dicionário

| Método | Descrição |
|---|---|
| `get(chave, padrão)` | Retorna o valor ou `padrão` se a chave não existir |
| `keys()` | Retorna uma visão de todas as chaves |
| `values()` | Retorna uma visão de todos os valores |
| `items()` | Retorna pares `(chave, valor)` |
| `update(d)` | Adiciona ou atualiza pares a partir do dicionário `d` |
| `pop(chave)` | Remove e retorna o valor associado à chave |

### Conjunto

| Operador / Método | Descrição |
|---|---|
| `add(x)` | Adiciona o elemento `x` |
| `remove(x)` | Remove `x`; lança `KeyError` se não existir |
| `discard(x)` | Remove `x` sem erro se não existir |
| `\|` / `union()` | União |
| `&` / `intersection()` | Interseção |
| `-` / `difference()` | Diferença |
| `^` / `symmetric_difference()` | Diferença simétrica |



## 10. Exemplos completos

[Aqui](../LPPY/asset/code/playlist.py) tem um exemplo completo de cadastro CRUD usando apenas listas.

[Aqui](../LPPY/asset/code/vacinas.py) tem um exemplo completo de cadastro CRUD usando cojuntos, set e frozenset.
