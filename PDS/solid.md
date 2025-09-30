# Princípios SOLID

Os princípios SOLID são um conjunto de cinco diretrizes de design de software que promovem a criação de sistemas robustos, escaláveis e fáceis de manter. Eles foram introduzidos por Robert C. Martin e são amplamente utilizados em programação orientada a objetos. Esta documentação explica cada princípio e ilustra sua aplicação com base em um exemplo prático de um sistema de gerenciamento de pedidos em uma loja online, implementado em Python.

Exemplo de Gerenciamento de Pedidos

## 1. Princípio da Responsabilidade Única (SRP): Ccada classe deve ter uma única responsabilidade

```python
class Pedido:
    def __init__(self, id_pedido, itens):
        self.id_pedido = id_pedido
        self.itens = itens

    def calcular_total(self):
        return sum(item.preco for item in self.itens)
```

Classe separada para salvar o pedido, respeitando SRP

```python
class RepositorioPedido:
    def salvar(self, pedido):
        print(f"Salvando pedido {pedido.id_pedido} no banco de dados")
```

## 2. Princípio Aberto/Fechado (OCP): classes devem estar abertas para extensão, mas fechadas para modificação

```python
from abc import ABC, abstractmethod

class ProcessadorPagamento(ABC):
    @abstractmethod
    def processar_pagamento(self, valor):
        pass

class PagamentoCartaoCredito(ProcessadorPagamento):
    def processar_pagamento(self, valor):
        print(f"Processando pagamento de {valor} via cartão de crédito")

class PagamentoPayPal(ProcessadorPagamento):
    def processar_pagamento(self, valor):
        print(f"Processando pagamento de {valor} via PayPal")
```

## 3. Princípio da Substituição de Liskov (LSP): subclasses devem ser substituíveis por suas superclasses sem quebrar o sistema

```python
class Item:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

class ItemFisico(Item):
    def calcular_custo_envio(self):
        return 10.0  # Custo fixo de envio

class ItemDigital(Item):
    def calcular_custo_envio(self):
        return 0.0  # Produtos digitais não têm custo de envio
```

## 4. Princípio da Segregação de Interfaces (ISP): clientes não devem ser forçados a depender de interfaces que não usam

```python
class Imprimivel(ABC):
    @abstractmethod
    def imprimir_fatura(self):
        pass

class Notificavel(ABC):
    @abstractmethod
    def enviar_notificacao(self):
        pass

class ImpressoraPedido(Imprimivel):
    def imprimir_fatura(self):
        print("Imprimindo fatura do pedido")

class NotificadorCliente(Notificavel):
    def enviar_notificacao(self):
        print("Enviando notificação ao cliente")
```

## 5. Princípio da Inversão de Dependência (DIP):módulos de alto nível não devem depender de módulos de baixo nível

```python
class GerenciadorPedidos:
    def __init__(self, processador_pagamento: ProcessadorPagamento, repositorio: RepositorioPedido):
        self.processador_pagamento = processador_pagamento
        self.repositorio = repositorio

    def processar_pedido(self, pedido):
        total = pedido.calcular_total()
        self.processador_pagamento.processar_pagamento(total)
        self.repositorio.salvar(pedido)
```

## 6. Exemplo de uso

```python
if __name__ == "__main__":
    # Criando itens
    livro = ItemFisico("Livro", 50.0)
    ebook = ItemDigital("E-book", 30.0)
    
    # Criando pedido
    pedido = Pedido(1, [livro, ebook])
    
    # Configurando dependências
    processador_pagamento = PagamentoCartaoCredito()
    repositorio = RepositorioPedido()
    impressora = ImpressoraPedido()
    notificador = NotificadorCliente()
    
    # Processando pedido
    gerenciador = GerenciadorPedidos(processador_pagamento, repositorio)
    gerenciador.processar_pedido(pedido)
    
    # Imprimindo e notificando
    impressora.imprimir_fatura()
    notificador.enviar_notificacao()
    
    # Calculando custos de envio
    print(f"Custo de envio do livro: {livro.calcular_custo_envio()}")
    print(f"Custo de envio do e-book: {ebook.calcular_custo_envio()}")
```

## 7. Teoria

1. **Princípio da Responsabilidade Única (SRP)**

O Princípio da Responsabilidade Única (Single Responsibility Principle) estabelece que uma classe deve ter apenas uma razão para mudar, ou seja, deve ter uma única responsabilidade.

>Dividir responsabilidades reduz o acoplamento, facilita a manutenção e melhora a legibilidade do código. Classes com múltiplas responsabilidades tendem a se tornar complexas e difíceis de modificar.

Aplicação no Código
No exemplo, a classe Pedido é responsável apenas por gerenciar os dados do pedido e calcular seu total. A responsabilidade de persistência (salvar o pedido no banco de dados) é delegada à classe RepositorioPedido. Isso garante que, se a lógica de salvamento mudar (por exemplo, mudar de um banco de dados relacional para um NoSQL), apenas a classe RepositorioPedido precisará ser modificada, sem impactar a classe Pedido.

