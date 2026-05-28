# Funções em Python

> **Recomendação:** execute cada exemplo no seu ambiente Python conforme avança na leitura. 

## 1. O que é uma função?

Uma **função** é um bloco de código com nome próprio que executa uma tarefa específica e pode ser chamado quantas vezes for necessário. Em vez de repetir o mesmo código em vários lugares do programa, você o define uma vez dentro de uma função e o reutiliza.

Considere o seguinte problema: calcular a média e o status de aprovação de três alunos.

```python
# Sem funções — lógica repetida três vezes
notas_aluno1 = [7.5, 8.0, 6.5]
media1 = sum(notas_aluno1) / len(notas_aluno1)
status1 = "Aprovado" if media1 >= 7.0 else "Reprovado"
print(f"Aluno 1 — Média: {media1:.2f} | {status1}")

notas_aluno2 = [9.0, 8.5, 9.5]
media2 = sum(notas_aluno2) / len(notas_aluno2)
status2 = "Aprovado" if media2 >= 7.0 else "Reprovado"
print(f"Aluno 2 — Média: {media2:.2f} | {status2}")

notas_aluno3 = [6.0, 5.5, 7.0]
media3 = sum(notas_aluno3) / len(notas_aluno3)
status3 = "Aprovado" if media3 >= 7.0 else "Reprovado"
print(f"Aluno 3 — Média: {media3:.2f} | {status3}")
```

O código acima funciona, mas tem um problema sério: a mesma lógica está copiada três vezes. Se a nota mínima mudar de 7.0 para 6.0, será necessário alterar em três lugares — e esquecer um é questão de tempo.

Com funções, a lógica fica definida em um único ponto:

```python
def calcular_media(notas):
    return sum(notas) / len(notas) if notas else 0

def verificar_aprovacao(media):
    return "Aprovado" if media >= 7 else "Reprovado"

alunos = [
    {"nome": "Aluno 1", "notas": [7.5, 8.0, 6.5]},
    {"nome": "Aluno 2", "notas": [9.0, 8.5, 9.5]},
    {"nome": "Aluno 3", "notas": [6.0, 5.5, 7.0]},
]

for aluno in alunos:
    media = calcular_media(aluno["notas"])
    status = verificar_aprovacao(media)
    print(f"{aluno['nome']} — Média: {media:.2f} | {status}")

# Saída:
# Aluno 1 — Média: 7.33 | Aprovado
# Aluno 2 — Média: 9.00 | Aprovado
# Aluno 3 — Média: 6.17 | Reprovado
```

Agora, se a nota mínima mudar, basta alterar o valor padrão em `verificar_aprovacao`. Um único ponto de mudança, zero risco de inconsistência.

## 2. Estrutura de uma função

```python
def nome_da_funcao(parametro1, parametro2):
    """Docstring: descrição breve do que a função faz."""
    # corpo da função
    return resultado
```

| Elemento | Descrição |
|---|---|
| `def` | Palavra-chave que declara a função |
| `nome_da_funcao` | Identificador da função (convenção PEP 8: minúsculas com `_`) |
| `parametro1, parametro2` | Dados que a função recebe (opcionais) |
| Docstring | Documentação interna da função (opcional, mas recomendada) |
| `return` | Valor que a função devolve ao chamador (opcional) |


## 3. Tipos de funções

### 3.1 Sem parâmetros e sem retorno

A função mais simples: executa uma ação fixa e não devolve nada.

```python
def exibir_cabecalho():
    print("=" * 40)
    print("   Sistema de Gestão Escolar — IFB")
    print("=" * 40)

exibir_cabecalho()

# Saída:
# ========================================
#    Sistema de Gestão Escolar — IFB
# ========================================
```

### 3.2 Com parâmetros

Parâmetros permitem que a função receba dados e adapte seu comportamento. Cada chamada pode passar valores diferentes.

