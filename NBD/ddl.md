# Comandos DDL no MySQL

DDL é a linguagem que define a estrutura do banco de dados, ou seja, são os comandos que manipulam os objetos do banco, como bancos de dados, tabelas, índices e colunas. Diferente dos comandos que manipulam dados (DML), os comandos DDL atuam na criação, alteração e exclusão das estruturas.

## CREATE

- **CREATE DATABASE**: Cria um banco de dados vazio no servidor MySQL.
  - Propósito: Isolar um conjunto de tabelas e dados, permitindo organizar diferentes aplicações ou ambientes.
  - Sintaxe:

    ```sql
    CREATE DATABASE nome_do_banco;
    ```

  - Opções comuns: `IF NOT EXISTS` para evitar erro se já existir.
  - Exemplo:

    ```sql
    CREATE DATABASE empresa;
    ```

  - Quando executado, o MySQL cria um diretório para armazenar os dados daquele banco.

- **CREATE TABLE**: Cria uma tabela nova, definindo seu nome, colunas, tipos de dados e restrições.
  - Fundamental para armazenar dados relacionais.
  - Sintaxe básica:

    ```sql
    CREATE TABLE nome_tabela (
      coluna1 tipo_dado restricoes,
      coluna2 tipo_dado restricoes,
      ...
    );
    ```

  - Tipos comuns: `INT`, `VARCHAR(n)`, `DATE`, `DECIMAL`, entre outros.
  - Restrições comuns:
    - `PRIMARY KEY`: identifica a chave primária da tabela.
    - `NOT NULL`: indica que a coluna deve obrigatoriamente ter valor.
    - `UNIQUE`: valor único na coluna.
    - `FOREIGN KEY`: estabelece vínculo com chave primária de outra tabela (integridade referencial).
  - Exemplo completo:

    ```sql
    CREATE TABLE funcionario (
      id INT AUTO_INCREMENT PRIMARY KEY,
      nome VARCHAR(100) NOT NULL,
      salario DECIMAL(10,2),
      data_admissao DATE,
      departamento_id INT,
      FOREIGN KEY (departamento_id) REFERENCES departamento(id)
    );
    ```

  - O comando cria estrutura no banco e prepara espaço para os dados.

## ALTER

- Usado para fazer modificações estruturais em tabelas e bancos de dados já existentes.
- Possibilidades:
  - Adicionar colunas:

    ```sql
    ALTER TABLE nome_tabela ADD coluna tipo;
    ```

  - Modificar colunas (tipo, tamanho, restrições):

    ```sql
    ALTER TABLE nome_tabela MODIFY coluna novo_tipo;
    ```

  - Remover colunas:

    ```sql
    ALTER TABLE nome_tabela DROP COLUMN coluna;
    ```

  - Adicionar chaves primárias, estrangeiras, índices.
- Exemplo de uso:

  ```sql
  ALTER TABLE funcionario ADD telefone VARCHAR(15);
  ```

- Pode ser usado para alterar nomes de tabelas e até o engine do banco de dados.
- Muito importante para evolução de projetos, pois permite adaptar estruturas sem perder dados.

## DROP

- Remove bancos de dados, tabelas ou outros objetos do banco de dados de forma permanente.
- **DROP DATABASE**: apaga todo o banco de dados e seus dados.

  ```sql
  DROP DATABASE nome_do_banco;
  ```

- **DROP TABLE**: elimina a tabela e todos os dados que ela contém.

  ```sql
  DROP TABLE nome_tabela;
  ```

- Deve ser usado com extremo cuidado, pois é irreversible.
- É uma forma rápida e definitiva de limpar dados ou remover estruturas desnecessárias.

## TRUNCATE

- Remove todos os registros de uma tabela, mas mantém sua estrutura para ser reutilizada.
- Sintaxe:

  ```sql
  TRUNCATE TABLE nome_tabela;
  ```

- Funciona de maneira mais rápida que um DELETE sem WHERE, pois não gera logs detalhados para cada linha excluída.
- Usado quando se deseja limpar uma tabela inteira sem apagar e recriar.
- Atenção: não pode ser revertido e não aciona triggers de DELETE.

## Restrições, Índices e Chaves

- Esses elementos também são criados via DDL:
  - **PRIMARY KEY**: garante unicidade e identificação única da linha.
  - **FOREIGN KEY**: mantém integridade referencial entre tabelas, com ações ON DELETE e ON UPDATE para definir comportamentos em cascata, restrição ou nulo.
  - **UNIQUE**: impede duplicidades em uma coluna.
  - **INDEX**: acelera consultas em colunas específicas.

Estes podem ser criados junto com a tabela, ou depois via ALTER.

## Considerações importantes

- Comandos DDL são auto-comitáveis no MySQL, ou seja, qualquer modificação é efetivada imediatamente.
- São comandos críticos para a arquitetura do banco de dados, e seu uso incorreto pode causar perda de dados.
- Normalmente usados por administradores de banco e desenvolvedores para definir o modelo de dados.
- DDL não manipula os dados propriamente ditos, mas os objetos que armazenam esses dados.

