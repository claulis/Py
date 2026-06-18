# Polimorfismo em Python

## O problema que o polimorfismo resolve

Imagine um sistema que precisa enviar notificações. Você tem três tipos: e-mail, SMS e push notification.

**Sem polimorfismo**, o código que envia ficaria assim:

```python
def enviar_notificacao(tipo, destinatario, mensagem):
    if tipo == "email":
        print(f"Enviando e-mail para {destinatario}: {mensagem}")
    elif tipo == "sms":
        print(f"Enviando SMS para {destinatario}: {mensagem}")
    elif tipo == "push":
        print(f"Enviando push para {destinatario}: {mensagem}")
    # E se vier um novo tipo? Mexer nessa função de novo...
```

Toda vez que um novo tipo de notificação surgir, você precisa abrir e modificar essa função. É arriscado, é repetitivo, e viola um princípio básico: código que funciona não deveria precisar ser reescrito.

**Com polimorfismo**, cada tipo sabe como se enviar:

```python
def enviar_notificacao(notificacao):
    notificacao.enviar()  # cada objeto sabe o que fazer
```

Isso funciona com qualquer tipo de notificação — presente ou futuro — sem alterar a função.

---

## Duck Typing

Python é uma linguagem de **duck typing**: se um objeto tem o método que você precisa, não importa de qual classe ele veio.

> "Se ele anda como um pato e grasna como um pato, então é um pato."

Na prática: se o objeto tem o método `enviar()`, a função pode usá-lo — não importa se é `Email`, `SMS` ou `Push`.

```python
class Email:
    def __init__(self, destinatario, mensagem):
        self.destinatario = destinatario
        self.mensagem = mensagem

    def enviar(self):
        print(f"[EMAIL] Para: {self.destinatario} | Mensagem: {self.mensagem}")

class SMS:
    def __init__(self, destinatario, mensagem):
        self.destinatario = destinatario
        self.mensagem = mensagem

    def enviar(self):
        print(f"[SMS] Para: {self.destinatario} | Mensagem: {self.mensagem}")

class Push:
    def __init__(self, destinatario, mensagem):
        self.destinatario = destinatario
        self.mensagem = mensagem

    def enviar(self):
        print(f"[PUSH] Para: {self.destinatario} | Mensagem: {self.mensagem}")


def enviar_notificacao(notificacao):
    notificacao.enviar()


notificacoes = [
    Email("ana@email.com", "Sua senha foi alterada."),
    SMS("5561999999999", "Seu pedido foi enviado."),
    Push("token_abc123", "Você tem uma nova mensagem."),
]

for n in notificacoes:
    enviar_notificacao(n)
```

**Saída:**
```
[EMAIL] Para: ana@email.com | Mensagem: Sua senha foi alterada.
[SMS] Para: 5561999999999 | Mensagem: Seu pedido foi enviado.
[PUSH] Para: token_abc123 | Mensagem: Você tem uma nova mensagem.
```

`enviar_notificacao` não sabe nem se importa com o tipo. Ela só chama `enviar()`. Polimorfismo em ação.

---

## Polimorfismo com herança

Quando classes compartilham uma superclasse, o polimorfismo fica ainda mais explícito: objetos de tipos diferentes são tratados de forma uniforme por código que conhece apenas a superclasse.

```python
class Animal:
    def __init__(self, nome):
        self.nome = nome

    def fazer_som(self):
        print(f"{self.nome} faz um som genérico.")


class Cachorro(Animal):
    def fazer_som(self):
        print(f"{self.nome} diz: Au au!")


class Gato(Animal):
    def fazer_som(self):
        print(f"{self.nome} diz: Miau!")


class Papagaio(Animal):
    def __init__(self, nome, frase):
        super().__init__(nome)
        self.frase = frase

    def fazer_som(self):
        print(f"{self.nome} diz: {self.frase}")


animais = [
    Cachorro("Rex"),
    Gato("Mimi"),
    Papagaio("Louro", "Quero biscoito!"),
]

for animal in animais:
    animal.fazer_som()
```

**Saída:**
```
Rex diz: Au au!
Mimi diz: Miau!
Louro diz: Quero biscoito!
```

A lista `animais` pode conter qualquer subclasse de `Animal`. O loop não precisa saber qual é qual.

---

## Classes Abstratas: garantindo o contrato

Duck typing é flexível, mas tem um risco: se uma classe esquecer de implementar o método `enviar()`, o erro só aparece quando o código tentar chamar o método — o que pode ser tarde demais.

**Classes abstratas** resolvem isso: elas **obrigam** as subclasses a implementar determinados métodos, verificando isso no momento em que o objeto é criado.

```python
from abc import ABC, abstractmethod

class Notificacao(ABC):
    """
    Classe abstrata — define o contrato que todas as notificações devem seguir.
    Não pode ser instanciada diretamente.
    """
    def __init__(self, destinatario, mensagem):
        self.destinatario = destinatario
        self.mensagem = mensagem

    @abstractmethod
    def enviar(self):
        """Toda subclasse DEVE implementar este método."""
        pass
```

**Tentando instanciar diretamente:**
```python
n = Notificacao("alguem@email.com", "teste")
```

**Saída do erro:**
```
TypeError: Can't instantiate abstract class Notificacao with abstract method enviar
```