```python
def exibir_situacao(nome, nota):
    situacao = "aprovado" if nota >= 7.0 else "reprovado"
    print(f"{nome}: nota {nota:.1f} — {situacao}")

exibir_situacao("Ana", 8.5)    # Ana: nota 8.5 — aprovado
exibir_situacao("Bruno", 5.0)  # Bruno: nota 5.0 — reprovado
exibir_situacao("Carla", 7.0)  # Carla: nota 7.0 — aprovado
```
### 3.3 Com retorno (`return`)

A instrução `return` encerra a execução da função e devolve um valor ao chamador. Esse valor pode ser armazenado em uma variável ou usado diretamente em uma expressão.

```python
def calcular_imc(peso, altura):
    """Calcula o Índice de Massa Corporal.

    Args:
        peso (float): Peso em quilogramas.
        altura (float): Altura em metros.

    Returns:
        float: Valor do IMC.
    """
    return peso / (altura ** 2)

imc = calcular_imc(70, 1.75)
print(f"IMC: {imc:.2f}")  # IMC: 22.86

# O retorno pode ser usado diretamente em expressões
if calcular_imc(90, 1.70) > 25:
    print("IMC acima do recomendado.")
```

Uma função pode ter múltiplos `return`, mas apenas um é executado por chamada. É comum usar `return` antecipado para tratar casos especiais antes da lógica principal.

```python
def calcular_media(notas):
    if not notas:           # retorno antecipado: lista vazia
        return 0.0
    return sum(notas) / len(notas)
```

### 3.4 Com parâmetros padrão

Um parâmetro padrão define um valor que é usado quando o argumento não é fornecido na chamada. Parâmetros com valor padrão devem sempre vir **depois** dos parâmetros obrigatórios.

```python
def gerar_relatorio(nome, nota, nota_minima=7.0, turma="não informada"):
    situacao = "Aprovado" if nota >= nota_minima else "Reprovado"
    print(f"Turma: {turma} | Aluno: {nome} | Nota: {nota} | {situacao}")

# Usando os valores padrão
gerar_relatorio("Ana", 8.5)

# Sobrescrevendo os valores padrão
gerar_relatorio("Bruno", 6.0, nota_minima=6.0, turma="2A")
gerar_relatorio("Carla", 5.5, turma="2B")

# Saída:
# Turma: não informada | Aluno: Ana   | Nota: 8.5 | Aprovado
# Turma: 2A            | Aluno: Bruno | Nota: 6.0 | Aprovado
# Turma: 2B            | Aluno: Carla | Nota: 5.5 | Reprovado
```

### 3.5 Com número variável de argumentos (`*args` e `**kwargs`)

Quando o número de argumentos não é conhecido previamente, Python oferece dois mecanismos:

- `*args` — captura argumentos posicionais em uma **tupla**
- `**kwargs` — captura argumentos nomeados em um **dicionário**

```python
# *args: número variável de valores posicionais
def calcular_total(*valores):
    """Soma todos os valores recebidos, independentemente da quantidade."""
    return sum(valores)

print(calcular_total(10, 20))           # 30
print(calcular_total(5, 15, 25, 35))   # 80

# **kwargs: número variável de argumentos nomeados
def registrar_aluno(**dados):
    """Exibe os dados de um aluno recebidos como argumentos nomeados."""
    print("--- Registro de Aluno ---")
    for campo, valor in dados.items():
        print(f"  {campo}: {valor}")

registrar_aluno(nome="Ana Silva", matricula="2024001", curso="Informática para Internet")

# Saída:
# --- Registro de Aluno ---
#   nome: Ana Silva
#   matricula: 2024001
#   curso: Informática para Internet
```

### 3.6 Funções anônimas (`lambda`)

Uma função `lambda` é uma função sem nome definida em uma única linha. É adequada para operações simples, especialmente quando usada como argumento de outras funções como `sorted`, `map` e `filter`.

