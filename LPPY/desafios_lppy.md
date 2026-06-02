# Desafios de Fixação — Python

> **Como usar:** leia o enunciado, tente resolver por conta própria e consulte a solução apenas depois.

---

## Desafio 1 — Classificador de Notas com Estatísticas

### Enunciado

Crie um programa que leia as notas de uma turma e gere um relatório com as estatísticas da turma.

### Instruções

1. Pergunte ao usuário quantos alunos tem a turma
2. Para cada aluno, peça o nome e a nota (de 0 a 10)
3. Valide a nota: se for inválida (fora do intervalo), peça novamente
4. Ao final, exiba:
   - Lista de alunos com nome, nota e situação
   - Maior nota, menor nota e média da turma

**Regras de situação:**

| Nota          | Situação     |
|---------------|--------------|
| ≥ 7.0         | Aprovado     |
| 5.0 a 6.9     | Recuperação  |
| < 5.0         | Reprovado    |

**Conceitos exercitados:** `input`, `while`, `for`, listas, dicionários, funções, condicionais

### Saída esperada

```
=============================================
Nome                  Nota  Situação
---------------------------------------------
Ana Silva              8.5  Aprovado
Bruno Costa            6.0  Recuperação
Carla Souza            9.5  Aprovado
Diego Alves            4.0  Reprovado
---------------------------------------------
  Média da turma : 7.00
  Maior nota     : 9.5
  Menor nota     : 4.0
=============================================
```

### Solução

```python
def ler_nota_valida(nome):
    """Lê e valida uma nota entre 0 e 10."""
    while True:
        try:
            nota = float(input(f"  Nota de {nome}: "))
            if 0 <= nota <= 10:
                return nota
            print("  Nota inválida! Digite um valor entre 0 e 10.")
        except ValueError:
            print("  Entrada inválida! Digite um número.")


def classificar(nota):
    """Retorna a situação do aluno com base na nota."""
    if nota >= 7:
        return "Aprovado"
    elif nota >= 5:
        return "Recuperação"
    else:
        return "Reprovado"


def gerar_relatorio(turma):
    """Exibe o relatório completo da turma."""
    notas = [a["nota"] for a in turma]

    print("\n" + "=" * 45)
    print(f"{'Nome':<20} {'Nota':>6}  {'Situação'}")
    print("-" * 45)
    for aluno in turma:
        print(f"{aluno['nome']:<20} {aluno['nota']:>6.1f}  {classificar(aluno['nota'])}")

    print("-" * 45)
    print(f"  Média da turma : {sum(notas) / len(notas):.2f}")
    print(f"  Maior nota     : {max(notas):.1f}")
    print(f"  Menor nota     : {min(notas):.1f}")
    print("=" * 45)


# --- Programa principal ---
turma = []

quantidade = int(input("Quantos alunos na turma? "))

for i in range(1, quantidade + 1):
    print(f"\nAluno {i}:")
    nome = input("  Nome: ")
    nota = ler_nota_valida(nome)
    turma.append({"nome": nome, "nota": nota})

gerar_relatorio(turma)
```

---

## Desafio 2 — Gerenciador de Estoque

### Enunciado

Crie um sistema de estoque simples para uma lanchonete, com menu interativo e operações de cadastro, listagem e busca de produtos.

### Instruções

1. O sistema deve ter um menu com as opções: **Adicionar produto**, **Listar estoque**, **Buscar produto** e **Sair**
2. Cada produto tem: nome, preço e quantidade em estoque
3. Ao listar, exiba os produtos ordenados por nome e indique `⚠ Estoque baixo` para produtos com quantidade ≤ 5
4. A busca deve ser por nome (parcial, sem distinção de maiúsculas/minúsculas)
5. Ao sair, exiba o valor total do estoque (soma de `preço × quantidade` de todos os produtos)

**Conceitos exercitados:** `while`, funções, listas, dicionários, `lambda` para ordenação, métodos de string

### Saída esperada

```
====================================================
Produto              Preço    Qtd  Status
----------------------------------------------------
Coxinha              R$   3.50      4  ⚠ Estoque baixo
Pastel               R$   5.00     12
Suco de Laranja      R$   7.00      3  ⚠ Estoque baixo
====================================================

Valor total em estoque: R$ 119.00
```

### Solução

```python
estoque = []


def adicionar_produto():
    """Cadastra um novo produto no estoque."""
    nome = input("Nome do produto: ").strip()
    if not nome:
        print("Nome não pode ser vazio.")
        return
    try:
        preco = float(input("Preço (R$): "))
        quantidade = int(input("Quantidade: "))
        if preco < 0 or quantidade < 0:
            print("Preço e quantidade devem ser positivos.")
            return
    except ValueError:
        print("Valor inválido!")
        return

    estoque.append({"nome": nome, "preco": preco, "quantidade": quantidade})
    print(f"Produto '{nome}' cadastrado com sucesso!")


def listar_estoque():
    """Exibe todos os produtos ordenados por nome."""
    if not estoque:
        print("Estoque vazio.")
        return

    print("\n" + "=" * 52)
    print(f"{'Produto':<20} {'Preço':>8}  {'Qtd':>5}  {'Status'}")
    print("-" * 52)

    for produto in sorted(estoque, key=lambda p: p["nome"].lower()):
        status = "⚠ Estoque baixo" if produto["quantidade"] <= 5 else ""
        print(
            f"{produto['nome']:<20} "
            f"R$ {produto['preco']:>6.2f}  "
            f"{produto['quantidade']:>5}  "
            f"{status}"
        )
    print("=" * 52)


def buscar_produto():
    """Busca produtos pelo nome (parcial, sem case)."""
    termo = input("Digite o nome (ou parte dele): ").strip().lower()
    resultados = [p for p in estoque if termo in p["nome"].lower()]

    if not resultados:
        print("Nenhum produto encontrado.")
        return

    print(f"\n{len(resultados)} resultado(s) encontrado(s):")
    for p in resultados:
        print(f"  • {p['nome']} — R$ {p['preco']:.2f} | Qtd: {p['quantidade']}")


def exibir_resumo():
    """Calcula e exibe o valor total do estoque."""
    total = sum(p["preco"] * p["quantidade"] for p in estoque)
    print(f"\nValor total em estoque: R$ {total:.2f}")


# --- Menu principal ---
while True:
    print("\n=== Gerenciador de Estoque ===")
    print("1. Adicionar produto")
    print("2. Listar estoque")
    print("3. Buscar produto")
    print("4. Sair")

    opcao = input("Opção: ").strip()

    if opcao == "1":
        adicionar_produto()
    elif opcao == "2":
        listar_estoque()
    elif opcao == "3":
        buscar_produto()
    elif opcao == "4":
        exibir_resumo()
        print("Encerrando o sistema. Até logo!")
        break
    else:
        print("Opção inválida!")
```
