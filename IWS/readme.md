# O que é uma API REST?

Uma **API REST** (*Application Programming Interface* — *Representational State Transfer*) é um conjunto de regras e convenções que permite que diferentes sistemas ou aplicações troquem informações entre si pela internet, de forma padronizada, eficiente e escalável. Ela segue os princípios do estilo arquitetural **REST**, proposto por Roy Fielding em sua tese de doutorado em 2000, que reaproveita os protocolos e métodos já existentes na web — principalmente o **HTTP** — para a comunicação entre sistemas.

## Analogia do restaurante

Uma API REST pode ser comparada ao papel de um garçom em um restaurante:

1. O cliente consulta o cardápio (a **documentação da API**) e faz um pedido (uma **requisição**).
2. O garçom (a **API**) leva o pedido até a cozinha (o **servidor**), responsável por processá-lo.
3. A cozinha prepara o prato (**processa os dados**) e o entrega ao garçom.
4. O garçom retorna o prato ao cliente (a **resposta**), já pronto.

O cliente não precisa conhecer o funcionamento interno da cozinha — apenas a forma correta de fazer o pedido (a URL e o método corretos) e o formato do que será recebido de volta. Esse contrato entre cliente e servidor é o que uma API REST formaliza.

Um exemplo completo e funcional, com autenticação, paginação, testes automatizados e banco de dados configurável (SQLite ou MySQL), está documentado em [IWS/rest/README.md](/IWS/rest/README.md).

## Princípios fundamentais do REST

O REST é baseado em seis princípios-chave. Uma API é considerada RESTful quando os segue (o último é opcional):

| # | Princípio | Descrição |
|---|-----------|--------------|
| 1 | **Cliente-Servidor** | Cliente (interface) e servidor (dados/regras de negócio) são independentes e evoluem separadamente. |
| 2 | **Sem Estado (*Stateless*)** | Cada requisição deve conter todas as informações necessárias para ser processada; o servidor não mantém contexto de requisições anteriores. |
| 3 | **Cache** | Respostas podem ser marcadas como cacheáveis, reduzindo processamento redundante. |
| 4 | **Interface Uniforme** | Conjunto consistente de regras: URLs identificam recursos, métodos HTTP definem ações, JSON/XML padroniza os dados. |
| 5 | **Sistema em Camadas** | Podem existir intermediários (proxies, balanceadores de carga, gateways) entre cliente e servidor, de forma transparente. |
| 6 | **Código sob Demanda** *(opcional)* | O servidor pode, eventualmente, enviar código executável ao cliente; pouco utilizado na prática. |

O princípio de maior impacto prático é o **Stateless**: como nenhuma requisição depende de contexto acumulado em requisições anteriores, o servidor pode ser reiniciado ou substituído sem afetar a continuidade das chamadas subsequentes, o que também simplifica a escalabilidade horizontal.

## Estrutura de uma API REST

### 1. Recursos e URLs

Em uma API REST, cada entidade manipulada (usuário, produto, pedido) é tratada como um **recurso**, identificado por uma **URL** única. Exemplo:

```
https://api.exemplo.com/usuarios/123
```

A URL identifica o recurso (o "quê"); o método HTTP define a ação sobre ele (o "como").

### 2. Métodos HTTP

| Método | Ação sobre o recurso | Equivalente em CRUD | Exemplo |
|--------|----------------------|----------------------|---------|
| **GET** | Consulta um recurso | Read | Obter dados de um usuário |
| **POST** | Cria um novo recurso | Create | Cadastrar um novo usuário |
| **PUT** | Substitui um recurso por completo | Update (total) | Reescrever todos os dados de um usuário |
| **PATCH** | Atualiza parte de um recurso | Update (parcial) | Alterar apenas o e-mail de um usuário |
| **DELETE** | Remove um recurso | Delete | Excluir um usuário |

`PUT` requer o objeto completo no corpo da requisição, incluindo campos não alterados; `PATCH` requer apenas os campos a serem modificados.

### 3. Estrutura de uma Requisição (Request)

Uma requisição HTTP é composta por quatro elementos:

- **URL** do recurso;
- **Método** HTTP (GET, POST, etc.);
- **Cabeçalhos (headers)**: metadados como autenticação (`Authorization`, `X-API-Key`) ou tipo de conteúdo (`Content-Type`);
- **Corpo (body)**, opcional: dados enviados, geralmente presentes em requisições `POST`, `PUT` ou `PATCH`.

Exemplo de requisição GET:

```http
GET /usuarios/123 HTTP/1.1
Host: api.exemplo.com
Accept: application/json
```

### 4. Estrutura de uma Resposta (Response)

O servidor processa a requisição e retorna uma resposta composta por três elementos:

- **Código de status HTTP**, indicando o resultado da operação;
- **Corpo**, geralmente em **JSON**, contendo os dados solicitados;
- **Cabeçalhos**, com metadados como o tipo de conteúdo.

Exemplo de resposta:

```http
HTTP/1.1 200 OK
Content-Type: application/json
```

```json
{
  "id": 123,
  "nome": "João Silva",
  "email": "joao@exemplo.com"
}
```

