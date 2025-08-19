# Encapsulamento em Python

O encapsulamento é um dos pilares fundamentais da Programação Orientada a Objetos (POO) e consiste em **ocultar os detalhes internos de implementação** de uma classe, expondo apenas uma interface controlada para o mundo externo.

## Como funciona o encapsulamento

O encapsulamento permite que você:

- **Proteja dados** contra acesso ou modificação inadequada
- **Controle como** os dados são acessados e modificados
- **Mantenha a integridade** dos objetos
- **Facilite a manutenção** do código

## Níveis de visibilidade em Python

Python usa convenções de nomenclatura para indicar diferentes níveis de acesso:

### 1. Atributos Públicos (sem prefixo)

```python
class ContaBancaria:
    def __init__(self, titular):
        self.titular = titular  # Público - pode ser acessado diretamente
        
conta = ContaBancaria("João")
print(conta.titular)  # Funciona normalmente
conta.titular = "Maria"  # Pode ser alterado diretamente
```

### 2. Atributos Protegidos (um underscore _)

```python
class ContaBancaria:
    def __init__(self, titular, saldo_inicial=0):
        self.titular = titular
        self._saldo = saldo_inicial  # Protegido - convenção para uso interno
    
    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
    
    def obter_saldo(self):
        return self._saldo

conta = ContaBancaria("João", 1000)
print(conta._saldo)  # Funciona, mas não é recomendado
conta._saldo = -500  # Perigoso! Quebra a lógica do negócio
```

### 3. Atributos Privados (dois underscores __)

```python
class ContaBancaria:
    def __init__(self, titular, saldo_inicial=0):
        self.titular = titular
        self.__saldo = saldo_inicial  # Privado - name mangling
        self.__numero_conta = self.__gerar_numero()
    
    def __gerar_numero(self):  # Método privado
        import random
        return random.randint(10000, 99999)
    
    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
    
    def sacar(self, valor):
        if 0 < valor <= self.__saldo:
            self.__saldo -= valor
            return True
        return False
    
    def obter_saldo(self):
        return self.__saldo
    
    def obter_numero_conta(self):
        return self.__numero_conta

# Uso da classe
conta = ContaBancaria("Ana", 1500)

# Acesso correto através de métodos
print(conta.obter_saldo())  # 1500
conta.depositar(500)
print(conta.obter_saldo())  # 2000

# Tentativa de acesso direto falha
# print(conta.__saldo)  # AttributeError!
# print(conta.__numero_conta)  # AttributeError!
```

| Tipo | Sintaxe | Acesso | Herança | Propósito |
|------|---------|--------|---------|-----------|
| **Público** | `nome` | ✅ Total | ✅ Sim | Interface oficial |
| **Protegido** | `_nome` | ⚠️ Por convenção | ✅ Sim | Uso interno/herança |
| **Privado** | `__nome` | ❌ Name mangling | ❌ Não | Implementação interna |

**Dica importante**: Em Python, a proteção é mais sobre **convenção** e **boas práticas** do que proteção real.

## Exemplo prático: Sistema de validação

```python
class Pessoa:
    def __init__(self, nome, idade):
        self.__nome = nome
        self.__idade = None
        self.definir_idade(idade)  # Usa o setter para validação
    
    # Getter para nome
    def obter_nome(self):
        return self.__nome
    
    # Setter para nome com validação
    def definir_nome(self, nome):
        if isinstance(nome, str) and len(nome.strip()) > 0:
            self.__nome = nome.strip()
        else:
            raise ValueError("Nome deve ser uma string não vazia")
    
    # Getter para idade
    def obter_idade(self):
        return self.__idade
    
    # Setter para idade com validação
    def definir_idade(self, idade):
        if isinstance(idade, int) and 0 <= idade <= 150:
            self.__idade = idade
        else:
            raise ValueError("Idade deve ser um número entre 0 e 150")
    
    def apresentar(self):
        return f"Olá, eu sou {self.__nome} e tenho {self.__idade} anos"

# Uso seguro da classe
pessoa = Pessoa("Carlos", 30)
print(pessoa.apresentar())

# Validação em ação
try:
    pessoa.definir_idade(-5)  # Erro!
except ValueError as e:
    print(f"Erro: {e}")

try:
    pessoa.definir_nome("")  # Erro!
except ValueError as e:
    print(f"Erro: {e}")
```