```python
class Pedido:
    def __init__(self, id_pedido, itens):
        self.id_pedido = id_pedido
        self.itens = itens

    def calcular_total(self):
        return sum(item.preco for item in self.itens)

class RepositorioPedido:
    def salvar(self, pedido):
        print(f"Salvando pedido {pedido.id_pedido} no banco de dados")
```

2. **Princípio Aberto/Fechado (OCP)**

O Princípio Aberto/Fechado (Open/Closed Principle) determina que uma classe deve estar aberta para extensão, mas fechada para modificação. Isso significa que novas funcionalidades podem ser adicionadas por meio de extensões, sem alterar o código existente.

>Evitar modificações em classes existentes reduz o risco de introduzir erros em funcionalidades já testadas. Isso também facilita a escalabilidade do sistema.

Aplicação no Código
A classe abstrata ProcessadorPagamento define um contrato para processar pagamentos, permitindo a criação de diferentes métodos de pagamento (como PagamentoCartaoCredito e PagamentoPayPal) sem modificar a classe original. Para adicionar um novo método de pagamento, basta criar uma nova classe que implemente ProcessadorPagamento.

```python
class ProcessadorPagamento(ABC):
    @abstractmethod
    def processar_pagamento(self, valor):
        pass

class PagamentoCartaoCredito(ProcessadorPagamento):
    def processar_pagamento(self, valor):
        print(f"Processando pagamento de {valor} via cartão de crédito")

class PagamentoPayPal(ProcessadorPagamento):
    def processar_pagamento(self, valor):
        print(f"Processando pagamento de {valor} via PayPal")
```

3. **Princípio da Substituição de Liskov (LSP)**

O Princípio da Substituição de Liskov (Liskov Substitution Principle) afirma que uma subclasse deve ser substituível por sua superclasse sem alterar o comportamento do programa.

>Garante que subclasses mantenham a funcionalidade esperada pela superclasse, permitindo maior flexibilidade e reutilização de código.

Aplicação no Código
As classes ItemFisico e ItemDigital herdam de Item e implementam o método calcular_custo_envio de forma consistente. Um ItemFisico tem um custo de envio fixo (10.0), enquanto um ItemDigital tem custo zero. Ambas podem ser usadas em qualquer contexto que espere um Item, sem causar erros.

```python
class Item:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

class ItemFisico(Item):
    def calcular_custo_envio(self):
        return 10.0  # Custo fixo de envio

class ItemDigital(Item):
    def calcular_custo_envio(self):
        return 0.0  # Produtos digitais não têm custo de envio
```

4. **Princípio da Segregação de Interfaces (ISP)**

O Princípio da Segregação de Interfaces (Interface Segregation Principle) estabelece que clientes não devem ser forçados a depender de interfaces que não utilizam.

>Interfaces específicas para cada necessidade reduzem a complexidade e evitam que classes implementem métodos desnecessários, tornando o código mais limpo e modular.

Aplicação no Código
As interfaces Imprimivel e Notificavel são separadas, garantindo que ImpressoraPedido implemente apenas imprimir_fatura e NotificadorCliente implemente apenas enviar_notificacao. Isso evita que classes sejam forçadas a implementar métodos irrelevantes.

```python
class Imprimivel(ABC):
    @abstractmethod
    def imprimir_fatura(self):
        pass

class Notificavel(ABC):
    @abstractmethod
    def enviar_notificacao(self):
        pass

class ImpressoraPedido(Imprimivel):
    def imprimir_fatura(self):
        print("Imprimindo fatura do pedido")

class NotificadorCliente(Notificavel):
    def enviar_notificacao(self):
        print("Enviando notificação ao cliente")
```

5. **Princípio da Inversão de Dependência (DIP)**

O Princípio da Inversão de Dependência (Dependency Inversion Principle) afirma que módulos de alto nível não devem depender de módulos de baixo nível; ambos devem depender de abstrações. Além disso, abstrações não devem depender de detalhes, mas os detalhes devem depender de abstrações.

>Reduz o acoplamento entre módulos, facilitando a substituição de implementações e melhorando a testabilidade e manutenção do código.

Aplicação no Código
A classe GerenciadorPedidos depende das abstrações ProcessadorPagamento e RepositorioPedido, não de suas implementações concretas. Isso permite injetar diferentes processadores de pagamento ou repositórios sem modificar a lógica de GerenciadorPedidos.

```python
class GerenciadorPedidos:
    def __init__(self, processador_pagamento: ProcessadorPagamento, repositorio: RepositorioPedido):
        self.processador_pagamento = processador_pagamento
        self.repositorio = repositorio

    def processar_pedido(self, pedido):
        total = pedido.calcular_total()
        self.processador_pagamento.processar_pagamento(total)
        self.repositorio.salvar(pedido)
```