```python
# Sintaxe: lambda parâmetros: expressão

# Comparação entre função convencional e lambda
def dobrar(x):
    return x * 2

dobrar_lambda = lambda x: x * 2

print(dobrar(5))        # 10
print(dobrar_lambda(5)) # 10

# Uso prático: ordenar lista de dicionários por um campo específico
alunos = [
    {"nome": "Carla", "nota": 9.5},
    {"nome": "Ana",   "nota": 8.5},
    {"nome": "Bruno", "nota": 6.0},
]

# Ordena pelo valor da chave "nota"
alunos_ordenados = sorted(alunos, key=lambda a: a["nota"], reverse=True)

for aluno in alunos_ordenados:
    print(f"{aluno['nome']}: {aluno['nota']}")

# Saída (ordem decrescente de nota):
# Carla: 9.5
# Ana: 8.5
# Bruno: 6.0
```

> **Atenção:** `lambda` deve ser usado apenas para expressões simples. Se a lógica exige mais de uma linha, uma função convencional com `def` é sempre preferível — o código fica mais legível e testável.

### 3.7 Funções recursivas

Uma função recursiva é aquela que **chama a si mesma** dentro do próprio corpo. É útil para problemas que podem ser decompostos em versões menores do mesmo problema.

Toda função recursiva precisa de dois elementos obrigatórios:
1. **Caso base:** condição que interrompe a recursão
2. **Chamada recursiva:** a função se chama com um problema menor

```python
def calcular_fatorial(n):
    """Calcula o fatorial de n usando recursão.

    Args:
        n (int): Número inteiro não negativo.

    Returns:
        int: Fatorial de n.
    """
    if n == 0 or n == 1:   # caso base — interrompe a recursão
        return 1
    return n * calcular_fatorial(n - 1)  # chamada recursiva

print(calcular_fatorial(5))  # 120
```

Para entender o que acontece internamente:

```
calcular_fatorial(5)
  → 5 * calcular_fatorial(4)
       → 4 * calcular_fatorial(3)
            → 3 * calcular_fatorial(2)
                 → 2 * calcular_fatorial(1)
                      → 1  ← caso base
                 → 2 * 1 = 2
            → 3 * 2 = 6
       → 4 * 6 = 24
  → 5 * 24 = 120
```

Recursão é elegante, mas tem um custo: cada chamada ocupa memória na pilha de execução. Para problemas com muitas iterações, um laço `for` ou `while` é mais eficiente.


## 4. Escopo de variáveis

**Escopo** define onde uma variável pode ser acessada. Em Python, variáveis criadas dentro de uma função são **locais** — existem apenas enquanto a função está sendo executada e não são visíveis fora dela.

```python
def processar():
    resultado = 42       # variável local
    print(resultado)     # 42 — acessível dentro da função

processar()
print(resultado)         # NameError: name 'resultado' is not defined
```

Variáveis criadas fora de qualquer função são **globais** e podem ser lidas dentro de funções, mas não modificadas diretamente (sem a declaração `global`, que deve ser evitada).

```python
nota_minima = 7.0  # variável global

def verificar(nota):
    # pode LER a variável global
    return "Aprovado" if nota >= nota_minima else "Reprovado"

print(verificar(8.0))  # Aprovado

# Modificar a variável global dentro de uma função é tecnicamente possível,
# mas é uma prática que dificulta a manutenção do código.
# Prefira passar o valor como parâmetro.
def verificar_correto(nota, minima=7.0):
    return "Aprovado" if nota >= minima else "Reprovado"
```

## 5. Docstrings

Uma **docstring** é uma string de documentação colocada logo após a assinatura da função. Ela descreve o que a função faz, quais parâmetros recebe e o que retorna. É a forma padrão de documentar funções em Python (PEP 257).

```python
def calcular_desconto(preco, percentual):
    """Calcula o preço final após aplicação de desconto.

    Args:
        preco (float): Preço original do produto.
        percentual (float): Percentual de desconto entre 0 e 100.

    Returns:
        float: Preço com desconto aplicado.

    Raises:
        ValueError: Se o percentual estiver fora do intervalo [0, 100].
    """
    if not (0 <= percentual <= 100):
        raise ValueError(f"Percentual inválido: {percentual}. Deve estar entre 0 e 100.")
    return preco * (1 - percentual / 100)

print(calcular_desconto(200.0, 15))  # 170.0
```

