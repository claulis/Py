# Polimorfismo

O polimorfismo é um dos pilares da programação orientada a objetos (POO) e se refere à capacidade de um mesmo nome de método ou operador se comportar de maneiras diferentes, dependendo do objeto ao qual se aplica. A palavra, de origem grega, significa "muitas formas", e no contexto da programação, isso se traduz na habilidade de tratar objetos de diferentes classes de forma uniforme.

## O Princípio do Duck Typing

Em Python, a forma mais comum de polimorfismo é o que se chama de **"duck typing"**. A filosofia por trás desse conceito é simples: "Se ele anda como um pato e quack como um pato, então é um pato". Isso significa que o tipo de um objeto não é tão importante quanto a sua capacidade de responder a um determinado método.

Para ilustrar, considere o seguinte exemplo:

```python
class Carro:
    def mover(self):
        return "O carro se move sobre rodas."

class Aviao:
    def mover(self):
        return "O avião se move no ar."

class Barco:
    def mover(self):
        return "O barco se move na água."

def locomocao(veiculo):
    """
    Esta função aceita qualquer objeto que tenha o método 'mover()'.
    """
    print(veiculo.mover())

# Criando instâncias das classes
meu_carro = Carro()
meu_aviao = Aviao()
meu_barco = Barco()

# Chamando a mesma função com diferentes objetos
locomocao(meu_carro)  # Saída: O carro se move sobre rodas.
locomocao(meu_aviao) # Saída: O avião se move no ar.
locomocao(meu_barco) # Saída: O barco se move na água.
```

Neste exemplo, a função `locomocao` não se preocupa com o tipo de objeto que recebe (`Carro`, `Aviao` ou `Barco`). Ela apenas invoca o método `mover()` no objeto, e o comportamento específico é determinado pela classe do objeto em questão.

## Polimorfismo e Herança

O polimorfismo também se manifesta de forma poderosa através da herança, onde uma subclasse pode **sobrescrever** um método da superclasse para fornecer sua própria implementação. Isso permite que objetos de diferentes classes herdeiras sejam tratados de forma polimorfa.

Considere um exemplo mais formal:

```python
class Animal:
    """
    Classe base que define um método genérico.
    """
    def fazer_som(self):
        raise NotImplementedError("As subclasses devem implementar este método.")

class Cachorro(Animal):
    def fazer_som(self):
        return "Au au!"

class Gato(Animal):
    def fazer_som(self):
        return "Miau!"

# Uma lista que pode conter instâncias de diferentes classes
lista_animais = [Cachorro(), Gato()]

for animal in lista_animais:
    print(animal.fazer_som())
```

Neste cenário, a classe `Animal` estabelece uma interface comum, garantindo que todas as subclasses que herdam dela terão o método `fazer_som()`. Embora os objetos sejam de classes diferentes, eles podem ser iterados e processados uniformemente, evidenciando o polimorfismo.

## Quando usar

O polimorfismo é uma ferramenta poderosa que se aplica em diversos cenários, especialmente quando a flexibilidade, a reutilização de código e a organização de grandes sistemas são prioritárias. O uso de polimorfismo se torna particularmente vantajoso nos seguintes casos:

### 1. Criar APIs e Interfaces Flexíveis

Quando você está desenvolvendo uma biblioteca ou um módulo que será usado por outros desenvolvedores, o polimorfismo permite que você defina uma **interface clara e consistente** sem se prender a tipos de dados específicos.

**Exemplo:** Um sistema de processamento de pagamentos. Você pode ter uma função `processar_pagamento()` que aceita qualquer objeto que implemente um método `realizar_transacao()`. Não importa se é um `PagamentoCartao`, um `PagamentoBoleto` ou um `PagamentoPix`. A função sabe o que fazer com todos eles, tornando seu código mais robusto e fácil de estender para novos métodos de pagamento no futuro.

### 2. Generalizar Comportamentos

Se você tem várias classes que executam uma tarefa semelhante, mas com detalhes de implementação diferentes, o polimorfismo permite que você escreva um código genérico que opera sobre todas elas. Isso elimina a necessidade de usar condicionais (`if/elif/else`) para verificar o tipo de cada objeto.

**Exemplo:** Imagine um software para desenhar formas geométricas. Você pode ter classes como `Circulo`, `Quadrado` e `Triangulo`. Em vez de ter uma função `desenhar_circulo()`, `desenhar_quadrado()`, etc., você pode ter uma única função `desenhar(forma)` que chama o método `desenhar()` de cada objeto.

```python
for forma in lista_de_formas:
    forma.desenhar() # Cada objeto sabe como se desenhar
```

### 3. Evitar o Código Repetitivo

O polimorfismo permite que você trabalhe com coleções de objetos de diferentes classes. Isso é ideal quando você precisa iterar sobre uma lista de objetos e executar uma ação comum em cada um deles.

