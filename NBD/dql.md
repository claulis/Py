# Comandos DQL no MySQL

## Seleção básica de colunas

Você pode escolher as colunas que deseja na consulta para trazer apenas o que é necessário.

```sql
SELECT nome, email FROM clientes;
```

Este comando retorna só as colunas nome e email da tabela clientes.

### Alias — apelidos para legibilidade

Permite dar nomes temporários às colunas ou tabelas, facilitando a leitura e uso em consultas complexas.

Exemplo de alias para coluna:

```sql
SELECT nome AS cliente, email AS contato FROM clientes;
```

Alias para tabela:

```sql
SELECT c.nome, c.email FROM clientes c;
```

Aqui 'c' é um apelido para a tabela clientes, útil para consultas com múltiplas tabelas.

***

### Claúsula WHERE — filtro de linhas

Serve para buscar apenas registros que atendam a uma condição.

Exemplo filtrar por idade maior que 30:

```sql
SELECT * FROM clientes WHERE idade > 30;
```

Você pode combinar condições com AND, OR e operadores lógicos:

```sql
SELECT * FROM clientes WHERE idade > 30 AND cidade = 'São Paulo';
```

## Junção de tabelas com JOIN

JOIN conecta tabelas relacionando colunas — importante para bancos relacionais.

- INNER JOIN: retorna só os registros com correspondência nas duas tabelas.

```sql
SELECT c.nome, p.valor
FROM clientes c
INNER JOIN pedidos p ON c.id = p.cliente_id;
```

- LEFT JOIN: retorna todos os clientes, mesmo os que não têm pedidos (valores NULL para pedidos).

```sql
SELECT c.nome, p.valor
FROM clientes c
LEFT JOIN pedidos p ON c.id = p.cliente_id;
```

## Agrupamento com GROUP BY

Agrupa linhas que tenham o mesmo valor em uma ou mais colunas, comum para sumários.

```sql
SELECT cidade, COUNT(*) AS numero_clientes
FROM clientes
GROUP BY cidade;
```

Isso mostra quantos clientes há em cada cidade.

## Filtro para grupos com HAVING

Filtra resultados do GROUP BY por condições nas agregações:

```sql
SELECT cidade, COUNT(*) AS numero_clientes
FROM clientes
GROUP BY cidade
HAVING numero_clientes > 10;
```

Mostra só cidades com mais de 10 clientes.

## Funções agregadas

Aplicam cálculos sobre grupos ou conjuntos:

- COUNT(): conta registros.
- SUM(): soma valores.
- AVG(): média.
- MIN(): valor mínimo.
- MAX(): valor máximo.

Exemplo calcular média salarial por departamento:

```sql
SELECT departamento, AVG(salario) AS media_salarial
FROM funcionarios
GROUP BY departamento;
```

## Subqueries (subconsultas)

Consultas dentro de outras consultas para lógica avançada.

Exemplo filtrar funcionários que ganham acima da média:

```sql
SELECT nome, salario
FROM funcionarios
WHERE salario > (SELECT AVG(salario) FROM funcionarios);
```

Exemplo subconsulta na cláusula FROM, para consulta intermediária:

```sql
SELECT departamento, media_salarial
FROM (
  SELECT departamento, AVG(salario) AS media_salarial
  FROM funcionarios
  GROUP BY departamento
) AS medias
WHERE media_salarial > 3000;
```

## Exemplo completo combinando recursos

```sql
SELECT c.nome AS cliente,
       COUNT(p.id) AS total_pedidos,
       AVG(p.valor) AS media_valor_pedidos
FROM clientes c
LEFT JOIN pedidos p ON c.id = p.cliente_id
WHERE c.cidade = 'São Paulo'
GROUP BY c.nome
HAVING total_pedidos > 2
ORDER BY media_valor_pedidos DESC
LIMIT 5;
```

Retorna os 5 clientes de São Paulo com mais de 2 pedidos, mostrando total e média de pedidos, ordenando do cliente com maior média para o menor.

## Resumo da sintaxe

| Recurso        | Explicação                  | Exemplo                         |
|----------------|----------------------------|--------------------------------|
| SELECT         | Define colunas a selecionar | `SELECT nome, email FROM clientes;` |
| AS (Alias)     | Dá apelido para colunas/tabelas | `SELECT nome AS cliente FROM clientes;` |
| WHERE          | Filtra linhas              | `WHERE idade > 30`              |
| JOIN           | Une tabelas                | `INNER JOIN pedidos ON clientes.id = pedidos.cliente_id` |
| GROUP BY       | Agrupa linhas              | `GROUP BY cidade`               |
| HAVING         | Filtra grupos              | `HAVING COUNT(*) > 10`          |
| Funções agregadas | Aplica sumarização       | `COUNT(*)`, `AVG(valor)`        |
| Subqueries     | Consultas aninhadas        | `WHERE salario > (SELECT AVG(salario) FROM funcionarios)` |