## Properties: A forma pythônica

Python oferece uma maneira mais elegante usando `@property`:

```python
class Produto:
    def __init__(self, nome, preco):
        self.__nome = nome
        self.__preco = None
        self.preco = preco  # Usa o setter
    
    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, valor):
        if isinstance(valor, str) and len(valor.strip()) > 0:
            self.__nome = valor.strip()
        else:
            raise ValueError("Nome deve ser uma string não vazia")
    
    @property
    def preco(self):
        return self.__preco
    
    @preco.setter
    def preco(self, valor):
        if isinstance(valor, (int, float)) and valor >= 0:
            self.__preco = valor
        else:
            raise ValueError("Preço deve ser um número não negativo")
    
    def __str__(self):
        return f"{self.nome}: R$ {self.preco:.2f}"

# Uso como se fossem atributos normais
produto = Produto("Notebook", 2500.00)
print(produto.nome)  # Notebook
print(produto.preco)  # 2500.0

# Mas com validação automática
try:
    produto.preco = -100  # Erro!
except ValueError as e:
    print(f"Erro: {e}")
```

## Getter e Setter

Em Python, há várias maneiras de implementar getters e setters. As principais abordagens são:

## 1. Métodos explícitos (abordagem tradicional)

```python
class Pessoa:
    def __init__(self, nome, idade):
        self.__nome = nome
        self.__idade = idade
    
    # Getter para nome
    def get_nome(self):
        return self.__nome
    
    # Setter para nome
    def set_nome(self, nome):
        if isinstance(nome, str) and len(nome.strip()) > 0:
            self.__nome = nome.strip()
        else:
            raise ValueError("Nome deve ser uma string não vazia")
    
    # Getter para idade
    def get_idade(self):
        return self.__idade
    
    # Setter para idade
    def set_idade(self, idade):
        if isinstance(idade, int) and 0 <= idade <= 150:
            self.__idade = idade
        else:
            raise ValueError("Idade deve estar entre 0 e 150")

# Uso
pessoa = Pessoa("João", 25)
print(pessoa.get_nome())  # João
pessoa.set_idade(30)
print(pessoa.get_idade())  # 30
```

## 2. Properties (abordagem pythônica) - RECOMENDADA

### Usando decoradores @property

```python
class ContaBancaria:
    def __init__(self, titular, saldo=0):
        self.__titular = titular
        self.__saldo = saldo
    
    @property
    def titular(self):
        """Getter para titular"""
        return self.__titular
    
    @titular.setter
    def titular(self, valor):
        """Setter para titular"""
        if isinstance(valor, str) and len(valor.strip()) > 0:
            self.__titular = valor.strip()
        else:
            raise ValueError("Titular deve ser uma string não vazia")
    
    @property
    def saldo(self):
        """Getter para saldo"""
        return self.__saldo
    
    @saldo.setter
    def saldo(self, valor):
        """Setter para saldo"""
        if isinstance(valor, (int, float)) and valor >= 0:
            self.__saldo = valor
        else:
            raise ValueError("Saldo deve ser um número não negativo")
    
    @property
    def saldo_formatado(self):
        """Property somente leitura"""
        return f"R$ {self.__saldo:.2f}"

# Uso - parece acesso direto aos atributos!
conta = ContaBancaria("Maria", 1000)
print(conta.titular)  # Maria
print(conta.saldo)    # 1000
print(conta.saldo_formatado)  # R$ 1000.00

# Mas com validação automática
conta.titular = "João Silva"  # Funciona
conta.saldo = 1500           # Funciona

try:
    conta.saldo = -100  # Erro!
except ValueError as e:
    print(f"Erro: {e}")
```

## 3. Usando a função property()

