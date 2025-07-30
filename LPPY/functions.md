# Funções em Python

## 1. Introdução

Em Python, uma função é definida como um bloco de código encapsulado que executa uma tarefa específica, promovendo modularidade e reutilização. Definida pela palavra-chave def, seguida por um nome, parâmetros opcionais entre parênteses e um bloco de código indentado, a função constitui uma unidade lógica que pode ser invocada em diferentes partes de um programa. Este mecanismo é essencial para estruturar aplicações complexas, reduzindo a redundância e facilitando a manutenção.

## 2. Propósito das Funções

Funções em Python existem para encapsular lógica que pode ser reutilizada em múltiplos contextos, minimizando a duplicação de código. Elas permitem a decomposição de problemas complexos em unidades menores e mais gerenciáveis, promovendo a separação de preocupações. Ao centralizar a lógica em um único ponto, uma função facilita modificações futuras, pois alterações em sua implementação propagam-se automaticamente para todas as chamadas. Além disso, funções contribuem para a legibilidade do código, uma vez que nomes descritivos fornecem uma abstração clara da funcionalidade implementada. Elas também suportam a testabilidade, permitindo que unidades específicas de lógica sejam validadas de forma isolada, o que é crítico em processos de depuração e desenvolvimento orientado a testes.
Por exemplo, considere um cenário em que um programa precisa calcular a média de valores numéricos em várias ocasiões. Sem funções, a lógica de cálculo seria repetida, aumentando o risco de erros e dificultando ajustes. Uma função calcular_media resolve esse problema ao encapsular a lógica, permitindo sua invocação com diferentes conjuntos de dados.

## 3. Quando Utilizar Funções

Um programador deve empregar funções quando uma tarefa específica é executada repetidamente em um programa, garantindo que a lógica seja definida apenas uma vez. Elas também são recomendadas quando se deseja isolar uma funcionalidade para melhorar a clareza ou facilitar a manutenção. Por exemplo, em um sistema que processa transações financeiras, funções separadas podem ser criadas para calcular impostos, validar pagamentos e gerar relatórios, promovendo uma arquitetura modular.

## 4. Utilizade das funções

- Tarefas repetitivas ocorrem, como cálculos ou transformações de dados que aparecem em múltiplos pontos do código;
- Separação de responsabilidades é necessária, dividindo a lógica em componentes independentes;
- Testes unitários são planejados, pois funções isoladas podem ser testadas sem dependências externas;
- Manutenção futura é uma preocupação, já que centralizar a lógica em uma função simplifica atualizações;
- Legibilidade é uma prioridade, pois funções com nomes descritivos servem como documentação implícita.

## 5. Tipos de Funções em Python

**Funções sem Parâmetros e sem Retorno.**
Essas funções executam uma ação sem depender de entradas externas ou produzir saídas explícitas. São úteis para tarefas simples, como exibir mensagens fixas.

```python
def exibir_saudacao():
    print("Bem-vindo ao sistema!")
exibir_saudacao()  # Saída: Bem-vindo ao sistema!
```

**Funções com Parâmetros**
Essas funções aceitam argumentos que permitem personalizar seu comportamento, aumentando a flexibilidade. Os parâmetros são definidos na assinatura da função.

```python
def saudacao_personalizada(nome):
    print(f"Olá, {nome}!")
saudacao_personalizada("Alice")  # Saída: Olá, Alice!
```

**Funções com Retorno**
Utilizam a palavra-chave return para fornecer um resultado ao chamador, permitindo que o valor seja usado em outras partes do programa.

```python
def calcular_quadrado(numero):
    return numero * numero
resultado = calcular_quadrado(5)
print(resultado)  # Saída: 25
```

**Funções com Parâmetros Padrão**
Permitem definir valores padrão para parâmetros, que são usados quando o argumento correspondente não é fornecido. Isso reduz a necessidade de chamadas redundantes com valores comuns.

```python
def saudacao_com_horario(nome, horario="manhã"):
    print(f"Bom {horario}, {nome}!")
saudacao_com_horario("Bob")  # Saída: Bom manhã, Bob!
saudacao_com_horario("Bob", "tarde")  # Saída: Bom tarde, Bob!
```

