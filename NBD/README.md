# Banco de dados

## Sumário

- [O Que É um Banco de Dados?](#o-que-é-um-banco-de-dados)
- [Sistemas de Gerenciamento de Bancos de Dados (DBMS)](#sistemas-de-gerenciamento-de-bancos-de-dados-dbms)
- [Modelos de Dados](#modelos-de-dados)
- [Tabelas: A Estrutura Básica de Armazenamento de Dados](#tabelas-a-estrutura-básica-de-armazenamento-de-dados)
- [Chaves Primárias (Primary Keys): Identificadores Únicos](#chaves-primárias-primary-keys-identificadores-únicos)
- [Chaves Estrangeiras (Foreign Keys): Conexões entre Tabelas](#chaves-estrangeiras-foreign-keys-conexões-entre-tabelas)
- [Bancos de Dados Relacionais vs. Não Relacionais](#bancos-de-dados-relacionais-vs-não-relacionais)
- [Linguagem SQL (Structured Query Language)](#linguagem-sql-structured-query-language)
- [Entidade-Relacionamento (ER Model)](#entidade-relacionamento-er-model)
- [Normalização](#normalização)
- [Índices: Aceleradores de Consultas](#índices-aceleradores-de-consultas)
- [Propriedades ACID](#propriedades-acid)
- [Transações](#transações)
- [Segurança em Bancos de Dados](#segurança-em-bancos-de-dados)
- [Big Data e Bancos Distribuídos](#big-data-e-bancos-distribuídos)
- [Backup e Recuperação](#backup-e-recuperação)
- [Como Tudo Se Conecta](#como-tudo-se-conecta)
- [Exemplos Completos](#exemplos-completos)

## O Que É um Banco de Dados?

- **Elementos Fundamentais**:
  - **Dados**: Podem ser estruturados (ex.: números em colunas), semi-estruturados (ex.: XML ou JSON) ou não estruturados (ex.: imagens ou vídeos). Em um banco relacional, dados são armazenados em tabelas, onde cada linha é um registro e cada coluna é um atributo.
  - **Metadados**: "Dados sobre dados", como o esquema que define tipos de dados (inteiro, string, data), constraints (restrições como "não nulo") e índices para otimização.
  - **Relacionamentos**: Como dados se conectam, por exemplo, um cliente relacionado a múltiplos pedidos.

- **História Breve**: Os bancos de dados evoluíram dos anos 1960 com sistemas hierárquicos (como IMS da IBM) para o modelo relacional nos anos 1970, graças a Edgar F. Codd, que propôs o uso de álgebra relacional para manipulação de dados.

- **Exemplos Práticos**:
  - **Simples**: Uma agenda de contatos no celular é um banco de dados básico.
  - **Complexo**: O sistema do Google armazena bilhões de páginas web indexadas, permitindo buscas em milissegundos.
  - **Uso Diário**: Em um e-commerce como Amazon, o banco gerencia inventário, avaliações de usuários e histórico de compras.

- **Vantagens Detalhadas**:
  - **Eficiência**: Reduz duplicação (redundância), evitando inconsistências (ex.: mesmo endereço de cliente armazenado em múltiplos lugares).
  - **Compartilhamento**: Suporta acesso concorrente por múltiplos usuários ou aplicações.
  - **Integridade**: Impõe regras, como validação de dados (ex.: idade deve ser positiva).
  - **Escalabilidade**: Pode crescer de megabytes para petabytes.

- **Desvantagens e Desafios**:
  - **Custo**: Manutenção de hardware e software pode ser alta para grandes sistemas.
  - **Complexidade**: Requer conhecimento para design e queries, levando a curvas de aprendizado íngremes.
  - **Desempenho**: Em volumes extremos, pode haver gargalos sem otimização.

- **Por Que Estudar Isso?** Entender o conceito básico é crucial porque bancos de dados são o backbone de praticamente todos os sistemas digitais modernos, de apps móveis a IA. Sem eles, dados seriam caóticos, como uma biblioteca sem catálogo.

## Sistemas de Gerenciamento de Bancos de Dados (DBMS)

Um DBMS é o software intermediário entre o usuário (ou aplicação) e os dados físicos armazenados. Ele abstrai a complexidade do armazenamento em disco, memória e rede, fornecendo uma interface amigável. Pense nele como o "gerente" de uma empresa: coordena, otimiza e protege.

- **Arquitetura Detalhada**:
  - **Camadas**: Interface de usuário (ex.: GUI como phpMyAdmin), Processador de Queries (otimiza SQL), Gerenciador de Armazenamento (lida com arquivos e buffers), Gerenciador de Transações (ver ACID mais adiante).
  - **Componentes Internos**: Motor de Execução (executa planos de query), Otimizador (escolhe o melhor caminho para uma consulta, usando estatísticas), Lock Manager (gerencia concorrência).

- **Tipos de DBMS em Profundidade**:
  - **RDBMS**: Baseados em SQL, como MySQL (open-source, bom para web), PostgreSQL (avançado, com suporte a JSON), Oracle (empresarial, robusto para grandes corporações), SQL Server (da Microsoft, integrado com .NET).
  - **NoSQL**: Para dados flexíveis; MongoDB para documentos, Redis para key-value (rápido para caches), Neo4j para grafos (ideal para redes sociais ou recomendações).
  - **Outros**: NewSQL (como CockroachDB, combina SQL com escalabilidade NoSQL), In-Memory (como SAP HANA, armazena dados na RAM para velocidade extrema).

- **Funções Expandidas**:
  - **Gerenciamento de Dados**: CRUD (Create, Read, Update, Delete) operations.
  - **Controle de Concorrência**: Usa locks (exclusivos ou compartilhados) ou MVCC (Multi-Version Concurrency Control) para evitar "dirty reads".
  - **Recuperação**: Logs de transações para rollback em falhas.
  - **Segurança**: Criptografia em repouso e em trânsito, auditoria de acessos.

- **Exemplo de Uso**: Em um app bancário, o DBMS garante que uma transferência seja atômica, mesmo com milhares de transações por segundo.

- **Vantagens e Desvantagens**:
  - **Vantagens**: Automatização de backups, replicação para alta disponibilidade, suporte a views (visões virtuais de dados).
  - **Desvantagens**: Overhead de performance em sistemas simples; licenças caras para versões enterprise.

- **Importância**: O DBMS transforma dados brutos em informações acionáveis, sendo essencial para desenvolvedores e administradores de sistemas.

## Modelos de Dados

Modelos de dados são abstrações que definem como dados são representados, armazenados e manipulados. Eles evoluíram para atender necessidades variadas, de rigidez a flexibilidade.

- **Modelo Hierárquico**: Organiza os dados como uma árvore, em que cada registro tem um único "pai" e pode ter vários "filhos".
  - *Exemplo*: um sistema de arquivos, onde cada pasta tem subpastas.
  - *Vantagem*: navegação muito rápida quando a relação já é naturalmente hierárquica.
  - *Desvantagem*: relações muitos-para-muitos são difíceis de representar — um registro com dois "pais" obriga a duplicar o dado. Foi muito usado em mainframes antigos e caiu em desuso.

- **Modelo em Rede**: Evolução do hierárquico — um registro pode ter múltiplos pais e múltiplos filhos, formando uma rede em vez de uma árvore. Baseado no padrão CODASYL.
  - *Exemplo*: um funcionário que reporta a dois gerentes ao mesmo tempo.
  - *Vantagem*: mais flexível que o hierárquico.
  - *Desvantagem*: navegar pela rede exige seguir "ponteiros" manuais entre registros — complexo de programar e manter.

- **Modelo Relacional**: Organiza os dados em tabelas (relações), com linhas (tuplas) e colunas (atributos), conectadas por chaves primárias e estrangeiras em vez de ponteiros. É o modelo detalhado no restante deste material.
  - *Exemplo*: uma tabela "Empregados" (com ID como chave primária) ligada a uma tabela "Departamentos".
  - *Vantagem*: simples de entender e muito poderoso para consultas — apoiado na álgebra relacional (seleção, projeção, união).
  - *Desvantagem*: o esquema é rígido; mudar a estrutura de uma tabela em produção exige planejamento.

- **Modelo Orientado a Objetos (OODBMS)**: Guarda os dados como objetos de uma linguagem de programação, com classes, herança e encapsulamento, em vez de "traduzir" objetos para linhas de tabela.
  - *Exemplo*: um objeto `Carro` que já carrega seus próprios métodos, salvo diretamente no banco.
  - *Vantagem*: natural para linguagens orientadas a objetos como Java.
  - *Desvantagem*: menos padronizado entre fornecedores; usado principalmente em nichos como CAD e multimídia.

- **Modelo de Documentos**: Armazena cada registro como um documento autocontido, geralmente em JSON ou BSON, em vez de espalhar os dados em várias tabelas.
  - *Exemplo*: `{ "nome": "João", "enderecos": ["Rua A, 123", "Av. B, 456"] }` guarda todos os endereços de João em um único documento.
  - *Vantagem*: schema flexível — documentos da mesma coleção podem ter campos diferentes entre si.
  - *Desvantagem*: joins entre documentos são mais difíceis e menos eficientes do que em um banco relacional.

- **Outros Modelos**: Colunar (armazena por coluna em vez de por linha, ótimo para analytics, ex.: BigQuery) e Grafos (nós e arestas representam as relações diretamente, ex.: o grafo social do Facebook).

- **Exemplo Comparativo** (em tabela para clareza):

| Modelo       | Estrutura Principal | Exemplo de Uso          | Força Principal     |
|--------------|---------------------|-------------------------|---------------------|
| Hierárquico | Árvore             | Sistemas de arquivos   | Hierarquias simples |
| Relacional  | Tabelas            | Bancos transacionais   | Consistência       |
| Documentos  | JSON-like          | Apps web dinâmicos     | Flexibilidade      |

- **Importância**: O modelo certo alinha com os requisitos da aplicação, afetando performance e manutenção.

**Exercícios de fixação:**

1. Explique a diferença entre o modelo hierárquico e o modelo em rede, citando um exemplo de cada.
2. Por que o modelo relacional se tornou dominante em vez do hierárquico ou em rede?
3. Em qual cenário um modelo de documentos (JSON) seria mais adequado que um modelo relacional?

## Tabelas: A Estrutura Básica de Armazenamento de Dados

As tabelas são o coração de um banco de dados relacional. Elas representam uma coleção organizada de dados em formato de grade, semelhante a uma planilha do Excel, mas com regras rigorosas para garantir consistência e integridade. Formalmente, uma tabela é uma relação matemática composta por linhas (tuplas ou registros) e colunas (atributos ou campos). Cada tabela armazena dados sobre uma entidade específica do mundo real, como "Clientes" ou "Produtos".

- **Componentes Detalhados de uma Tabela**:
  - **Colunas**: Definidas por um nome, tipo de dado (ex.: INT para inteiros, VARCHAR para textos variáveis, DATE para datas) e constraints (restrições, como NOT NULL para valores obrigatórios ou DEFAULT para valores padrão).
  - **Linhas**: Cada uma representa uma instância única da entidade. Por exemplo, uma linha na tabela "Clientes" poderia ser: ID=1, Nome="João Silva", Idade=30.
  - **Esquema**: A definição da tabela, incluindo colunas e tipos, criada via DDL (Data Definition Language) em SQL.
  - **Constraints Gerais**: Além das por coluna, há UNIQUE (valores únicos), CHECK (condições personalizadas, ex.: Idade > 18).

- **Criação e Manipulação em SQL**:
  - Comando básico: `CREATE TABLE Clientes (ID INT NOT NULL, Nome VARCHAR(100), Idade INT CHECK (Idade >= 0));`
  - Inserir dados: `INSERT INTO Clientes (ID, Nome, Idade) VALUES (1, 'João Silva', 30);`
  - Consultar: `SELECT * FROM Clientes WHERE Idade > 25;`
  - Alterar estrutura: `ALTER TABLE Clientes ADD COLUMN Email VARCHAR(50);`
  - Excluir: `DROP TABLE Clientes;` (cuidado, isso remove tudo!).

- **Exemplos Práticos**:
  - **Analogia**: Imagine uma tabela como uma ficha de cadastro em uma biblioteca. Cada coluna é um campo (Nome do Livro, Autor, Ano), e cada linha é um livro específico.
  - **Uso Real**: Em um sistema de e-commerce, a tabela "Produtos" poderia ter colunas como ID_Produto, Nome, Preco, Estoque. Isso permite consultas como "todos os produtos com preço abaixo de R$100".

- **Vantagens das Tabelas**:
  - **Organização**: Facilitam a modelagem de entidades do mundo real, reduzindo redundância quando combinadas com normalização (ex.: evitam repetir o endereço de um cliente em múltiplos pedidos).
  - **Flexibilidade**: Podem ser relacionadas via joins para consultas complexas.
  - **Eficiência**: Otimizadas para operações CRUD (Create, Read, Update, Delete).
  - **Integridade**: Constraints embutidos previnem dados inválidos.

- **Desvantagens e Considerações**:
  - **Rigidez**: O esquema é fixo; alterar colunas em produção pode requerer migrações cuidadosas para evitar perda de dados.
  - **Desempenho em Grandes Escalas**: Tabelas muito largas (muitas colunas) ou altas (milhões de linhas) podem exigir particionamento (dividir em sub-tabelas) ou sharding (distribuir em servidores).
  - **Limitações**: Não ideais para dados não estruturados (ex.: imagens grandes); use blobs ou arquivos externos para isso.

- **Por Que São Importantes?** Tabelas são a unidade mínima de armazenamento lógico. Sem elas, os dados seriam uma sopa desorganizada, impossibilitando consultas eficientes. Elas formam a base para os outros conceitos que discutiremos.

**Exercícios de fixação:**

1. Escreva o comando `CREATE TABLE` para uma tabela `Livros` com as colunas: `ID` (chave primária, auto incremento), `Titulo` (texto de até 150 caracteres, obrigatório), `Ano` (inteiro) e `Preco` (decimal com 2 casas, deve ser maior que 0).

   <details><summary>Ver resposta</summary>

   ```sql
   CREATE TABLE Livros (
     ID INT AUTO_INCREMENT PRIMARY KEY,
     Titulo VARCHAR(150) NOT NULL,
     Ano INT,
     Preco DECIMAL(10,2) CHECK (Preco > 0)
   );
   ```

   </details>

2. O que acontece se você tentar inserir uma linha na tabela acima sem informar o campo `Titulo`? Por quê?

## Chaves Primárias (Primary Keys): Identificadores Únicos

Uma chave primária (PK) é um atributo (ou conjunto de atributos) que identifica unicamente cada registro em uma tabela. Ela garante que não haja duplicatas e serve como referência para relacionamentos. Toda tabela bem projetada deve ter uma PK, que é automaticamente indexada (veremos índices adiante) para buscas rápidas.

- **Características Detalhadas**:
  - **Única e Não Nula**: Nenhum valor pode se repetir ou ser NULL.
  - **Tipos Comuns**: INT AUTO_INCREMENT (gerado automaticamente), UUID (para distribuição), ou composta (múltiplas colunas, ex.: Codigo_Pais + Codigo_Cidade).
  - **Escolha da PK**: Prefira valores artificiais (surrogate keys, como IDs sequenciais) em vez de naturais (ex.: CPF, que pode mudar ou ter exceções).
  - **Constraints**: Definida com PRIMARY KEY no SQL.

- **Criação e Uso em SQL**:
  - Simples: `CREATE TABLE Clientes (ID INT PRIMARY KEY AUTO_INCREMENT, Nome VARCHAR(100));`
  - Composta: `CREATE TABLE Pedidos_Itens (Pedido_ID INT, Produto_ID INT, PRIMARY KEY (Pedido_ID, Produto_ID));`
  - Consultar: PKs são usadas implicitamente em WHERE, ex.: `SELECT * FROM Clientes WHERE ID = 1;`

- **Exemplos Práticos**:
  - **Analogia**: Como um número de matrícula em uma universidade – único para cada aluno, usado para acessar notas ou histórico.
  - **Uso Real**: Em uma tabela "Funcionarios", a PK "ID_Funcionario" garante que cada empregado seja único, evitando confusões como dois "João Silva".

- **Vantagens das Chaves Primárias**:
  - **Identificação Única**: Elimina ambiguidades e facilita joins.
  - **Integridade Referencial**: Serve como base para chaves estrangeiras.
  - **Otimização**: Automaticamente cria um índice, acelerando buscas.
  - **Escalabilidade**: IDs sequenciais são eficientes em armazenamento.

- **Desvantagens e Considerações**:
  - **Overhead**: Em tabelas com PKs compostas, inserts podem ser mais lentos devido a verificações de unicidade.
  - **Escolha Errada**: Usar dados sensíveis como PK (ex.: email) pode complicar mudanças futuras.
  - **Limitações**: Em bancos distribuídos, IDs sequenciais podem causar hotspots; use UUIDs para evitar.

- **Por Que São Importantes?** Sem PKs, tabelas seriam como listas sem IDs – impossível referenciar itens de forma confiável, levando a dados duplicados e inconsistentes.

**Exercícios de fixação:**

1. Por que geralmente é melhor usar uma chave artificial (surrogate, ex.: ID) em vez do CPF como chave primária de uma tabela de Clientes?
2. Dê um exemplo de chave primária composta e explique em que situação ela é necessária.

## Chaves Estrangeiras (Foreign Keys): Conexões entre Tabelas

Uma chave estrangeira (FK) é um atributo em uma tabela que referencia a PK de outra tabela, estabelecendo um relacionamento. Ela garante que todo valor gravado na FK já exista como PK na tabela referenciada — isso previne "órfãos" (registros sem pai válido) e modela relações como 1:N (um para muitos) ou N:N (muitos para muitos, via tabela intermediária).

- **Características Detalhadas**:
  - **Referencial**: Deve combinar o tipo e o tamanho da PK referenciada.
  - **Ações em Cascata**: ON DELETE CASCADE (exclui filhos ao deletar pai), ON UPDATE RESTRICT (impede atualizações que quebrem referências).
  - **Relacionamentos**: 1:1 (raro, ex.: perfil de usuário), 1:N (comum, ex.: um cliente tem muitos pedidos), N:N (ex.: alunos e cursos, via tabela de matrículas).
  - **Constraints**: Definida com FOREIGN KEY ... REFERENCES.

- **Criação e Uso em SQL**:
  - Exemplo: `CREATE TABLE Pedidos (ID INT PRIMARY KEY, Cliente_ID INT, FOREIGN KEY (Cliente_ID) REFERENCES Clientes(ID) ON DELETE CASCADE);`
  - Insert: `INSERT INTO Pedidos (ID, Cliente_ID) VALUES (101, 1);` (falha se Cliente_ID=1 não existir).
  - Join: `SELECT Clientes.Nome, Pedidos.ID FROM Clientes INNER JOIN Pedidos ON Clientes.ID = Pedidos.Cliente_ID;`

- **Exemplos Práticos**:
  - **Analogia**: Como um endereço que referencia uma cidade – o CEP deve existir na tabela de cidades, senão é inválido.
  - **Uso Real**: Em um banco de hospital, a tabela "Consultas" tem FK para "Pacientes.ID", garantindo que consultas sejam ligadas a pacientes reais.

- **Vantagens das Chaves Estrangeiras**:
  - **Integridade**: Previne dados inconsistentes (ex.: pedido sem cliente).
  - **Relacionamentos**: Permite modelar o mundo real de forma relacional.
  - **Automação**: Cascatas simplificam manutenção (ex.: deletar cliente remove pedidos automaticamente).
  - **Consultas Poderosas**: Facilita joins para dados combinados.

- **Desvantagens e Considerações**:
  - **Overhead de Performance**: Verificações em inserts/updates podem ralentizar em volumes altos; desative temporariamente em bulk operations.
  - **Ciclos**: Evite ciclos de referências (tabela A referencia B, B referencia A) para não complicar deletes.
  - **Limitações**: Em NoSQL, FKs não são nativas; use IDs manuais.

- **Por Que São Importantes?** FKs transformam tabelas isoladas em um sistema interconectado, essencial para bancos normalizados e consultas complexas.

**Exercícios de fixação:**

1. Escreva o SQL para criar uma tabela `Matriculas` que referencia `Alunos.ID` e `Cursos.ID`, apagando as matrículas automaticamente quando o aluno for removido.
2. O que é um registro "órfão" e como a FK evita isso?

## Bancos de Dados Relacionais vs. Não Relacionais

Essa distinção é pivotal na era do big data.

- **Relacionais (SQL)**:
  - **Características**: Esquema fixo, ACID-compliant, queries complexas com joins, subqueries e agregações (SUM, AVG).
  - **Internals**: Armazenamento row-based (bom para transações), normalização para integridade.
  - **Exemplos**: MySQL para WordPress, PostgreSQL para GIS.
  - **Vantagens**: Forte consistência, maturidade, ferramentas de BI.
  - **Desvantagens**: Escalabilidade vertical limitada; schema changes são disruptivos.

- **Não Relacionais (NoSQL)**:
  - **Características**: Esquema flexível, segue o modelo BASE (Basically Available, Soft state, Eventual consistency) em vez de ACID — o sistema prioriza estar sempre disponível e aceita que, por um curto período, réplicas diferentes mostrem valores levemente desatualizados até se sincronizarem. *Exemplo*: ao curtir uma foto no Instagram, o contador pode demorar um instante para atualizar em todos os servidores — isso é consistência eventual, e é aceitável nesse caso (diferente de um saldo bancário, onde não seria).
  - **Tipos Detalhados**:
    - Key-Value: Simples como dicionários (ex.: Redis para sessões de usuário).
    - Documentos: Para dados nested (ex.: MongoDB para logs).
    - Colunares: Otimizado para leituras analíticas (ex.: Cassandra para time-series).
    - Grafos: Para travessias (ex.: Neo4j para fraudes detection).
  - **Exemplos**: DynamoDB na AWS para escalabilidade serverless.
  - **Vantagens**: Horizontal scaling, tolerância a falhas, alta throughput.
  - **Desvantagens**: Consistência eventual pode levar a dados "stale"; queries limitadas sem SQL-like.

- **Quando Escolher?** Relacional para finanças (precisão); NoSQL para IoT (volume).

- **Importância**: A escolha impacta arquitetura de sistemas; híbridos (polyglot persistence) são comuns hoje.

## Linguagem SQL (Structured Query Language)

SQL é declarativa: você descreve o que quer, não como obter. Pronuncia-se "sequel" ou "S-Q-L".

SQL (Structured Query Language), ou Linguagem de Consulta Estruturada, é a linguagem padrão utilizada para gerenciar e manipular bancos de dados relacionais. Ela foi criada na década de 1970 baseada no modelo relacional de dados, e desde então tornou-se fundamental para qualquer sistema que precise armazenar, consultar e modificar dados organizados em tabelas.

SQL é uma **linguagem declarativa** que permite ao usuário especificar o **que deseja obter ou modificar nos dados, sem precisar dizer como o banco de dados deve executar** essas operações. Basicamente, o usuário escreve comandos SQL e o sistema gerenciador do banco de dados (SGBD), como MySQL, PostgreSQL, Oracle, SQL Server, entre outros, interpreta e executa essas consultas ou comandos.

Um banco de dados relacional SQL organiza as informações em tabelas compostas por linhas (registros) e colunas (campos). Cada coluna representa um atributo e cada linha representa uma entidade ou instância do dado.

### Principais componentes e comandos do SQL

- [**DDL (Data Definition Language):**](/NBD/ddl.md) Cria e altera estruturas de bancos, tabelas e índices. Exemplos: `CREATE`, `ALTER`, `DROP`.
- [**DML (Data Manipulation Language):**](/NBD/dml.md) Manipula dados armazenados, como inserir, atualizar, excluir.
- [**DQL (Data Query Language):**](/NBD/dql.md) Consulta dados.
- **DCL (Data Control Language):** Controla permissões e acessos.
- **TCL (Transaction Control Language):** Controla transações.

### Como o SQL funciona?

O usuário escreve comandos SQL que são enviados ao SGBD. Este processa a consulta, decide o plano de execução ideal, acessa os dados físicos, realiza as operações solicitadas e retorna os resultados.

A linguagem é declarativa, ou seja, o usuário diz o que quer ("selecionar clientes maiores de 30 anos") e o banco determina como fazer isso internamente. O SQL permite consultar diversas tabelas relacionadas, fazer agregações, ordenar dados, filtrar por condições, etc.

### Sistemas que suportam SQL

Existem muitos SGBDs que implementam SQL, como MySQL, PostgreSQL, Microsoft SQL Server, Oracle, MariaDB, SQLite, entre outros. Embora o núcleo do SQL seja padrão, cada sistema pode ter suas extensões específicas.

SQL é a linguagem universal para lidar com bancos de dados relacionais, permitindo armazenar, manipular, consultar e administrar dados estruturados. Seu domínio é essencial para desenvolvedores, analistas de dados, administradores de banco de dados e qualquer profissional que trabalhe com dados.

SQL simplifica a transformação de dados brutos em informações úteis para decisão, análise e operação de sistemas modernos.

**Exercícios de fixação:**

1. Classifique cada comando como DDL, DML ou DQL: `ALTER TABLE`, `INSERT INTO`, `SELECT`, `DROP TABLE`, `UPDATE`.

   <details><summary>Ver resposta</summary>

   DDL: `ALTER TABLE`, `DROP TABLE` — DML: `INSERT INTO`, `UPDATE` — DQL: `SELECT`

   </details>

2. Veja os exemplos completos de [DDL](/NBD/ddl.md), [DML](/NBD/dml.md) e [DQL](/NBD/dql.md) e execute pelo menos uma consulta de cada tipo em um banco de testes.

## Entidade-Relacionamento (ER Model)

Desenvolvido por Peter Chen em 1976, o ER Model é uma ferramenta de modelagem conceitual.

- **Componentes Expandidos**:
  - **Entidades**: Fortes (independentes) vs. Fracas (dependem de outra).
  - **Atributos**: Simples (atomic), Compostos (ex.: Endereço com Rua+Cidade), Multivalorados (ex.: Telefones), Derivados (ex.: Idade de DataNasc).
  - **Relacionamentos**: Cardinalidade (1:1, 1:N, N:N), Participação (total/parcial). Ex.: N:N resolvido com tabela intermediária.

- **Diagrama Textual Exemplo**:
  ```
  [Cliente] --1:N-- [Pedido] --N:1-- [Produto]
  Atributos: Cliente (ID PK, Nome), Pedido (ID PK, Data, ClienteID FK)
  ```

- **Conversão para Relacional**: Entidades viram tabelas, atributos viram colunas, e relacionamentos viram chaves estrangeiras (1:N) ou uma tabela de junção (N:N). Aplicando isso ao diagrama acima:

  ```sql
  CREATE TABLE Cliente (
    ID INT AUTO_INCREMENT PRIMARY KEY,
    Nome VARCHAR(100) NOT NULL
  );

  CREATE TABLE Pedido (
    ID INT AUTO_INCREMENT PRIMARY KEY,
    Data DATE NOT NULL,
    ClienteID INT NOT NULL,
    FOREIGN KEY (ClienteID) REFERENCES Cliente(ID)
  );
  ```

  Note que o "1:N" do diagrama virou, na prática, a `FOREIGN KEY (ClienteID)` dentro de `Pedido` — o mesmo padrão visto na seção de [Chaves Estrangeiras](#chaves-estrangeiras-foreign-keys-conexões-entre-tabelas).

- **Ferramentas**: Lucidchart, ERDPlus para diagramas.

- **Importância**: Previne erros de design, facilitando comunicação entre stakeholders.

**Exercícios de fixação:**

1. Modele um mini sistema de "Biblioteca" com as entidades Livro, Autor e Empréstimo. Quais são as cardinalidades entre elas?
2. Como um relacionamento N:N entre Aluno e Curso é representado quando convertido para o modelo relacional?

## Normalização

Processo para eliminar redundância e anomalias (inserção, atualização, exclusão).

- **Formas Normais Detalhadas**:
  - **1NF**: Valores atômicos, sem grupos repetidos. Ex.: Separe "Hobbies: ler, nadar" em linhas.
  - **2NF**: 1NF + sem dependências parciais (atributos dependem da PK completa em chaves compostas).
  - **3NF**: 2NF + sem dependências transitivas (ex.: Cidade depende de CEP, não de Empregado).
  - **BCNF**: Toda dependência funcional é de superchave.
  - **4NF/5NF**: Para multivalorados e joins.

- **Exemplo Passo a Passo**: Considere esta tabela não normalizada:

  | PedidoID | Cliente | Produtos                | CidadeCliente | CEP    |
  |----------|---------|--------------------------|---------------|--------|
  | 1        | João    | Caneta, Caderno          | São Paulo     | 01000  |

  1. **1NF** (valores atômicos, sem listas dentro de uma célula): separe "Produtos" em uma linha por produto, criando uma tabela `Pedido_Item(PedidoID, Produto)`.
  2. **2NF** (sem dependências parciais): se a chave fosse composta (`PedidoID + Produto`) e "Cliente" dependesse só de `PedidoID` — não do par completo —, mova "Cliente" para sua própria tabela: `Pedido(PedidoID, ClienteID)`.
  3. **3NF** (sem dependências transitivas): "CidadeCliente" depende do "CEP", que depende do cliente — não do pedido. Ou seja, `Cidade` depende de `PedidoID` só indiretamente, através de `CEP`. Mova esses dados para `Cliente(ClienteID, Nome, CEP, Cidade)`.

  Resultado: três tabelas menores (`Cliente`, `Pedido`, `Pedido_Item`) ligadas por chaves estrangeiras, sem repetir "São Paulo" a cada pedido do mesmo cliente.

- **Denormalização**: Reintroduz redundância para performance (ex.: Armazene total calculado).

- **Importância**: Bancos normalizados são eficientes em espaço e consistentes, mas equilibre com performance.

**Exercícios de fixação:**

1. Dada uma tabela `Pedido(ID, Cliente, Produto1, Produto2, Produto3)`, explique por que ela viola a 1NF e como corrigi-la.
2. Dê um exemplo de dependência transitiva que viola a 3NF.

## Índices: Aceleradores de Consultas

Índices são estruturas de dados auxiliares que melhoram a velocidade de recuperação de dados, semelhantes a um índice remissivo em um livro. Em vez de escanear toda a tabela (full table scan), o DBMS usa o índice para localizar registros rapidamente. Eles são criados em colunas frequentemente usadas em WHERE, JOIN ou ORDER BY.

- **Características Detalhadas**:
  - **Estruturas Internas**: B-Tree (para ranges, ex.: >, <), Hash (para igualdades exatas), Bitmap (para colunas de baixa cardinalidade, ex.: gênero M/F).
  - **Tipos**: Primário (automático na PK, clusterizado, ordena os dados fisicamente), Secundário (não único, non-clusterizado, aponta para os dados), Único/Composto (para constraints ou múltiplas colunas), Full-Text (para buscas textuais, ex.: `LIKE '%termo%'`).
  - **Custo**: Consomem espaço em disco e tempo em inserts/updates/deletes (índice deve ser atualizado).

- **Criação e Uso em SQL**:
  - Simples: `CREATE INDEX idx_nome ON Clientes(Nome);`
  - Único: `CREATE UNIQUE INDEX idx_email ON Clientes(Email);`
  - Composto: `CREATE INDEX idx_composto ON Pedidos(Cliente_ID, Data);`
  - Analisar: `EXPLAIN SELECT * FROM Clientes WHERE Nome = 'João';` (mostra se o índice é usado).
  - Remover: `DROP INDEX idx_nome ON Clientes;`

- **Exemplos Práticos**:
  - **Analogia**: Em um catálogo telefônico, o índice por nome permite achar números rapidamente, sem ler página por página.
  - **Uso Real**: Em uma tabela de logs com milhões de entradas, índice em "Data" acelera `SELECT WHERE Data BETWEEN '2024-01-01' AND '2024-12-31';`. Sem índice, essa mesma busca em 1 milhão de linhas seria lenta; com índice, quase instantânea.

- **Vantagens dos Índices**:
  - **Desempenho**: Reduz tempo de query de O(n) para O(log n).
  - **Ordenação**: Acelera ORDER BY e GROUP BY.
  - **Unicidade**: Úteis para constraints além da PK.
  - **Cobertura**: Índices covering incluem colunas selecionadas, evitando acesso à tabela.

- **Desvantagens e Considerações**:
  - **Custo de Manutenção**: Atualizações reescrevem o índice, consumindo I/O; evite em tabelas de alta escrita.
  - **Espaço**: Pode dobrar o tamanho do banco; monitore com ferramentas como pg_indexes_size no PostgreSQL.
  - **Sobrecarga**: Muitos índices ralentizam inserts; use apenas em colunas com alta seletividade (muitos valores únicos).
  - **Limitações**: Inúteis em colunas de baixa cardinalidade (ex.: booleano); em NoSQL, índices são semelhantes mas gerenciados diferentemente.

- **Por Que São Importantes?** Sem índices, consultas em bancos grandes seriam impraticáveis, levando a lentidão inaceitável em aplicações reais. São críticos para queries em produção — monitore sempre com `EXPLAIN`.

**Exercícios de fixação:**

1. Por que criar um índice em toda coluna de uma tabela pode ser uma má ideia?
2. Em qual situação um índice Full-Text seria mais útil que um índice B-Tree comum?

## Propriedades ACID

Garantem confiabilidade em transações — blocos de comandos SQL que devem ser tratados como uma única unidade indivisível.

- **Atomicidade**: A transação é "tudo ou nada". Se qualquer comando falhar no meio do caminho, o banco desfaz (rollback) tudo o que já havia sido feito, usando os logs de transação.
- **Consistência**: Antes e depois da transação, os dados devem respeitar todas as regras do banco (constraints, chaves, triggers) — uma transação nunca pode deixar os dados num estado inválido.
- **Isolamento**: Transações executando ao mesmo tempo não devem enxergar resultados parciais umas das outras. Níveis de isolamento (ex.: Read Committed) controlam o quanto uma transação pode ver do trabalho ainda não confirmado de outra, evitando *phantom reads* (quando a mesma consulta, repetida dentro da transação, retorna linhas diferentes porque outra transação inseriu dados no meio do caminho).
- **Durabilidade**: Depois do `COMMIT`, a mudança sobrevive mesmo a uma queda de energia — garantido pelo Write-Ahead Logging (WAL), que grava a mudança em um log em disco antes de confirmar a transação.

- **Exemplo em SQL**: Uma transferência de R$100 da conta A para a conta B:

  ```sql
  START TRANSACTION;
  UPDATE Contas SET Saldo = Saldo - 100 WHERE ID = 'A';
  UPDATE Contas SET Saldo = Saldo + 100 WHERE ID = 'B';
  COMMIT;
  ```

  Se o servidor cair depois do primeiro `UPDATE` mas antes do `COMMIT`, a atomicidade garante que o débito é desfeito automaticamente — a conta A nunca fica debitada sem que a conta B tenha recebido o valor.

- **Importância**: Essencial para sistemas críticos como bancos, onde perder ou duplicar uma transação tem custo real.

**Exercícios de fixação:**

1. Dê um exemplo (diferente do caixa eletrônico do texto) do que aconteceria se a propriedade de Atomicidade não existisse.
2. Qual a diferença prática entre Isolamento e Consistência?

## Transações

Uma transação é uma unidade lógica de trabalho: um conjunto de comandos SQL que só faz sentido se executado por completo (ver [Propriedades ACID](#propriedades-acid) acima).

- **Estados**: Active (em execução) → Partially Committed (comandos terminaram, aguardando confirmação) → Committed (confirmada e durável) — ou, em caso de erro, Failed → Aborted (desfeita).
- **Controle com SAVEPOINT**: Permite desfazer só uma parte da transação, sem cancelar tudo:

  ```sql
  START TRANSACTION;
  UPDATE Estoque SET Quantidade = Quantidade - 1 WHERE Produto = 'Caneta';
  SAVEPOINT depois_estoque;
  UPDATE Contas SET Saldo = Saldo - 5 WHERE Cliente = 'João';
  -- Se o pagamento falhar, desfaz só o pagamento e mantém a baixa no estoque:
  ROLLBACK TO depois_estoque;
  COMMIT;
  ```

- **Concorrência e "lost update"**: Imagine duas pessoas comprando o último item do estoque ao mesmo tempo. Se ambas leem "Quantidade = 1" antes de qualquer uma escrever, as duas podem decrementar para 0 — e o sistema deixa passar duas vendas de um item que só existia um. O DBMS evita isso com locks (uma transação bloqueia a linha até terminar) ou MVCC (visto na seção de [DBMS](#sistemas-de-gerenciamento-de-bancos-de-dados-dbms)).
- **Transações distribuídas**: Quando uma transação envolve mais de um banco (ex.: debitar em um servidor e creditar em outro), usa-se 2PC (Two-Phase Commit): primeiro todos os bancos confirmam que *conseguem* aplicar a mudança (fase de preparação); só depois, se todos concordarem, a mudança é efetivada em todos ao mesmo tempo (fase de commit).

- **Importância**: Mantém a integridade dos dados em ambientes com múltiplos usuários e processos simultâneos.

## Segurança em Bancos de Dados

Protege contra ameaças internas/externas.

- **Medidas Detalhadas**:
  - **Autenticação**: Senhas, MFA, certificados.
  - **Autorização**: RBAC (Role-Based Access Control) — em vez de conceder permissões a cada usuário individualmente, você cria papéis (ex.: "vendedor", "gerente") com um conjunto fixo de permissões e atribui os usuários a esses papéis.
  - **Criptografia**: AES para dados, TLS para conexões.
  - **Auditoria**: Logs de queries para compliance.
  - **Defesas**: Contra SQL Injection (use parametros), DDoS (firewalls).

- **Exemplo**: `PREPARE stmt FROM 'SELECT * FROM Users WHERE ID = ?';` previne injeções.

- **Importância**: Com leis como LGPD/GDPR, violações custam milhões.

**Exercícios de fixação:**

1. Por que usar uma query parametrizada (como `PREPARE stmt FROM 'SELECT * FROM Users WHERE ID = ?'`) previne SQL Injection, enquanto concatenar strings diretamente na query não?
2. O que é RBAC e por que é preferível a dar acesso de administrador para todos os usuários?

## Big Data e Bancos Distribuídos

Big Data se refere a volumes de dados grandes (ou rápidos) demais para um único servidor tradicional processar — resumido nos "3Vs": Volume (quantidade), Variedade (formatos diferentes) e Velocidade (chegam em tempo real).

- **Tecnologias**:
  - **Hadoop**: distribui o armazenamento (HDFS — o dado é dividido e espalhado por vários servidores) e o processamento (MapReduce — divide um cálculo grande em tarefas menores, roda em paralelo em cada servidor e depois combina os resultados).
  - **Spark**: faz algo parecido com o MapReduce, mas processa em memória em vez de gravar resultados intermediários em disco a cada etapa — muito mais rápido para cálculos iterativos.
  - **Kafka**: uma fila de mensagens de alto volume, usada para capturar eventos em tempo real (ex.: cada clique em um site) antes de eles serem processados.

- **Técnicas**:
  - **Sharding**: divide uma tabela grande em pedaços menores ("shards"), cada um armazenado em um servidor diferente, para que nenhum servidor precise guardar os dados inteiros.
  - **Replicação master-slave**: mantém cópias dos mesmos dados em vários servidores; o "master" recebe as escritas e as replica para os "slaves", que atendem às leituras.
  - **CAP Theorem**: em um sistema distribuído só é possível garantir 2 das 3 propriedades ao mesmo tempo — Consistência (todos os nós veem o mesmo dado), Disponibilidade (o sistema sempre responde) e Tolerância a Partição (continua funcionando mesmo se a rede entre servidores cair). Como partições de rede acontecem na prática, a escolha real é entre Consistência e Disponibilidade durante uma falha.

- **Exemplos**: Elasticsearch para busca full-text em grandes volumes de texto, BigTable no Google para bilhões de linhas.

- **Importância**: Essencial para sistemas de IA/ML, que dependem de treinar modelos com dados massivos.

## Backup e Recuperação

Estratégias para garantir que o banco sobreviva a falhas de hardware, erros humanos ou ataques.

- **Tipos de backup**:
  - **Full**: cópia completa do banco. Mais simples de restaurar, mas mais lento de gerar e mais pesado de armazenar.
  - **Differential**: guarda só o que mudou desde o último full. Restaurar exige o full + o differential mais recente.
  - **Incremental**: guarda só o que mudou desde o último backup (full ou incremental). Mais rápido de gerar, mas restaurar exige aplicar vários incrementos em sequência.

- **Métricas que orientam a estratégia**:
  - **RPO (Recovery Point Objective)**: quanto dado a empresa aceita perder. Um RPO de 1 hora exige backups pelo menos a cada hora.
  - **RTO (Recovery Time Objective)**: quanto tempo o sistema pode ficar fora do ar até ser restaurado. Um RTO de 30 minutos exige um processo de restore rápido e já testado, não só um backup guardado.

- **Comandos práticos**:

  ```bash
  # Backup completo em MySQL
  mysqldump -u root -p meu_banco > backup_2026-07-29.sql

  # Restaurar a partir do backup
  mysql -u root -p meu_banco < backup_2026-07-29.sql
  ```

- **Planejamento**: Um backup só vale algo se o restore já foi testado antes da emergência real; guarde cópias fora do local principal (offsite) como parte do plano de Disaster Recovery (DR).

- **Importância**: Previne perda irreversível de dados — a única coisa pior que não ter backup é descobrir, na hora da crise, que o backup nunca funcionou.

## Como Tudo Se Conecta

Agora que você viu cada peça separadamente, vale a pena juntar tudo:

- **Tabelas e Chaves**: PKs são definidas nas tabelas para garantir unicidade, enquanto FKs conectam tabelas, formando o modelo relacional.
- **Chaves e Índices**: PKs e FKs geralmente têm índices automáticos; índices adicionais otimizam consultas envolvendo chaves.
- **Modelo ER e Tabelas**: No ER Model, entidades viram tabelas com PKs, relacionamentos viram FKs, e colunas frequentes ganham índices.
- **Normalização e Chaves**: A normalização usa PKs e FKs para eliminar redundância, dividindo dados em tabelas menores e ligadas entre si.
- **SQL Amarra Tudo**: DDL cria tabelas, chaves e índices; DML e DQL manipulam e consultam os dados; ACID garante que essas operações sejam confiáveis mesmo com múltiplos usuários simultâneos.
- **Boas Práticas**: Sempre defina PKs; use FKs para integridade; crie índices baseados em queries reais (use `EXPLAIN`); normalize para evitar redundância, mas denormalize se performance for crítica.

## Exemplos Completos

Projetos práticos para ver os conceitos acima em código real:

| Exemplo | O que mostra |
| :-- | :-- |
| [MySQL Connector](/NBD/Mysqlconnector/) | Conexão direta ao MySQL a partir do Python com `mysql-connector`, escrevendo SQL "puro" (sem ORM). |
| [Alchemy ORM](/NBD/SqlAlchemy/) | As mesmas operações, mas usando SQLAlchemy (ORM) — compare com o exemplo anterior para ver a diferença entre escrever SQL manualmente e mapear tabelas para classes Python. |
| [db_pedidos.sql](/NBD/Mysqlconnector/db_pedidos.sql) | Script SQL completo de criação de um banco de pedidos, útil para praticar DDL, PK e FK vistos acima. |
