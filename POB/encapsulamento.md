# Encapsulamento em Python

## O problema que o encapsulamento resolve

Considere o seguinte cenário: você tem uma classe `ContaBancaria` com um atributo `saldo`.

```python
class ContaBancaria:
    def __init__(self, titular, saldo_inicial=0):
        self.titular = titular
        self.saldo = saldo_inicial

conta = ContaBancaria("Ana", 1000)
print(conta.saldo)  # Saída: 1000

# Qualquer parte do programa pode fazer isso:
conta.saldo = -99999
print(conta.saldo)  # Saída: -99999
```

Ninguém impediu o saldo de virar negativo. Não houve nenhum aviso, nenhum erro. O dado foi corrompido silenciosamente.

**Encapsulamento** é o mecanismo que impede isso: você controla como os dados são lidos e modificados, adicionando validações obrigatórias.

---

## Níveis de visibilidade em Python

Python usa convenções de nomenclatura para indicar quem deve acessar um atributo:

| Prefixo | Nome | Uso pretendido |
|---|---|---|
| `nome` | Público | Acesso livre — faz parte da interface da classe |
| `_nome` | Protegido | Sinal para outros desenvolvedores: "use com cuidado, é interno" |
| `__nome` | Privado | Python aplica name mangling — dificulta o acesso externo acidental |

> **Importante:** Em Python, nenhum desses níveis é uma barreira técnica absoluta. A proteção é baseada em **convenção e boas práticas**. A comunidade Python confia que os desenvolvedores respeitam os sinais.

### Atributo público

```python
class Aluno:
    def __init__(self, nome):
        self.nome = nome  # público: acessível e modificável livremente

aluno = Aluno("Ana")
print(aluno.nome)   # Saída: Ana
aluno.nome = "Ana Paula"  # permitido
```

### Atributo protegido (um underscore)

O prefixo `_` é um sinal para outros desenvolvedores: "este atributo é de uso interno, pense duas vezes antes de acessar diretamente".

```python
class ContaBancaria:
    def __init__(self, titular, saldo_inicial=0):
        self.titular = titular
        self._saldo = saldo_inicial  # protegido: convenção de uso interno
    
    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
    
    def obter_saldo(self):
        return self._saldo

conta = ContaBancaria("João", 1000)
conta.depositar(500)
print(conta.obter_saldo())  # Saída: 1500

# Tecnicamente ainda é possível acessar diretamente, mas não é recomendado:
conta._saldo = -500
# ↑ Isso funciona, mas quebra a lógica. O _ avisa: "não faça isso".
```

### Atributo privado (dois underscores)

O prefixo `__` faz com que Python renomeie o atributo internamente, dificultando o acesso acidental de fora da classe.

```python
class ContaBancaria:
    def __init__(self, titular, saldo_inicial=0):
        self.titular = titular
        self.__saldo = saldo_inicial  # privado

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
    
    def obter_saldo(self):
        return self.__saldo

conta = ContaBancaria("Ana", 1500)
print(conta.obter_saldo())  # Saída: 1500

# Tentar acessar diretamente gera um erro real:
print(conta.__saldo)
```

**Saída do erro:**
```
AttributeError: 'ContaBancaria' object has no attribute '__saldo'
```

O atributo existe, mas o acesso direto por fora da classe falha. Isso é intencional — força o uso dos métodos que você definiu.

---

## `@property`: a forma pythônica de encapsular

Em vez de criar métodos `get_saldo()` e `set_saldo()` manualmente, Python oferece o decorador `@property`, que permite acessar e modificar atributos **como se fossem públicos**, mas com validação por baixo.

### Exemplo: conta bancária com validação

```python
class ContaBancaria:
    def __init__(self, titular, saldo_inicial=0):
        self.__titular = titular
        self.__saldo = 0
        self.saldo = saldo_inicial  # já passa pela validação do setter

    @property
    def titular(self):
        """Retorna o titular da conta."""
        return self.__titular

    @titular.setter
    def titular(self, valor):
        if isinstance(valor, str) and len(valor.strip()) > 0:
            self.__titular = valor.strip()
        else:
            raise ValueError("Titular deve ser um nome válido.")

    @property
    def saldo(self):
        """Retorna o saldo atual."""
        return self.__saldo

    @saldo.setter
    def saldo(self, valor):
        if isinstance(valor, (int, float)) and valor >= 0:
            self.__saldo = valor
        else:
            raise ValueError("Saldo não pode ser negativo.")
    
    @property
    def saldo_formatado(self):
        """Property somente leitura — calculada automaticamente."""
        return f"R$ {self.__saldo:.2f}"
```

**Usando a classe:**