A docstring pode ser consultada em tempo de execução com `help()`:

```python
help(calcular_desconto)
```

---

## 6. Validação de entradas

Uma função bem escrita verifica se os dados recebidos são válidos antes de processá-los. Isso evita erros silenciosos e produz mensagens de erro claras.

```python
def calcular_media(notas):
    """Calcula a média de uma lista de notas."""
    if not isinstance(notas, list):
        raise TypeError("O argumento 'notas' deve ser uma lista.")
    if len(notas) == 0:
        raise ValueError("A lista de notas não pode estar vazia.")
    if not all(isinstance(n, (int, float)) for n in notas):
        raise TypeError("Todos os elementos da lista devem ser numéricos.")
    return sum(notas) / len(notas)

# Uso correto
print(calcular_media([7.0, 8.5, 9.0]))  # 8.166...

# Usos incorretos — erros claros e descritivos
calcular_media("7, 8, 9")      # TypeError: O argumento 'notas' deve ser uma lista.
calcular_media([])              # ValueError: A lista de notas não pode estar vazia.
calcular_media([7, "oito", 9]) # TypeError: Todos os elementos da lista devem ser numéricos.
```


## 7. Boas práticas

**Uma função, uma responsabilidade.** Cada função deve realizar exatamente uma tarefa. Se o nome da função contém "e" (calcular_e_exibir, validar_e_salvar), provavelmente ela faz coisas demais e deve ser dividida.

**Nomenclatura descritiva.** O nome deve indicar o que a função faz, não como ela faz. `calcular_media` é melhor que `proc_vals`. Siga a convenção PEP 8: letras minúsculas separadas por `_`.

**Parâmetros limitados.** Funções com muitos parâmetros são difíceis de usar e testar. Se uma função precisa de mais de quatro ou cinco parâmetros, considere agrupar os dados em um dicionário ou em uma classe.

**Evite variáveis globais.** Prefira receber dados via parâmetros e devolvê-los via `return`. Dependências de variáveis globais tornam as funções difíceis de testar e reutilizar.

**Retorno explícito.** Mesmo quando a função não precisa retornar nada, seja consistente. Funções que às vezes retornam um valor e às vezes não retornam nada são fontes comuns de erros.

```python
# INCORRETO — retorno inconsistente
def buscar_aluno(matricula, turma):
    for aluno in turma:
        if aluno["matricula"] == matricula:
            return aluno
    # implicitamente retorna None — comportamento ambíguo

# CORRETO — retorno explícito e previsível
def buscar_aluno(matricula, turma):
    for aluno in turma:
        if aluno["matricula"] == matricula:
            return aluno
    return None  # deixa claro que nenhum resultado foi encontrado
```

## 8. Exemplo completo: sistema de boletim escolar

O exemplo a seguir integra os conceitos apresentados: funções com parâmetros, retorno, parâmetros padrão, validação e docstrings.

```python
def calcular_media(notas):
    """Calcula a média aritmética de uma lista de notas.

    Args:
        notas (list): Lista de valores numéricos.

    Returns:
        float: Média das notas, ou 0.0 se a lista estiver vazia.
    """
    if not notas:
        return 0.0
    return sum(notas) / len(notas)


def classificar_desempenho(media):
    """Classifica o desempenho com base na média.

    Args:
        media (float): Média do aluno.

    Returns:
        str: Classificação textual do desempenho.
    """
    if media >= 9.0:
        return "Excelente"
    elif media >= 7.0:
        return "Aprovado"
    elif media >= 5.0:
        return "Recuperação"
    else:
        return "Reprovado"


def gerar_boletim(turma, nota_minima=7.0):
    """Gera e exibe o boletim de uma turma.

    Args:
        turma (list): Lista de dicionários com 'nome' e 'notas'.
        nota_minima (float): Nota mínima para aprovação (padrão: 7.0).
    """
    print(f"{'Nome':<15} {'Média':>6} {'Situação':<15}")
    print("-" * 38)

    for aluno in turma:
        media = calcular_media(aluno["notas"])
        situacao = classificar_desempenho(media)
        print(f"{aluno['nome']:<15} {media:>6.2f} {situacao:<15}")


# Dados da turma
turma_2a = [
    {"nome": "Ana Silva",    "notas": [8.5, 9.0, 7.5]},
    {"nome": "Bruno Costa",  "notas": [6.0, 5.5, 6.5]},
    {"nome": "Carla Souza",  "notas": [9.5, 9.0, 10.0]},
    {"nome": "Diego Alves",  "notas": [4.0, 3.5, 5.0]},
    {"nome": "Emília Nunes", "notas": [7.0, 7.5, 6.5]},
]

gerar_boletim(turma_2a)

# Saída:
# Nome             Média Situação
# --------------------------------------
# Ana Silva         8.33 Excelente
# Bruno Costa       6.00 Recuperação
# Carla Souza       9.50 Excelente
# Diego Alves       4.17 Reprovado
# Emília Nunes      7.00 Aprovado
```
## 9. Erros frequentes