```python
class Temperatura:
    def __init__(self, celsius=0):
        self.__celsius = celsius
    
    def get_celsius(self):
        return self.__celsius
    
    def set_celsius(self, valor):
        if valor < -273.15:
            raise ValueError("Temperatura não pode ser menor que -273.15°C")
        self.__celsius = valor
    
    def get_fahrenheit(self):
        return (self.__celsius * 9/5) + 32
    
    def set_fahrenheit(self, valor):
        celsius = (valor - 32) * 5/9
        self.set_celsius(celsius)  # Reutiliza a validação
    
    def get_kelvin(self):
        return self.__celsius + 273.15
    
    def set_kelvin(self, valor):
        celsius = valor - 273.15
        self.set_celsius(celsius)  # Reutiliza a validação
    
    # Criando as properties
    celsius = property(get_celsius, set_celsius)
    fahrenheit = property(get_fahrenheit, set_fahrenheit)
    kelvin = property(get_kelvin, set_kelvin)

# Uso
temp = Temperatura(25)
print(f"Celsius: {temp.celsius}")      # 25
print(f"Fahrenheit: {temp.fahrenheit}") # 77.0
print(f"Kelvin: {temp.kelvin}")        # 298.15

# Alterando por diferentes escalas
temp.fahrenheit = 86
print(f"Celsius: {temp.celsius}")      # 30.0
```

## 4. Property somente leitura

```python
class Circulo:
    def __init__(self, raio):
        self.__raio = raio
    
    @property
    def raio(self):
        return self.__raio
    
    @raio.setter
    def raio(self, valor):
        if valor > 0:
            self.__raio = valor
        else:
            raise ValueError("Raio deve ser positivo")
    
    @property
    def area(self):
        """Property somente leitura - calculada dinamicamente"""
        import math
        return math.pi * self.__raio ** 2
    
    @property
    def circunferencia(self):
        """Property somente leitura - calculada dinamicamente"""
        import math
        return 2 * math.pi * self.__raio

# Uso
circulo = Circulo(5)
print(f"Raio: {circulo.raio}")              # 5
print(f"Área: {circulo.area:.2f}")          # 78.54
print(f"Circunferência: {circulo.circunferencia:.2f}")  # 31.42

# Pode alterar o raio
circulo.raio = 10
print(f"Nova área: {circulo.area:.2f}")     # 314.16

# Mas não pode alterar área diretamente
# circulo.area = 100  # AttributeError!
```

## 5. Exemplo prático completo

```python
class Produto:
    def __init__(self, nome, preco, categoria="Geral"):
        self.__nome = nome
        self.__preco = preco
        self.__categoria = categoria
        self.__desconto = 0
    
    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, valor):
        if isinstance(valor, str) and len(valor.strip()) > 0:
            self.__nome = valor.strip().title()
        else:
            raise ValueError("Nome deve ser uma string não vazia")
    
    @property
    def preco(self):
        return self.__preco
    
    @preco.setter
    def preco(self, valor):
        if isinstance(valor, (int, float)) and valor > 0:
            self.__preco = float(valor)
        else:
            raise ValueError("Preço deve ser um número positivo")
    
    @property
    def categoria(self):
        return self.__categoria
    
    @categoria.setter
    def categoria(self, valor):
        categorias_validas = ["Eletrônicos", "Roupas", "Casa", "Livros", "Geral"]
        if valor in categorias_validas:
            self.__categoria = valor
        else:
            raise ValueError(f"Categoria deve ser uma de: {categorias_validas}")
    
    @property
    def desconto(self):
        return self.__desconto
    
    @desconto.setter
    def desconto(self, valor):
        if 0 <= valor <= 100:
            self.__desconto = valor
        else:
            raise ValueError("Desconto deve estar entre 0 e 100%")
    
    @property
    def preco_com_desconto(self):
        """Property calculada - somente leitura"""
        return self.__preco * (1 - self.__desconto / 100)
    
    @property
    def info_completa(self):
        """Property formatada - somente leitura"""
        return f"{self.nome} ({self.categoria}) - R$ {self.preco_com_desconto:.2f}"

# Uso
produto = Produto("smartphone", 1000)
print(produto.info_completa)  # Smartphone (Geral) - R$ 1000.00

produto.categoria = "Eletrônicos"
produto.desconto = 15
print(produto.info_completa)  # Smartphone (Eletrônicos) - R$ 850.00

# Validação funcionando
try:
    produto.desconto = 150  # Erro!
except ValueError as e:
    print(f"Erro: {e}")
```

### Quando usar cada abordagem?

**Properties (@property)**: Use sempre que possível - é a forma mais pythônica
**Métodos explícitos**: Apenas quando você precisa de compatibilidade com código muito antigo
**Property somente leitura**: Para valores calculados ou que não devem ser alterados externamente

