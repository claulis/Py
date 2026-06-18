 # Programação Orientada a Objetos

## Por que POO existe?

Imagine que você precisa guardar informações de 30 alunos em um programa. Sem organização, você acabaria com isso:

```python
aluno1_nome = "Ana"
aluno1_matricula = "2023001"
aluno1_presencas = []

aluno2_nome = "Bruno"
aluno2_matricula = "2023002"
aluno2_presencas = []

# ... e assim por diante até o aluno 30
```

Funciona? Tecnicamente sim. É sustentável? Absolutamente não.

A **Programação Orientada a Objetos (POO)** surgiu para resolver exatamente esse tipo de problema: organizar o código em torno de **entidades do mundo real**, agrupando dados e comportamentos relacionados em um só lugar.

Com POO, o mesmo exemplo fica assim:

```python
class Aluno:
    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula
        self.presencas = []

ana = Aluno("Ana", "2023001")
bruno = Aluno("Bruno", "2023002")
```

Muito mais limpo. E você pode criar quantos alunos quiser sem repetir código.

---

## Classe vs Objeto: a analogia da ficha

Pense em uma **ficha de cadastro de aluno em branco**. Ela define quais campos existem: nome, matrícula, data de nascimento. A ficha em branco é a **classe** — é o molde, o modelo.

Agora imagine a ficha preenchida com os dados da Ana. Esse é o **objeto** — uma instância concreta da classe, com valores reais.

| Conceito | Analogia | Em Python |
|---|---|---|
| **Classe** | Ficha em branco | `class Aluno:` |
| **Objeto** | Ficha preenchida | `ana = Aluno("Ana", "2023001")` |

Uma classe pode gerar **muitos objetos diferentes**. Cada objeto tem seus próprios dados, mas todos seguem a mesma estrutura definida pela classe.

---

## Os 4 Pilares da POO

### 1. Abstração

Abstrair significa **focar no que é essencial e ignorar o resto**.

Ao modelar um aluno para um sistema de frequência, você não precisa saber a cor dos olhos dele, o nome da mãe ou o endereço. Você precisa de nome, matrícula e presenças. Isso é abstração: você escolhe quais características do mundo real são relevantes para o seu sistema.

> **Analogia:** Um mapa é uma abstração do mundo real. Ele mostra ruas e prédios, mas ignora as árvores, as calçadas e as nuvens — porque para navegar, essas informações não importam.

### 2. Encapsulamento

Encapsular significa **proteger os dados internos de um objeto**, controlando como eles são acessados e modificados.

Imagine que o saldo de uma conta bancária é um atributo. Se qualquer parte do programa pudesse alterá-lo diretamente, alguém poderia definir o saldo como `-R$9.999` sem passar por nenhuma validação. O encapsulamento evita isso.

> **Analogia:** O painel de controle de um avião tem botões protegidos por tampas. O piloto pode acioná-los, mas somente seguindo um procedimento. Ninguém aperta um botão crítico por acidente.

### 3. Herança

Herança permite que uma classe **reaproveite e especialize** o comportamento de outra.

Se você tem uma classe `Conta` com os atributos `titular` e `saldo`, pode criar `ContaCorrente` e `ContaPoupanca` que herdam esses atributos e adicionam suas próprias características — sem reescrever o que já existe.

> **Analogia:** Um `Carro` e uma `Moto` são ambos `Veículos`. Eles herdam características comuns (têm motor, têm cor, podem acelerar), mas cada um tem particularidades próprias.

### 4. Polimorfismo

Polimorfismo significa **muitas formas**. O mesmo método pode se comportar de maneira diferente dependendo do objeto que o executa.

Se `ContaCorrente` e `ContaPoupanca` têm o método `calcular_rendimento`, cada uma calcula de forma diferente — mas o código que chama esse método não precisa saber qual tipo de conta está usando.

> **Analogia:** O comando "falar" significa coisas diferentes para um `Cachorro` (latir) e um `Gato` (miar). O comando é o mesmo; o comportamento depende de quem está respondendo.

---

## Por que isso importa?

Os 4 pilares não são regras arbitrárias. Eles resolvem problemas reais de desenvolvimento:

| Pilar | Problema que resolve |
|---|---|
| Abstração | Código com informações desnecessárias |
| Encapsulamento | Dados modificados de forma indevida |
| Herança | Código repetido em classes parecidas |
| Polimorfismo | Condicionais (`if/elif`) para tratar tipos diferentes |

---

## Referências

- BOOCH, Grady. *Object-Oriented Analysis and Design with Applications*. Addison-Wesley, 1994.
- KAY, Alan. *The Early History of Smalltalk*. ACM SIGPLAN Notices, 1993.
- MARTIN, Robert C. *Clean Code: A Handbook of Agile Software Craftsmanship*. Prentice Hall, 2008.
- STROUSTRUP, Bjarne. *The C++ Programming Language*. Addison-Wesley, 2000.