### 5. Códigos de status HTTP mais comuns

A faixa do código já indica a natureza do resultado: `2xx` sucesso, `4xx` erro do cliente, `5xx` erro do servidor.

| Código | Significado | Ocorre em |
|--------|-------------|-----------------|
| `200 OK` | Sucesso | GET, PUT ou PATCH concluídos com sucesso |
| `201 Created` | Recurso criado | POST que criou um novo recurso |
| `204 No Content` | Sucesso sem corpo de resposta | DELETE bem-sucedido |
| `400 Bad Request` | Requisição malformada | Corpo ou parâmetros inválidos |
| `401 Unauthorized` | Ausência de autenticação | Credencial ausente ou inválida |
| `403 Forbidden` | Autenticado, mas sem permissão | Acesso negado a um recurso vedado |
| `404 Not Found` | Recurso inexistente | URL aponta para um ID inexistente |
| `500 Internal Server Error` | Erro inesperado no servidor | Falha não tratada no backend |

### 6. Formato de dados

O **JSON** é o formato predominante em APIs REST, por sua simplicidade e legibilidade. XML também é suportado, porém menos utilizado atualmente.

### 7. Autenticação e segurança

APIs REST geralmente exigem autenticação para restringir o acesso a usuários autorizados e utilizam **HTTPS** para criptografar a comunicação. Mecanismos comuns:

- **Chave de API** (ex.: header `X-API-Key`) — mecanismo mais simples, utilizado no [exemplo prático deste repositório](/IWS/rest/README.md);
- **JWT (JSON Web Token)** — carrega identidade e permissões dentro do próprio token;
- **OAuth** — padrão para delegação de acesso entre sistemas (ex.: autenticação via terceiros).

Os três mecanismos resolvem o mesmo problema — identificação e autorização do solicitante — com níveis distintos de granularidade e complexidade.

## Glossário

| Termo | Significado |
|-------|--------------|
| **Endpoint** | URL específica de um recurso (ex.: `/livros/456`) |
| **Payload** | Conteúdo transmitido no corpo da requisição ou resposta |
| **Header** | Metadado enviado junto da requisição ou resposta (ex.: tipo de conteúdo, autenticação) |
| **Query string** | Parâmetros adicionais na URL, após `?` (ex.: `/livros?ano=1899`) |
| **Path parameter** | Parte variável da URL (ex.: `456` em `/livros/456`) |
| **Idempotência** | Propriedade pela qual repetir a mesma chamada produz o mesmo efeito de executá-la uma única vez; válida para GET, PUT e DELETE, mas não para POST |

## Exemplo Prático

Uma API REST para gerenciamento de uma livraria online pode conter os seguintes endpoints:

| Método | Endpoint | Ação |
|--------|----------|------|
| GET | `/livros` | Lista todos os livros |
| GET | `/livros/456` | Retorna os detalhes do livro com ID 456 |
| POST | `/livros` | Cria um novo livro com os dados enviados no corpo |
| PUT | `/livros/456` | Atualiza (por completo) o livro com ID 456 |
| DELETE | `/livros/456` | Exclui o livro com ID 456 |

Requisição POST para criação de um livro:

```http
POST /livros HTTP/1.1
Host: api.livraria.com
Content-Type: application/json
Authorization: Bearer <token>
```

```json
{
  "titulo": "Dom Casmurro",
  "autor": "Machado de Assis",
  "ano": 1899
}
```

Resposta correspondente — status `201 Created`, indicando a criação do recurso, e campo `id` gerado pelo servidor:

```http
HTTP/1.1 201 Created
Content-Type: application/json
```

```json
{
  "id": 789,
  "titulo": "Dom Casmurro",
  "autor": "Machado de Assis",
  "ano": 1899
}
```

## Vantagens da API REST

- **Escalabilidade**: por ser *stateless*, é possível adicionar servidores adicionais para atender mais solicitações.
- **Flexibilidade**: suporta diferentes formatos de dados e pode ser consumida por diversos tipos de clientes (web, mobile, IoT).
- **Simplicidade**: utiliza padrões já estabelecidos na web (HTTP, URLs), o que reduz a curva de aprendizado e facilita a integração.
- **Independência de tecnologia**: cliente e servidor podem ser implementados em linguagens diferentes, desde que ambos utilizem HTTP.

## Limitações

- **Latência**: como cada requisição é independente, sistemas que dependem de múltiplas chamadas em sequência podem sofrer sobrecarga de rede.
- **Complexidade em operações compostas**: operações que envolvem vários recursos simultaneamente podem exigir múltiplas chamadas — problema que abordagens como GraphQL buscam resolver, permitindo especificar exatamente os dados necessários em uma única chamada.
- **Gestão de estado no cliente**: como o servidor não mantém estado, cabe ao cliente gerenciá-lo (ex.: token de autenticação, controle de paginação).

## Leitura complementar

- [MDN — Métodos HTTP](https://developer.mozilla.org/pt-BR/docs/Web/HTTP/Methods)
- [MDN — Códigos de status HTTP](https://developer.mozilla.org/pt-BR/docs/Web/HTTP/Status)
