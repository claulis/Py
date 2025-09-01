# Estruturas de Seleção em Python

## Objetivos

- `if` simples  
- `if…else`  
- `if…elif…else`  
- aninhamento de condicionais  
- `match–case` (Python 3.10+)  
- operadores lógicos e tabela verdade  
- diversos exemplos práticos  

## 1. Estrutura `if` Simples

O `if` avalia uma condição booleana e executa um bloco de código apenas se ela for verdadeira.

Exemplo 1: verificar se um número é par  

```python
num = int(input("Digite um número inteiro: "))
if num % 2 == 0:
    print(f"{num} é par")
```

Exemplo 2: aplicar desconto genérico  

```python
valor = float(input("Valor da compra: R$ "))
if valor > 100:
    print("Você ganhou 10% de desconto!")
```

---

## 2. Estrutura `if…else`

Use `else` para tratar o caminho quando a condição do `if` for falsa.

Exemplo: positivo, negativo ou zero  

```python
n = float(input("Digite um número: "))
if n > 0:
    print("Positivo")
else:
    print("Zero ou Negativo")
```

---

## 3. Estrutura `if…elif…else`

Quando há múltiplas condições excludentes, use `elif` (“else if”).

Exemplo: faixa etária  

```python
idade = int(input("Idade: "))
if idade < 12:
    print("Criança")
elif idade < 18:
    print("Adolescente")
elif idade < 65:
    print("Adulto")
else:
    print("Idoso")
```

---

## 4. Condicionais Aninhadas

Você pode colocar um `if` dentro de outro para cenários ainda mais específicos.

Exemplo: login e senha  

```python
usuario = input("Usuário: ")
senha = input("Senha: ")
if usuario == "admin":
    if senha == "1234":
        print("Acesso liberado")
    else:
        print("Senha incorreta")
else:
    print("Usuário não encontrado")
```

Dica: muitos níveis de aninhamento podem dificultar a manutenção. Considere funções para clarear a lógica.

---

## 5. `match–case` (Python 3.10+)

Equivalente ao `switch` de outras linguagens, mas mais poderoso.

Exemplo 1: menu de operações  

```python
op = input("Escolha [+] [-] [*] [/]: ")
a = float(input("a = "))
b = float(input("b = "))

match op:
    case "+":
        print(a + b)
    case "-":
        print(a - b)
    case "*":
        print(a * b)
    case "/":
        if b != 0:
            print(a / b)
        else:
            print("Divisão por zero!")
    case _:
        print("Operação inválida")
```

Exemplo 2: dia da semana  

```python
d = int(input("Dia (1–7): "))
match d:
    case 1: print("Domingo")
    case 2: print("Segunda")
    case 3: print("Terça")
    case 4: print("Quarta")
    case 5: print("Quinta")
    case 6: print("Sexta")
    case 7: print("Sábado")
    case _: print("Valor fora de 1–7")
```

---

## 6. Operadores Lógicos e Tabela Verdade

Em Python usamos `and`, `or` e `not`. Veja a tabela verdade:

| A      | B      | A and B | A or B | not A |
|--------|--------|---------|--------|-------|
| True   | True   | True    | True   | False |
| True   | False  | False   | True   | False |
| False  | True   | False   | True   | True  |
| False  | False  | False   | False  | True  |

Exemplo: verificar intervalo fechado  

```python
x = int(input("Número: "))
if 0 <= x <= 50:
    print("Está entre 0 e 50")
else:
    print("Fora do intervalo")
```

---

## 7. Exemplos de Condições Compostas

1. Divisível por 3 **e** 5  

   ```python
   n = int(input("Digite um número: "))
   if n % 3 == 0 and n % 5 == 0:
       print("Divisível por 3 e 5")
   ```

2. Ano bissexto  

   ```python
   ano = int(input("Ano: "))
   if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
       print("Ano bissexto")
   else:
       print("Ano comum")
   ```

3. Lados de um triângulo  

   ```python
   a, b, c = map(int, input("Lados a b c: ").split())
   if a + b > c and a + c > b and b + c > a:
       print("Triângulo válido")
   else:
       print("Não é triângulo")
   ```

---

## 8. Exercícios Práticos

1. **Par ou Ímpar**  
   Faça um programa que leia um número inteiro e exiba “Par” se o número for par ou “Ímpar” caso contrário.

2. **Positivo, Negativo ou Zero**  
   Leia um número real e imprima:
   - “Positivo” se for maior que zero  
   - “Negativo” se for 
   
   menor que zero  
   - “Zero” se for igual a zero  

3. **Faixa Etária**  
   Receba a idade de uma pessoa e exiba a categoria:
   - 0–12: “Criança”  
   - 13–17: “Adolescente”  
   - 18–64: “Adulto”  
   - 65+: “Idoso”  

4. **Validação de Acesso**  
   Simule um sistema de login. Peça usuário e senha, e:
   - Se usuário for “admin” e senha “1234”, exiba “Acesso liberado”  
   - Caso contrário, “Acesso negado”  

5. **Desconto Progressivo**  
   Leia o valor de uma compra:
   - Se valor ≥ 200, aplique 20% de desconto  
   - Se 100 ≤ valor < 200, aplique 10% de desconto  
   - Caso contrário, sem desconto  
   Exiba o valor final.

6. **Senha Simples**  
   Peça ao usuário uma senha e valide:
   - Deve ter pelo menos 6 caracteres  
   - Deve conter pelo menos um dígito (`0–9`)  
   Se atender aos critérios, exiba “Senha válida”, caso contrário “Senha inválida”.

7. **FizzBuzz**  
   Para cada número de 1 a 20:
   - Se for múltiplo de 3, imprima “Fizz”  
   - Se for múltiplo de 5, imprima “Buzz”  
   - Se for múltiplo de 3 e 5, imprima “FizzBuzz”  
   - Caso contrário, imprima o próprio número  

8. **Validação de Triângulo**  
   Leia três valores (lados) e verifique se formam um triângulo (soma de dois lados maior que o terceiro). Exiba “Válido” ou “Inválido”.

9. **Dia da Semana (match–case)**  
   Use `match–case` para receber um número de 1 a 7 e exibir o dia correspondente (“Domingo” a “Sábado”). Para valores fora desse intervalo, exiba “Inválido”.

10. **Ano Bissexto**  
    Leia um ano e determine se é bissexto:
    - Divisível por 400, ou  
    - Divisível por 4 e não por 100  
    Exiba “Bissexto” ou “Comum”.