**Funções com Argumentos Variáveis**
Utilizam *args para aceitar um número variável de argumentos posicionais e **kwargs para argumentos nomeados, oferecendo flexibilidade em cenários com entradas dinâmicas.

```python
def somar_varios(*numeros):
    return sum(numeros)
print(somar_varios(1, 2, 3))  # Saída: 6
print(somar_varios(1, 2, 3, 4, 5))  # Saída: 15

def exibir_informacoes(**kwargs):
    for chave, valor in kwargs.items():
        print(f"{chave}: {valor}")
exibir_informacoes(nome="Carlos", idade=30)  # Saída: nome: Carlos \n idade: 30
```

**Funções Anônimas (Lambda)**
Definidas com a palavra-chave lambda, essas funções são usadas para operações curtas e inline, frequentemente em conjunto com funções como map ou filter.

```python
dobrar = lambda x: x * 2
print(dobrar(10))  # Saída: 20
```

**Funções Recursivas**
Funções que se auto-invocam para resolver problemas que podem ser divididos em subproblemas menores, como cálculos de fatorial ou busca em estruturas hierárquicas.

```python
def calcular_fatorial(n):
    if n == 0 or n == 1:
        return 1
    return n * calcular_fatorial(n - 1)
print(calcular_fatorial(5))  # Saída: 120
```

## 6. Melhores Práticas

**Nomenclatura Descritiva**
O nome de uma função deve refletir claramente sua funcionalidade, seguindo a convenção PEP 8 (letras minúsculas com underscores). Por exemplo, calcular_media é preferível a cm.

**Escopo Focado**
Uma função deve realizar uma única tarefa, aderindo ao princípio da responsabilidade única. Funções extensas devem ser refatoradas em unidades menores.

**Documentação com Docstrings**
Cada função deve incluir uma docstring que descreva seu propósito, parâmetros e valor de retorno, conforme a convenção PEP 257.

```python
def calcular_area_circulo(raio):
    """Calcula a área de um círculo com base no raio fornecido.

    Args:
        raio (float): O raio do círculo.
    
    Returns:
        float: A área calculada do círculo.
    """
    return 3.14159 * raio ** 2
```

**Evitar Efeitos Colaterais**
Funções devem operar apenas com os argumentos fornecidos, evitando modificações em variáveis globais ou estados externos, para garantir previsibilidade.

**Validação de Entradas**
Antes de executar operações, a função deve validar os argumentos para prevenir erros, utilizando exceções quando apropriado.

```python
def dividir_numeros(a, b):
    if b == 0:
        raise ValueError("Divisão por zero não é permitida.")
    return a / b
```

**Retorno Explícito**
O uso de return deve ser explícito, mesmo para retornar None, para evitar ambiguidades no comportamento da função.

**Limitação de Parâmetros**
Funções com muitos parâmetros podem ser refatoradas para usar `*args`, `**kwargs` ou estruturas de dados (como dicionários) para melhorar a clareza.

### Exemplo Prático

O código a seguir demonstra a implementação de um sistema que calcula a média de notas de alunos e determina o status de aprovação.

```python
def calcular_media(notas):
    """Calcula a média aritmética de uma lista de notas.

    Args:
        notas (list): Lista de valores numéricos representando notas.
    
    Returns:
        float: Média das notas ou 0 se a lista estiver vazia.
    """
    if not notas:
        return 0
    return sum(notas) / len(notas)

def verificar_aprovacao(media, nota_minima=7.0):
    """Determina o status de aprovação com base na média.

    Args:
        media (float): Média calculada das notas.
        nota_minima (float): Nota mínima para aprovação.
    
    Returns:
        str: 'Aprovado' se a média for suficiente, 'Reprovado' caso contrário.
    """
    return "Aprovado" if media >= nota_minima else "Reprovado"

# Exemplo de uso
notas_aluno = [8.5, 7.0, 9.0]
media = calcular_media(notas_aluno)
status = verificar_aprovacao(media)
print(f"Média: {media:.2f} - Status: {status}")  # Saída: Média: 8.17 - Status: Aprovado
```

### Estrutura sequencial X Funções

