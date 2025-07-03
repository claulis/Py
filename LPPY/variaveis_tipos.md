# Aula: Variáveis e Tipos de Dados em Python

## O que são Variáveis?

Variáveis são espaços reservados na memória do computador para armazenar valores que podem ser usados e modificados durante a execução do programa. Elas funcionam como “caixas” que guardam informações, como números, textos ou outros dados, para que o programa possa trabalhar com eles.

Em Python, não é necessário declarar o tipo da variável antes de usá-la. Basta escolher um nome e atribuir um valor. O Python identifica automaticamente o tipo de dado.

## Características das variáveis em Python

- O nome da variável deve começar com uma letra ou underline (_).
- Não pode conter espaços ou caracteres especiais (exceto _).
- Python diferencia maiúsculas de minúsculas (ex: `idade` e `Idade` são variáveis diferentes).
- O tipo da variável é definido pelo valor atribuído.

**Exemplo:**

```python
nome = "Maria"      # str (texto)
idade = 25          # int (inteiro)
altura = 1.68       # float (decimal)
ativo = True        # bool (booleano)
```

## O que acontece na memória?

Quando o código acima é executado:

- O Python reserva um espaço para cada variável.
- Armazena o valor correspondente.
- Permite que o valor seja usado ou alterado depois.

## Mudando o valor de uma variável

Você pode alterar o valor de uma variável a qualquer momento:

```python
idade = 25
idade = 26  # Agora a variável idade vale 26
```

> Boas práticas para nomes de variáveis:
>
>- Use nomes descritivos: `nota_aluno`, `preco_produto`
>- Evite nomes muito curtos ou sem sentido: `a`, `x1`
>- Use letras minúsculas e, se necessário, underline para separar palavras

**Exemplo de boas práticas:**

```python
media_turma = 7.5
nome_completo = "Ana Souza"
```

---

## Tipos de Dados em Python

Python possui vários tipos de dados. Os mais comuns são:

| Tipo    | Exemplo           | Descrição                                 |
|---------|-------------------|-------------------------------------------|
| int     | 10, -5, 0         | Números inteiros                          |
| float   | 3.14, -2.0        | Números decimais                          |
| str     | "texto", 'abc'    | Cadeia de caracteres (texto)              |
| bool    | True, False       | Valores booleanos (lógico)                |
| list    | [1, 2, 3]         | Lista de elementos                        |
| dict    | {"a": 1, "b": 2}  | Dicionário (pares chave: valor)           |

**Exemplos práticos**

```python
quantidade = 10             # int
preco = 19.99               # float
produto = "Camiseta"        # str
disponivel = True           # bool
notas = [7, 8, 9]           # list
aluno = {"nome": "Ana", "idade": 17}  # dict
```

## Como descobrir o tipo de uma variável?

Use a função `type()`:

```python
print(type(quantidade))  # <class 'int'>
print(type(produto))     # <class 'str'>
```

---

## Entrada (input) e Saída (output) de Dados

### Entrada de dados (input)

Para receber informações do usuário pelo terminal, use a função `input()`. O valor recebido sempre será do tipo texto (`str`). Para usar como número, é preciso converter.

**Exemplo:**

```python
nome = input("Digite seu nome: ")  # Recebe texto
idade = int(input("Digite sua idade: "))  # Recebe texto e converte para inteiro
altura = float(input("Digite sua altura: "))  # Recebe texto e converte para decimal
```

### Saída de dados (output)

Para mostrar informações no terminal, use a função `print()`.

**Exemplo:**

```python
print("Nome:", nome)
print("Idade:", idade)
print("Altura:", altura)
```

---

### 5. Exemplo Prático no VS Code

1. Abra o VS Code e crie um arquivo chamado `exemplo_variaveis.py`.

2. Escreva o seguinte código:

```python
nome = input("Qual seu nome? ")
idade = int(input("Qual sua idade? "))
altura = float(input("Qual sua altura? "))

print("Nome:", nome)
print("Idade:", idade)
print("Altura:", altura)
```

3. Salve o arquivo e execute no terminal:

```bash
python exemplo_variaveis.py
```

---

## Exercícios de Geometria e Matemática Básica no Cotidiano

1. **Peça ao usuário o comprimento e a largura de um cômodo e calcule a área em metros quadrados.**

2. **Solicite o raio de uma pizza e calcule sua área (use π = 3.14).**

3. **Peça ao usuário a base e a altura de um triângulo e calcule sua área.**

4. **Solicite o valor do salário mensal e calcule quanto a pessoa receberia em um ano.**

5. **Peça ao usuário o valor de uma compra e o percentual de desconto. Calcule o valor final com desconto.**

6. **Solicite o valor gasto em combustível e a distância percorrida. Calcule o consumo médio (km/litro).**

7. **Peça ao usuário a quantidade de degraus de uma escada e a altura de cada degrau. Calcule a altura total da escada.**

8. **Solicite o valor de um produto e o número de parcelas. Calcule o valor de cada parcela.**

9. **Peça ao usuário o diâmetro de uma roda de bicicleta e calcule o perímetro (circunferência) da roda.**

10. **Solicite a largura e o comprimento de um terreno e calcule o valor total, sabendo o preço do metro**