```python
conta = ContaBancaria("Maria", 1000)

print(conta.titular)        # Saída: Maria
print(conta.saldo)          # Saída: 1000
print(conta.saldo_formatado) # Saída: R$ 1000.00

# Atribuição com validação — parece acesso direto, mas passa pelo setter:
conta.saldo = 1500
print(conta.saldo)          # Saída: 1500

# Tentativa inválida gera erro claro:
conta.saldo = -100
```

**Saída do erro:**
```
ValueError: Saldo não pode ser negativo.
```

```python
# Property somente leitura — não pode ser alterada diretamente:
conta.saldo_formatado = "R$ 0.00"
```

**Saída do erro:**
```
AttributeError: can't set attribute
```

---

## Por que `@property` é melhor que métodos `get`/`set`?

Compare as duas abordagens:

```python
# Abordagem antiga (com métodos explícitos):
conta.set_saldo(1500)
print(conta.get_saldo())

# Abordagem pythônica (com @property):
conta.saldo = 1500
print(conta.saldo)
```

O resultado é o mesmo. A segunda abordagem é mais legível, parece acesso direto, mas executa a validação por baixo. É o padrão recomendado em Python.

---

## Exemplo completo: Produto com validações

```python
class Produto:
    def __init__(self, nome, preco, categoria="Geral"):
        self.__nome = None
        self.__preco = None
        self.__desconto = 0
        self.__categoria = None
        # Usa os setters para validar desde a criação
        self.nome = nome
        self.preco = preco
        self.categoria = categoria

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, valor):
        if isinstance(valor, str) and len(valor.strip()) > 0:
            self.__nome = valor.strip().title()
        else:
            raise ValueError("Nome deve ser uma string não vazia.")

    @property
    def preco(self):
        return self.__preco

    @preco.setter
    def preco(self, valor):
        if isinstance(valor, (int, float)) and valor > 0:
            self.__preco = float(valor)
        else:
            raise ValueError("Preço deve ser um número positivo.")

    @property
    def categoria(self):
        return self.__categoria

    @categoria.setter
    def categoria(self, valor):
        categorias_validas = ["Eletrônicos", "Roupas", "Casa", "Livros", "Geral"]
        if valor in categorias_validas:
            self.__categoria = valor
        else:
            raise ValueError(f"Categoria inválida. Escolha entre: {categorias_validas}")

    @property
    def desconto(self):
        return self.__desconto

    @desconto.setter
    def desconto(self, valor):
        if 0 <= valor <= 100:
            self.__desconto = valor
        else:
            raise ValueError("Desconto deve estar entre 0% e 100%.")

    @property
    def preco_com_desconto(self):
        """Somente leitura — calculado automaticamente."""
        return self.__preco * (1 - self.__desconto / 100)

    @property
    def resumo(self):
        """Somente leitura — texto formatado do produto."""
        return f"{self.nome} ({self.categoria}) — R$ {self.preco_com_desconto:.2f}"


# Uso normal:
produto = Produto("smartphone", 1000)
print(produto.resumo)
# Saída: Smartphone (Geral) — R$ 1000.00

produto.categoria = "Eletrônicos"
produto.desconto = 15
print(produto.resumo)
# Saída: Smartphone (Eletrônicos) — R$ 850.00

# Validação em ação:
produto.desconto = 150
# ValueError: Desconto deve estar entre 0% e 100%.
```

---

## Exercícios

### Exercício 1 — Temperatura com validação

Crie uma classe `Temperatura` com um atributo `celsius`.

**Requisitos:**
- `celsius` deve ser uma property com validação: não aceitar valores abaixo de `-273.15` (zero absoluto)
- Adicione uma property **somente leitura** `fahrenheit` que converte automaticamente

**Esqueleto:**
```python
class Temperatura:
    def __init__(self, celsius):
        self.__celsius = None
        self.celsius = celsius  # passa pelo setter

    @property
    def celsius(self):
        # complete aqui
        pass

    @celsius.setter
    def celsius(self, valor):
        # valide e atribua
        pass

    @property
    def fahrenheit(self):
        # fórmula: (celsius * 9/5) + 32
        pass
```

**Teste esperado:**
```python
t = Temperatura(25)
print(t.celsius)     # 25
print(t.fahrenheit)  # 77.0

t.celsius = -300
# ValueError: Temperatura abaixo do zero absoluto.
```

---

### Exercício 2 — Aluno com nota protegida

Adicione à classe `Aluno` (do módulo anterior) uma nota final encapsulada.

**Requisitos:**
- `nota` deve aceitar apenas valores entre `0.0` e `10.0`
- Property somente leitura `situacao` deve retornar `"Aprovado"` (nota ≥ 6.0) ou `"Reprovado"`

---