Python impede a criação do objeto — exatamente o que queremos.

**Subclasse que esquece de implementar:**
```python
class WhatsApp(Notificacao):
    pass  # esqueceu de implementar enviar()

msg = WhatsApp("5561999999999", "Olá!")
```

**Saída do erro:**
```
TypeError: Can't instantiate abstract class WhatsApp with abstract method enviar
```

O erro aparece na hora certa — quando o objeto é criado — não em algum momento aleatório depois.

**Subclasse implementada corretamente:**
```python
class WhatsApp(Notificacao):
    def enviar(self):
        print(f"[WHATSAPP] Para: {self.destinatario} | Mensagem: {self.mensagem}")

msg = WhatsApp("5561999999999", "Olá!")
msg.enviar()
# Saída: [WHATSAPP] Para: 5561999999999 | Mensagem: Olá!
```

---

## Classes abstratas vs Duck typing: quando usar cada um

| Situação | Abordagem recomendada |
|---|---|
| Classes não relacionadas que têm o mesmo método | Duck typing |
| Família de classes com contrato obrigatório | Classe abstrata |
| Você controla as classes que serão usadas | Classe abstrata |
| Você recebe objetos de fontes externas | Duck typing |

Duck typing é mais flexível. Classes abstratas são mais seguras. Na prática, use classes abstratas quando estiver definindo uma hierarquia e quiser garantir que todas as subclasses implementem os métodos essenciais.

---

## Exemplo completo: sistema de pagamento

```python
from abc import ABC, abstractmethod

class MetodoPagamento(ABC):
    """Contrato para todos os métodos de pagamento."""

    @abstractmethod
    def processar(self, valor):
        pass

    @abstractmethod
    def confirmar(self):
        pass


class CartaoCredito(MetodoPagamento):
    def __init__(self, ultimos_digitos):
        self.ultimos_digitos = ultimos_digitos

    def processar(self, valor):
        print(f"Processando R$ {valor:.2f} no cartão ****{self.ultimos_digitos}")

    def confirmar(self):
        print("Pagamento com cartão confirmado.")


class Pix(MetodoPagamento):
    def __init__(self, chave):
        self.chave = chave

    def processar(self, valor):
        print(f"Transferindo R$ {valor:.2f} via Pix para {self.chave}")

    def confirmar(self):
        print("Transferência Pix confirmada instantaneamente.")


class Boleto(MetodoPagamento):
    def __init__(self, vencimento):
        self.vencimento = vencimento

    def processar(self, valor):
        print(f"Gerando boleto de R$ {valor:.2f} com vencimento em {self.vencimento}")

    def confirmar(self):
        print("Aguardando compensação do boleto (até 3 dias úteis).")


def realizar_pagamento(metodo, valor):
    """Funciona com qualquer MetodoPagamento."""
    metodo.processar(valor)
    metodo.confirmar()


# Qualquer método funciona com a mesma função:
realizar_pagamento(CartaoCredito("1234"), 250.00)
print()
realizar_pagamento(Pix("ana@email.com"), 89.90)
print()
realizar_pagamento(Boleto("2025-08-10"), 150.00)
```

**Saída:**
```
Processando R$ 250.00 no cartão ****1234
Pagamento com cartão confirmado.

Transferindo R$ 89.90 via Pix para ana@email.com
Transferência Pix confirmada instantaneamente.

Gerando boleto de R$ 150.00 com vencimento em 2025-08-10
Aguardando compensação do boleto (até 3 dias úteis).
```

---

## Exercícios

### Exercício 1 — Sistema de relatórios

Crie uma classe abstrata `Relatorio` com os métodos abstratos `gerar()` e `exportar()`.

Implemente três subclasses:
- `RelatorioPDF` — gera e exporta para PDF (simule com print)
- `RelatorioExcel` — gera e exporta para Excel
- `RelatorioHTML` — gera e exporta para HTML

**Teste esperado:**
```python
relatorios = [RelatorioPDF("frequencia"), RelatorioExcel("notas"), RelatorioHTML("turmas")]

for r in relatorios:
    r.gerar()
    r.exportar()
    print()
```

---

### Exercício 2 — Formas geométricas

Crie uma classe abstrata `Forma` com método abstrato `calcular_area()`.

Implemente:
- `Circulo(raio)` — área: π × r²
- `Retangulo(largura, altura)` — área: largura × altura
- `Triangulo(base, altura)` — área: (base × altura) / 2

**Teste esperado:**
```python
formas = [Circulo(5), Retangulo(4, 6), Triangulo(3, 8)]

for forma in formas:
    print(f"{type(forma).__name__}: área = {forma.calcular_area():.2f}")
```

**Saída esperada:**
```
Circulo: área = 78.54
Retangulo: área = 24.00
Triangulo: área = 12.00
```

---

### Exercício 3 — Sistema de frequência com polimorfismo

Estendendo o sistema dos módulos anteriores: crie uma classe abstrata `RegistroFrequencia` com métodos abstratos `registrar(aluno, data)` e `relatorio()`.

Implemente:
- `RegistroManual` — registra presenças manualmente (como já fazemos)
- `RegistroAutomatico` — simula um registro que aceita todos os alunos da turma automaticamente

---