### Esquecer o `return`

```python
# INCORRETO — a função calcula mas não devolve o resultado
def calcular_area(base, altura):
    area = base * altura
    # esqueceu o return

resultado = calcular_area(5, 3)
print(resultado)  # None — não é o esperado

# CORRETO
def calcular_area(base, altura):
    return base * altura
```

### Modificar um argumento mutável sem intenção

Quando uma lista é passada como argumento, a função recebe uma referência ao mesmo objeto na memória. Modificá-la dentro da função altera o objeto original.

```python
def adicionar_nota(notas, nova_nota):
    notas.append(nova_nota)  # modifica a lista original!

minhas_notas = [7.0, 8.5]
adicionar_nota(minhas_notas, 9.0)
print(minhas_notas)  # [7.0, 8.5, 9.0] — foi alterada fora da função

# Se isso não for a intenção, trabalhe com uma cópia
def adicionar_nota_seguro(notas, nova_nota):
    copia = notas.copy()
    copia.append(nova_nota)
    return copia
```

### Parâmetro padrão mutável

Usar uma lista ou dicionário como valor padrão é um erro clássico em Python. O objeto padrão é criado **uma única vez** quando a função é definida, não a cada chamada.

```python
# INCORRETO — a lista padrão é compartilhada entre todas as chamadas
def registrar_nota(nota, historico=[]):
    historico.append(nota)
    return historico

print(registrar_nota(8.0))  # [8.0]
print(registrar_nota(9.5))  # [8.0, 9.5] — acumulou da chamada anterior!

# CORRETO — use None como padrão e crie o objeto dentro da função
def registrar_nota(nota, historico=None):
    if historico is None:
        historico = []
    historico.append(nota)
    return historico
```

---

## 10. Exercícios

**Exercício 1 — Saudação por turno**
Crie uma função que receba o nome de uma pessoa e o turno do dia (`"manhã"`, `"tarde"` ou `"noite"`) e retorne uma saudação personalizada. O turno deve ter valor padrão.
[Solução](https://github.com/claulis/Py/blob/main/LPPY/asset/code/ex_func_1.py)

**Exercício 2 — Calculadora de desconto**
Escreva uma função que receba o preço original de um produto e o percentual de desconto e retorne o preço final. Inclua validação para garantir que o percentual esteja entre 0 e 100.
[Solução](https://github.com/claulis/Py/blob/main/LPPY/asset/code/ex_func_2.py)

**Exercício 3 — Organizador de lista de compras**
Implemente duas funções: uma que adiciona itens a uma lista de compras com uma categoria opcional (padrão: `"Geral"`) e outra que exibe os itens numerados e agrupados por categoria.
[Solução](https://github.com/claulis/Py/blob/main/LPPY/asset/code/ex_func_.py)

---

> Ao encontrar um erro em uma função, o primeiro passo é verificar os valores que estão sendo passados como argumento. Use `print()` temporário ou o depurador do seu editor para inspecionar os dados no ponto de entrada da função — na maioria dos casos, o problema está nos dados, não na lógica.