**Exemplo:** Em um jogo, você pode ter uma lista de inimigos (`Ogre`, `Dragao`, `Slime`). Todos eles podem herdar de uma classe base `Inimigo` com um método `atacar()`. Você pode iterar sobre a lista de inimigos e pedir para cada um deles atacar, sem se preocupar com a lógica de ataque específica de cada tipo de monstro.

```python
for inimigo in lista_de_inimigos:
    inimigo.atacar()
```

### Classes Abstratas

As classes abstratas e as interfaces são conceitos fundamentais na programação orientada a objetos que reforçam o polimorfismo, a herança e a organização do código. Embora Python não tenha uma implementação nativa de interfaces como em linguagens como Java ou C\#, é possível emular esses conceitos usando a biblioteca `abc` (Abstract Base Classes).

Uma **classe abstrata** é uma classe que não pode ser instanciada diretamente. Sua principal finalidade é servir como um modelo para outras classes (subclasses), definindo uma estrutura comum e um conjunto de métodos que as subclasses **devem** implementar.

#### Características

* **Métodos Abstratos:** Uma classe abstrata contém um ou mais **métodos abstratos**. Um método abstrato é um método que é declarado, mas não tem uma implementação.
* **Decoração:** Em Python, você usa o decorador `@abc.abstractmethod` para marcar um método como abstrato. A classe que contém esse método deve herdar de `ABC` (Abstract Base Class).
* **Herança Obrigatória:** Se uma subclasse herda de uma classe abstrata, ela é obrigada a implementar todos os métodos abstratos da classe pai. Se não o fizer, a subclasse também será considerada abstrata e não poderá ser instanciada.

#### Exemplo em Python

```python
from abc import ABC, abstractmethod

class Veiculo(ABC):
    """
    Esta é uma classe abstrata que define um contrato.
    Qualquer subclasse deve implementar o método 'ligar'.
    """
    @abstractmethod
    def ligar(self):
        pass

    def parar(self):
        print("Veículo parado.")

class Carro(Veiculo):
    def ligar(self):
        print("O carro está ligado.")

class Moto(Veiculo):
    def ligar(self):
        print("A moto está ligada.")

# Não é possível instanciar a classe abstrata Veiculo
# veiculo_generico = Veiculo() # Isso geraria um TypeError

meu_carro = Carro()
meu_carro.ligar() # Saída: O carro está ligado.
meu_carro.parar() # Saída: Veículo parado.

minha_moto = Moto()
minha_moto.ligar() # Saída: A moto está ligada.
```

### Interfaces

Uma **interface** é um contrato que define um conjunto de métodos que uma classe deve implementar, mas, ao contrário das classes abstratas, uma interface não pode ter nenhum método implementado. Em linguagens como Java, é um conceito mais rígido.

Em Python, as interfaces são emuladas usando classes abstratas, mas com uma regra: **todos os métodos são abstratos**. A ideia é definir um "esqueleto" de uma classe, garantindo que qualquer classe que "implemente" essa interface terá os métodos necessários.

#### Características (emuladas em Python)

* **Somente Métodos Abstratos:** A "interface" só pode ter métodos abstratos.
* **Sem Atributos de Estado:** Idealmente, interfaces não devem ter variáveis de instância (atributos).
* **Contrato Puro:** Elas servem para garantir que as classes sigam um contrato específico.

#### Exemplo de Interface (emulado em Python)

```python
from abc import ABC, abstractmethod

class Pagavel(ABC):
    """
    Esta é uma 'interface' que define o contrato de um objeto pagável.
    """
    @abstractmethod
    def pagar(self, valor):
        pass

    @abstractmethod
    def verificar_status(self):
        pass

class ContaBancaria(Pagavel):
    def pagar(self, valor):
        print(f"Pagamento de R${valor} realizado pela conta bancária.")

    def verificar_status(self):
        print("Status: Transação concluída.")

class Fatura(Pagavel):
    def pagar(self, valor):
        print(f"Fatura de R${valor} paga com sucesso.")

    def verificar_status(self):
        print("Status: Fatura em dia.")

# As classes ContaBancaria e Fatura são 'Pagavel'
# porque elas implementam os métodos da 'interface'.

def processar_pagamento(objeto_pagavel, valor):
    objeto_pagavel.pagar(valor)
    objeto_pagavel.verificar_status()

minha_conta = ContaBancaria()
minha_fatura = Fatura()

processar_pagamento(minha_conta, 100)
# Saída:
# Pagamento de R$100 realizado pela conta bancária.
# Status: Transação concluída.

print("-" * 20)

processar_pagamento(minha_fatura, 50)
# Saída:
# Fatura de R$50 paga com sucesso.
# Status: Fatura em dia.
```

### Resumo das Diferenças

