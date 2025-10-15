# O que é uma API REST?

Uma **API REST** (Application Programming Interface Representational State Transfer) é um conjunto de regras e ferramentas que permite que diferentes sistemas ou aplicações se comuniquem entre si pela internet de maneira padronizada, eficiente e escalável. Ela é baseada nos princípios do estilo arquitetural **REST**, proposto por Roy Fielding em 2000, que utiliza os protocolos e métodos padrão da web, como o HTTP, para facilitar a troca de dados.

Pense em uma API REST como um "garçom" em um restaurante: você (o cliente) faz um pedido (uma solicitação), o garçom leva o pedido à cozinha (o servidor), e a cozinha retorna a comida (os dados) por meio do garçom. A API REST é o intermediário que facilita essa comunicação entre um cliente (como um aplicativo ou site) e um servidor (onde os dados estão armazenados).

Exemplo completo [aqui](/IWS/rest/README.md)

## Princípios fundamentais do REST

O REST é baseado em alguns princípios-chave que garantem sua simplicidade e eficiência:

1. **Arquitetura Cliente-Servidor**: A API REST separa o cliente (que faz a solicitação) do servidor (que armazena ou processa os dados). Isso permite que ambos evoluam independentemente.

2. **Sem Estado (Stateless)**: Cada solicitação do cliente ao servidor deve conter todas as informações necessárias para ser processada. O servidor não armazena informações sobre solicitações anteriores, o que simplifica a escalabilidade.

3. **Cache**: As respostas do servidor podem ser armazenadas em cache no cliente, reduzindo a carga no servidor e melhorando o desempenho.

4. **Interface Uniforme**: O REST define um conjunto de convenções para a interação, como o uso de URLs para identificar recursos, métodos HTTP (GET, POST, PUT, DELETE, etc.) para ações específicas, e formatos de dados padronizados (como JSON ou XML).

5. **Sistema em Camadas**: A arquitetura pode incluir camadas intermediárias (como proxies ou balanceadores de carga) sem que o cliente precise saber como o sistema está estruturado.

6. **Código Sob Demanda (opcional)**: Em alguns casos, o servidor pode enviar código executável (como scripts) para o cliente, mas isso é menos comum.

## Como funciona uma API REST?

Uma API REST funciona utilizando os padrões da web, especialmente o protocolo **HTTP**. Aqui está o processo básico:

1. **Recursos**: Tudo em uma API REST é tratado como um **recurso** (por exemplo, um usuário, um produto, um pedido). Cada recurso é identificado por uma **URL** única, como `https://api.exemplo.com/usuarios/123`.

2. **Métodos HTTP**: A API usa métodos HTTP para definir ações sobre os recursos:
   - **GET**: Recupera dados de um recurso (ex.: obter informações de um usuário).
   - **POST**: Cria um novo recurso (ex.: adicionar um novo usuário).
   - **PUT** ou **PATCH**: Atualiza um recurso existente (ex.: alterar o nome de um usuário).
   - **DELETE**: Remove um recurso (ex.: excluir um usuário).

3. **Solicitação (Request)**: O cliente envia uma solicitação HTTP ao servidor, especificando:
   - A URL do recurso.
   - O método HTTP (GET, POST, etc.).
   - Cabeçalhos (headers) com informações adicionais, como autenticação ou tipo de conteúdo.
   - (Opcional) Um corpo (body) com dados, como em solicitações POST ou PUT.

   Exemplo de solicitação GET:
   ```
   GET /usuarios/123 HTTP/1.1
   Host: api.exemplo.com
   Accept: application/json
   ```

4. **Resposta (Response)**: O servidor processa a solicitação e retorna uma resposta, que inclui:
   - Um **código de status HTTP** (ex.: 200 para sucesso, 404 para recurso não encontrado, 500 para erro no servidor).
   - Um corpo com os dados solicitados, geralmente em formato **JSON** (ou às vezes XML).
   - Cabeçalhos com metadados, como o tipo de conteúdo ou informações de cache.

   Exemplo de resposta:
   ```json
   HTTP/1.1 200 OK
   Content-Type: application/json

   {
     "id": 123,
     "nome": "João Silva",
     "email": "joao@exemplo.com"
   }
   ```

5. **Formato de Dados**: O JSON é o formato mais comum para troca de dados em APIs REST devido à sua simplicidade e legibilidade. XML ou outros formatos também podem ser usados, mas são menos frequentes.

6. **Autenticação e Segurança**: APIs REST frequentemente requerem autenticação (como tokens JWT, OAuth ou chaves de API) para garantir que apenas usuários autorizados acessem os recursos. Além disso, usam HTTPS para criptografar as comunicações.

## Exemplo Prático

Imagine uma API REST para gerenciar uma livraria online. A API pode ter os seguintes endpoints:

- **GET /livros**: Lista todos os livros.
- **GET /livros/456**: Retorna os detalhes do livro com ID 456.
- **POST /livros**: Cria um novo livro com os dados enviados no corpo da solicitação.
- **PUT /livros/456**: Atualiza as informações do livro com ID 456.
- **DELETE /livros/456**: Exclui o livro com ID 456.

Exemplo de solicitação POST para criar um livro:
```
POST /livros HTTP/1.1
Host: api.livraria.com
Content-Type: application/json
Authorization: Bearer <token>

{
  "titulo": "Dom Casmurro",
  "autor": "Machado de Assis",
  "ano": 1899
}
```

Resposta:
```
HTTP/1.1 201 Created
Content-Type: application/json

{
  "id": 789,
  "titulo": "Dom Casmurro",
  "autor": "Machado de Assis",
  "ano": 1899
}
```

## Vantagens da API REST

- **Escalabilidade**: Por ser stateless, é fácil adicionar servidores para lidar com mais solicitações.
- **Flexibilidade**: Suporta diferentes formatos de dados e pode ser usada por diversos tipos de clientes (web, mobile, IoT).
- **Simplicidade**: Usa padrões da web (HTTP, URLs), o que facilita o desenvolvimento e a integração.
- **Independência**: Clientes e servidores podem ser desenvolvidos em linguagens diferentes, desde que sigam o protocolo HTTP.

## Limitações

- **Latência**: Como cada solicitação é independente, pode haver sobrecarga em sistemas que exigem muitas chamadas.
- **Complexidade em Operações Complexas**: Para operações que envolvem múltiplos recursos, pode ser necessário fazer várias chamadas, o que pode ser menos eficiente que outras abordagens (como GraphQL).
- **Manutenção de Estado**: Como o REST é stateless, o cliente precisa gerenciar o estado, o que pode complicar algumas aplicações.

