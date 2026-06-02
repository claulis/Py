# Desafios de Fixação — Python

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

## Desafio 2 — Gerenciador de Estoque

### Enunciado

Crie um sistema de estoque simples para uma lanchonete, com menu interativo e operações de cadastro, listagem e busca de produtos.

### Instruções

1. O sistema deve ter um menu com as opções: **Adicionar produto**, **Listar estoque**, **Buscar produto** e **Sair**
2. Cada produto tem: nome, preço e quantidade em estoque
3. Ao listar, exiba os produtos ordenados por nome e indique `⚠ Estoque baixo` para produtos com quantidade ≤ 5
4. A busca deve ser por nome (parcial, sem distinção de maiúsculas/minúsculas)
5. Ao sair, exiba o valor total do estoque (soma de `preço × quantidade` de todos os produtos)

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


