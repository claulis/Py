# Classes e Objetos em Python

Representar entidades em Python requer usar classes e objetos. Entender esses conceitos envolve:

- **Classe**: Definir um molde que especifica atributos (dados) e métodos (comportamentos) de uma entidade. No sistema acadêmico de frequência, modelar a classe `Aluno` abstrai características como nome e matrícula.
- **Objeto**: Criar uma instância específica de uma classe, contendo valores próprios para os atributos. Por exemplo, instanciar `Aluno("Ana", "2023001")` gera um objeto representando um aluno específico.

[Exemplo completo](../POB/asset/code/chamada/)

## Estruturar uma Classe

Construir uma classe em Python utiliza a palavra-chave `class`, seguida por um nome (geralmente em CamelCase). A estrutura inclui:

- **Construtor**: Implementar o método `__init__` para inicializar atributos da instância.
- **Atributos**: Declarar variáveis de instância (usando `self`) ou de classe (definidas diretamente na classe).
- **Métodos**: Definir funções que operam nos atributos, incluindo métodos de instância, de classe ou estáticos.

Exemplo básico:

```python
class Exemplo:
    def __init__(self, valor):
        self.atributo_instancia = valor
    
    def executar_acao(self):
        return f"Valor: {self.atributo_instancia}"
```

## Métodos Construtores

Definir um construtor com `__init__` permite inicializar atributos ao criar um objeto. O parâmetro `self` refere-se à instância sendo criada. No sistema de frequência, a classe `Aluno` usa um construtor para definir `nome`, `matricula` e `presencas`:

```python
class Aluno:
    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula
        self.presencas = []
```

Exemplo funcional:

```python
aluno = Aluno("Ana", "2023001")
print(aluno.nome)  # Saída: Ana
print(aluno.matricula)  # Saída: 2023001
print(aluno.presencas)  # Saída: []
```

Personalizar o construtor permite inicializar objetos com diferentes configurações. Por exemplo, adicionar um parâmetro opcional para presenças iniciais:

```python
class Aluno:
    def __init__(self, nome, matricula, presencas_iniciais=None):
        self.nome = nome
        self.matricula = matricula
        self.presencas = presencas_iniciais if presencas_iniciais is not None else []
```

Exemplo funcional:

```python
aluno1 = Aluno("Bruno", "2023002")
aluno2 = Aluno("Clara", "2023003", ["2025-07-30"])
print(aluno1.presencas)  # Saída: []
print(aluno2.presencas)  # Saída: ["2025-07-30"]
```

## Variáveis de Instância

Declarar variáveis com `self` associa-as a uma instância específica. Cada objeto possui seus próprios valores. No sistema de frequência, `nome`, `matricula` e `presencas` são variáveis de instância:

```python
class Aluno:
    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula
        self.presencas = []
    
    def adicionar_presenca(self, data):
        self.presencas.append(data)
```

Exemplo funcional:

```python
aluno1 = Aluno("Ana", "2023001")
aluno2 = Aluno("Bruno", "2023002")
aluno1.adicionar_presenca("2025-07-30")
print(aluno1.presencas)  # Saída: ["2025-07-30"]
print(aluno2.presencas)  # Saída: []
```

## Variáveis de Classe

Definir variáveis diretamente na classe cria atributos compartilhados por todas as instâncias. No sistema de frequência, contar o total de alunos requer uma variável de classe:

```python
class Aluno:
    total_alunos = 0  # Variável de classe
    
    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula
        self.presencas = []
        Aluno.total_alunos += 1
```

Exemplo funcional:

```python
aluno1 = Aluno("Ana", "2023001")
aluno2 = Aluno("Bruno", "2023002")
print(Aluno.total_alunos)  # Saída: 2
print(aluno1.total_alunos)  # Saída: 2
```

## Métodos de Instância

Definir métodos com `self` permite operar nos atributos da instância. No sistema de frequência, o método `adicionar_presenca` modifica a lista `presencas` do objeto:

```python
class Aluno:
    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula
        self.presencas = []
    
    def adicionar_presenca(self, data):
        if data not in self.presencas:
            self.presencas.append(data)
            return f"Presença registrada para {self.nome} em {data}."
        return f"Presença já registrada para {self.nome} em {data}."
```

Exemplo funcional:

```python
aluno = Aluno("Ana", "2023001")
print(aluno.adicionar_presenca("2025-07-30"))  # Saída: Presença registrada para Ana em 2025-07-30.
print(aluno.adicionar_presenca("2025-07-30"))  # Saída: Presença já registrada para Ana em 2025-07-30.
print(aluno.presencas)  # Saída: ["2025-07-30"]
```