| Característica | Classe Abstrata | Interface (em Python) |
| :--- | :--- | :--- |
| **Métodos Implementados?** | Sim, pode ter métodos abstratos e concretos. | Não, idealmente todos os métodos são abstratos. |
| **Herança de?** | `ABC` | `ABC` |
| **Finalidade** | Serve como base para classes, fornecendo uma estrutura parcial e definindo métodos obrigatórios. | Define um contrato ou um "protocolo" que as classes devem seguir. |
| **Quando usar?** | Quando você tem uma relação "é um" (ex: `Carro é um Veiculo`) e parte do comportamento pode ser herdado. | Quando você quer garantir que classes diferentes (que podem não ter uma relação de herança direta) tenham um conjunto de métodos em comum (ex: `ContaBancaria` e `Fatura` podem ser `Pagavel`). |

Vamos criar um exemplo mais robusto e interessante para cada um dos conceitos, usando classes abstratas e interfaces.

### Exemplo com Classe Abstrata: Sistema de Notificação

Imagine um sistema que precisa enviar diferentes tipos de notificações (e-mail, SMS, push notification) para os usuários. Embora cada tipo de notificação tenha um método `enviar` que faz algo diferente, a lógica principal do sistema não precisa se preocupar com os detalhes internos. Usamos uma **classe abstrata** para criar um modelo de notificação.

```python
from abc import ABC, abstractmethod

class Notificacao(ABC):
    """
    Classe abstrata que serve como modelo para todos os tipos de notificação.
    Ela garante que toda notificação tem um método 'enviar'.
    """
    def __init__(self, destinatario, mensagem):
        self.destinatario = destinatario
        self.mensagem = mensagem

    @abstractmethod
    def enviar(self):
        """
        Método abstrato que deve ser implementado por cada subclasse.
        """
        pass

class Email(Notificacao):
    def enviar(self):
        print(f"Enviando e-mail para {self.destinatario}: '{self.mensagem}'")

class SMS(Notificacao):
    def enviar(self):
        print(f"Enviando SMS para {self.destinatario}: '{self.mensagem}'")

class Push(Notificacao):
    def enviar(self):
        print(f"Enviando notificação push para {self.destinatario}: '{self.mensagem}'")

def notificar_usuario(notificacao):
    """
    Função polimórfica que aceita qualquer objeto que herde de Notificacao.
    """
    notificacao.enviar()

# Criando objetos de diferentes tipos de notificação
notificacao_email = Email("usuario@email.com", "Sua senha foi alterada.")
notificacao_sms = SMS("5511999999999", "Seu pedido foi enviado.")
notificacao_push = Push("token_do_app", "Você tem uma nova mensagem.")

# Usando a mesma função para enviar diferentes tipos de notificação
notificar_usuario(notificacao_email)
notificar_usuario(notificacao_sms)
notificar_usuario(notificacao_push)
```

Neste exemplo, a classe `Notificacao` define o contrato comum. O código que notifica o usuário (`notificar_usuario`) não precisa saber se está lidando com um e-mail, um SMS ou um push. Ele simplesmente chama o método `enviar`, e o polimorfismo se encarrega de executar o comportamento correto para cada objeto.

-----

### Exemplo com Interface: Sistema de Impressão

Considere um sistema que precisa imprimir diferentes tipos de documentos, como relatórios e planilhas. Embora ambos sejam "imprimíveis", eles não compartilham a mesma classe base; no entanto, eles podem compartilhar um "protocolo" comum. Usamos uma **interface** (emulada com uma classe abstrata) para definir o contrato de "imprimibilidade".

```python
from abc import ABC, abstractmethod

class Imprimivel(ABC):
    """
    Esta é a interface que define o contrato de um objeto imprimível.
    """
    @abstractmethod
    def imprimir(self):
        """
        Método que deve ser implementado por qualquer classe 'Imprimivel'.
        """
        pass

class Relatorio:
    def __init__(self, titulo, conteudo):
        self.titulo = titulo
        self.conteudo = conteudo

    def imprimir(self):
        print(f"--- Relatório: {self.titulo} ---")
        print(self.conteudo)
        print("---------------------------------")

class Planilha:
    def __init__(self, dados):
        self.dados = dados

    def imprimir(self):
        print("--- Planilha ---")
        for linha in self.dados:
            print(" ".join(map(str, linha)))
        print("----------------")

def imprimir_documento(documento):
    """
    Função polimórfica que aceita qualquer objeto 'imprimível'
    (que implemente o método imprimir()).
    """
    documento.imprimir()

# Criando objetos de diferentes tipos que implementam a interface
meu_relatorio = Relatorio("Relatório Anual", "Conteúdo detalhado do relatório...")
minha_planilha = Planilha([[1, 2, 3], [4, 5, 6]])

# Verificando se as classes implementam a interface (opcional, mas didático)
# print(isinstance(meu_relatorio, Imprimivel))
# print(isinstance(minha_planilha, Imprimivel))

imprimir_documento(meu_relatorio)
imprimir_documento(minha_planilha)
```

Neste caso, `Relatorio` e `Planilha` não herdam de uma classe comum, mas ambos **implementam** o método `imprimir`, seguindo o contrato definido pela interface `Imprimivel`. A função `imprimir_documento` pode, então, trabalhar com qualquer um desses objetos de forma polimórfica, sem se preocupar com o tipo exato do objeto.