1. Sequencial

```python
# Notas de três alunos
notas_aluno1 = [7.5, 8.0, 6.5]
notas_aluno2 = [9.0, 8.5, 9.5]
notas_aluno3 = [6.0, 5.5, 7.0]

# Cálculo da média e aprovação do aluno 1
soma = 0
for nota in notas_aluno1:
    soma += nota
media_aluno1 = soma / len(notas_aluno1) if notas_aluno1 else 0
status_aluno1 = "Aprovado" if media_aluno1 >= 7.0 else "Reprovado"
print(f"Aluno 1 - Média: {media_aluno1:.2f}, Status: {status_aluno1}")

# Cálculo da média e aprovação do aluno 2
soma = 0
for nota in notas_aluno2:
    soma += nota
media_aluno2 = soma / len(notas_aluno2) if notas_aluno2 else 0
status_aluno2 = "Aprovado" if media_aluno2 >= 7.0 else "Reprovado"
print(f"Aluno 2 - Média: {media_aluno2:.2f}, Status: {status_aluno2}")

# Cálculo da média e aprovação do aluno 3
soma = 0
for nota in notas_aluno3:
    soma += nota
media_aluno3 = soma / len(notas_aluno3) if notas_aluno3 else 0
status_aluno3 = "Aprovado" if media_aluno3 >= 7.0 else "Reprovado"
print(f"Aluno 3 - Média: {media_aluno3:.2f}, Status: {status_aluno3}")

# Saída:
# Aluno 1 - Média: 7.33, Status: Aprovado
# Aluno 2 - Média: 9.00, Status: Aprovado
# Aluno 3 - Média: 6.17, Status: Reprovado
```

2. Refatorado com funções

```python
def calcular_media(notas):
    """Calcula a média aritmética de uma lista de notas.
    
    Args:
        notas (list): Lista de valores numéricos representando notas.
    
    Returns:
        float: Média das notas ou 0 se a lista estiver vazia.
    """
    return sum(notas) / len(notas) if notas else 0

def verificar_aprovacao(media, nota_minima=7.0):
    """Determina o status de aprovação com base na média.
    
    Args:
        media (float): Média calculada das notas.
        nota_minima (float): Nota mínima para aprovação.
    
    Returns:
        str: 'Aprovado' se a média for suficiente, 'Reprovado' caso contrário.
    """
    return "Aprovado" if media >= nota_minima else "Reprovado"

# Lista de alunos e suas notas
alunos = [
    {"nome": "Aluno 1", "notas": [7.5, 8.0, 6.5]},
    {"nome": "Aluno 2", "notas": [9.0, 8.5, 9.5]},
    {"nome": "Aluno 3", "notas": [6.0, 5.5, 7.0]}
]

# Processamento com funções
for aluno in alunos:
    media = calcular_media(aluno["notas"])
    status = verificar_aprovacao(media)
    print(f"{aluno['nome']} - Média: {media:.2f}, Status: {status}")

# Saída:
# Aluno 1 - Média: 7.33, Status: Aprovado
# Aluno 2 - Média: 9.00, Status: Aprovado
# Aluno 3 - Média: 6.17, Status: Reprovado
```

## 7. Exercicios

**Exercício 1: Saudação Personalizada por Turno**
Descrição: Crie uma função que gera uma saudação personalizada com base no nome de uma pessoa e no turno do dia (manhã, tarde ou noite). Use um parâmetro padrão para o turno. A função deve retornar a saudação formatada.

[Solução](/LPPY/asset/code/ex_func_1.py)

**Exercício 2: Calculadora de Desconto**
Descrição: Escreva uma função que calcula o preço final de um produto após aplicar um desconto percentual. A função deve receber o preço original e o percentual de desconto, retornando o valor com desconto.

[Solução](/LPPY/asset/code/ex_func_2.py)

**Exercício 3: Organizador de Lista de Compras**
Descrição: Escreva uma função que adiciona itens a uma lista de compras e outra que exibe os itens numerados. Use um parâmetro padrão para categorizar os itens (e.g., "Alimentos" como padrão).

[Solução](/LPPY/asset/code/ex_func_.py)
