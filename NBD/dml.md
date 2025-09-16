# Comandos DML no MySQL

DML é a linguagem usada para **inserir, alterar, excluir e consultar dados** dentro das tabelas do banco. São fundamentais em qualquer sistema que precise interagir dinamicamente com os dados.

## INSERT — Inserir dados

- Permite adicionar **novos registros** a uma tabela.
- Sintaxe geral:

  ```sql
  INSERT INTO nome_tabela (coluna1, coluna2, ...) VALUES (valor1, valor2, ...);
  ```

- Deve-se passar os valores na mesma ordem das colunas indicadas.
- Exemplo:

  ```sql
  INSERT INTO clientes (nome, idade, cidade) VALUES ('Ana', 30, 'São Paulo');
  ```

- Também suporta inserção múltipla:

  ```sql
  INSERT INTO produtos (nome, preco) VALUES ('Caneta', 1.5), ('Lápis', 1.0);
  ```

- Comando fundamental para alimentar tabelas com dados novos.

## UPDATE — Atualizar dados

- Permite **alterar registros existentes** em uma tabela.
- Sintaxe básica:

  ```sql
  UPDATE nome_tabela SET coluna1 = valor1, coluna2 = valor2, ... WHERE condição;
  ```

- A cláusula `WHERE` é crucial para definir quais registros serão modificados, evitando alterar toda a tabela.
- Exemplo:

  ```sql
  UPDATE clientes SET idade = 31 WHERE nome = 'Ana';
  ```

- Sem o `WHERE`, todas as linhas da tabela seriam atualizadas com os mesmos valores, o que geralmente não é desejado.
- Útil para corrigir, ajustar ou modificar dados existentes.

## DELETE — Excluir dados

- Remove registros da tabela.
- Sintaxe:

  ```sql
  DELETE FROM nome_tabela WHERE condição;
  ```

- Também deve usar `WHERE` para restringir os registros que serão deletados.
- Exemplo:

  ```sql
  DELETE FROM clientes WHERE nome = 'Ana';
  ```

- Sem `WHERE`, todos os registros da tabela podem ser apagados.
- Remove dados permanentemente, atenção ao uso.

## SELECT — Consultar dados

- Comando para **recuperar e visualizar dados** armazenados.
- Sintaxe básica:

  ```sql
  SELECT colunas FROM nome_tabela WHERE condição;
  ```

- Pode recuperar todos os dados (`SELECT *`), ou apenas colunas específicas.
- Exemplo:

  ```sql
  SELECT nome, idade FROM clientes WHERE cidade = 'São Paulo';
  ```

- Permite ordenar (`ORDER BY`), agrupar (`GROUP BY`), limitar resultados (`LIMIT`) e muito mais.
- Não altera dados, mas é fundamental para extrair informações.

## Considerações importantes sobre DML no MySQL

- Comandos DML geralmente são **transacionais**, ou seja, podem ser revertidos (rollback) ou confirmados (commit), importante para garantir consistência dos dados.
- Erros no uso dos comandos (como esquecer o `WHERE` em `UPDATE` ou `DELETE`) podem causar alterações ou perdas de dados indesejadas.
- São os comandos mais usados na manipulação diária de bancos para leitura e modificação de dados.
- Escolher bem as condições e usar cláusulas auxiliares é essencial para controlar o efeito das operações.

## Resumo prático

| Comando  | Função                             | Exemplo                                        |
|----------|----------------------------------|------------------------------------------------|
| INSERT   | Inserir novos registros          | `INSERT INTO clientes (nome, idade) VALUES ('João', 25);` |
| UPDATE   | Atualizar registros existentes   | `UPDATE clientes SET idade=26 WHERE nome='João';`         |
| DELETE   | Remover registros                | `DELETE FROM clientes WHERE nome='João';`                 |
| SELECT   | Consultar e recuperar dados      | `SELECT * FROM clientes WHERE idade > 20;`                |
