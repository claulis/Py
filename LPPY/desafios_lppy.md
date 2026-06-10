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
[Solução aqui](/LPPY/asset/code/desafio1.py)

## Desafio 2 —Classificador de Notas com Estatísticas com cadastro de alunos

### Enunciado

Pegue o exemplo do desafio 1 e agora implemente um cadastro aluno, mantendo as funcionalidades de antes.

### Instruções

1. Imprimir um menu de escolha
2. Escolher se incluir, remover e listar
3. Imprimir as estatísticas após cada interação
4. Manter as funcionalidades do desafio 1