## Métodos de Classe

Usar o decorador `@classmethod` define métodos que operam na classe, recebendo `cls` como primeiro parâmetro. No sistema de frequência, consultar o total de alunos pode ser implementado assim:

```python
class Aluno:
    total_alunos = 0
    
    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula
        self.presencas = []
        Aluno.total_alunos += 1
    
    @classmethod
    def obter_total_alunos(cls):
        return f"Total de alunos cadastrados: {cls.total_alunos}"
```

Exemplo funcional:

```python
aluno1 = Aluno("Ana", "2023001")
aluno2 = Aluno("Bruno", "2023002")
print(Aluno.obter_total_alunos())  # Saída: Total de alunos cadastrados: 2
```

## Métodos Estáticos

Definir métodos com `@staticmethod` cria funções que não dependem de instâncias ou da classe. No sistema de frequência, validar o formato de uma data pode ser um método estático:

```python
class Aluno:
    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula
        self.presencas = []
    
    @staticmethod
    def validar_data(data):
        from datetime import datetime
        try:
            datetime.strptime(data, "%Y-%m-%d")
            return True
        except ValueError:
            return False
```

Exemplo funcional:

```python
print(Aluno.validar_data("2025-07-30"))  # Saída: True
print(Aluno.validar_data("invalido"))  # Saída: False
```

## Aplicar Abstração

Abstrair consiste em modelar apenas os aspectos relevantes de uma entidade. No sistema de frequência:

- **Aluno**: Representar com `nome`, `matricula` e `presencas`, ignorando detalhes como endereço.
- **Professor**: Definir com `nome`, `id_professor` e o método `registrar_presenca`.
- **Turma**: Estruturar com `codigo`, `professor` e uma lista de `alunos`.

Exemplo funcional no sistema de frequência:

```python
class Aluno:
    total_alunos = 0
    
    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula
        self.presencas = []
        Aluno.total_alunos += 1
    
    def adicionar_presenca(self, data):
        if data not in self.presencas:
            self.presencas.append(data)
            return f"Presença registrada para {self.nome} em {data}."
        return f"Presença já registrada para {self.nome} em {data}."
    
    @classmethod
    def obter_total_alunos(cls):
        return f"Total de alunos: {cls.total_alunos}"
    
    @staticmethod
    def validar_data(data):
        from datetime import datetime
        try:
            datetime.strptime(data, "%Y-%m-%d")
            return True
        except ValueError:
            return False

class Professor:
    def __init__(self, nome, id_professor):
        self.nome = nome
        self.id_professor = id_professor
    
    def registrar_presenca(self, aluno, turma, data):
        if Aluno.validar_data(data) and aluno in turma.alunos:
            return aluno.adicionar_presenca(data)
        return f"Erro: Data inválida ou aluno {aluno.nome} não matriculado na turma {turma.codigo}."

class Turma:
    def __init__(self, codigo, professor):
        self.codigo = codigo
        self.professor = professor
        self.alunos = []
    
    def matricular_aluno(self, aluno):
        if aluno not in self.alunos:
            self.alunos.append(aluno)
            return f"Aluno {aluno.nome} matriculado na turma {self.codigo}."
        return f"Aluno {aluno.nome} já matriculado na turma {self.codigo}."

# Testar o sistema
professor = Professor("Dr. Carlos", "P001")
turma = Turma("T101", professor)
aluno = Aluno("Ana", "2023001")
print(turma.matricular_aluno(aluno))  # Saída: Aluno Ana matriculado na turma T101.
print(professor.registrar_presenca(aluno, turma, "2025-07-30"))  # Saída: Presença registrada para Ana em 2025-07-30.
print(Aluno.obter_total_alunos())  # Saída: Total de alunos: 1
print(Aluno.validar_data("2025-07-30"))  # Saída: True
```

## Conceitos chave

Compreender classes e objetos em Python envolve:

1. Definir classes como moldes com atributos e métodos.
2. Criar objetos como instâncias com valores específicos.
3. Usar construtores para inicializar atributos.
4. Declarar variáveis de instância para dados específicos e de classe para dados compartilhados.
5. Implementar métodos de instância, de classe e estáticos para diferentes funcionalidades.
6. Aplicar abstração para focar no essencial.
7. Explorar encapsulamento, herança e polimorfismo para designs robustos.
