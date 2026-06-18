# Classes e Objetos

## O sistema que vamos construir

Sistema de exemplo nesse arquivo: **sistema de registro de frequência** para uma turma. As entidades do sistema são:

- `Aluno` — tem nome, matrícula e uma lista de presenças
- `Professor` — pode registrar presenças
- `Turma` — agrupa alunos e tem um professor responsável

Esse contexto vai guiar todos os exemplos.

[Exemplo completo](../POB/asset/code/chamada/)

---

## Estruturar uma Classe

Uma classe em Python começa com a palavra-chave `class`, seguida de um nome.

> **Convenção importante:** nomes de classe usam **CamelCase** — cada palavra começa com maiúscula, sem espaço ou underline. Por exemplo: `Aluno`, `ContaBancaria`, `RegistroFrequencia`. Isso não é obrigatório, mas é o padrão da linguagem e do mercado.

Estrutura básica:

```python
class NomeDaClasse:
    def __init__(self, parametros):
        self.atributo = parametros
    
    def nome_do_metodo(self):
        # código aqui
        pass
```

---

## O Construtor `__init__`

O método `__init__` é chamado automaticamente toda vez que você cria um objeto. Ele é responsável por **inicializar os atributos** do objeto.

O parâmetro `self` representa o próprio objeto que está sendo criado. Quando você escreve `self.nome`, está dizendo: "este objeto tem um atributo chamado `nome`".

```python
class Aluno:
    def __init__(self, nome, matricula):
        self.nome = nome          # atributo: nome do aluno
        self.matricula = matricula # atributo: matrícula
        self.presencas = []       # atributo: lista de presenças (começa vazia)
```

Criando objetos a partir dessa classe:

```python
aluno = Aluno("Ana", "2023001")

print(aluno.nome)       # Saída: Ana
print(aluno.matricula)  # Saída: 2023001
print(aluno.presencas)  # Saída: []
```

> **Dica:** `self` é sempre o primeiro parâmetro dos métodos, mas você nunca o passa explicitamente. Python faz isso automaticamente.

---

## Variáveis de Instância

Variáveis de instância são atributos que **pertencem a cada objeto individualmente**. Cada objeto tem seus próprios valores — alterar o atributo de um não afeta o outro.

```python
class Aluno:
    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula
        self.presencas = []
    
    def adicionar_presenca(self, data):
        self.presencas.append(data)

aluno1 = Aluno("Ana", "2023001")
aluno2 = Aluno("Bruno", "2023002")

aluno1.adicionar_presenca("2025-07-30")

print(aluno1.presencas)  # Saída: ["2025-07-30"]
print(aluno2.presencas)  # Saída: []  ← não foi afetado
```

---

## Variáveis de Classe

Variáveis de classe são definidas **diretamente na classe**, fora de qualquer método. Elas são **compartilhadas por todos os objetos** da classe.

Use variáveis de classe quando um dado pertence à classe como um todo, não a um objeto específico. Um bom exemplo é contar quantos alunos foram criados:

```python
class Aluno:
    total_alunos = 0  # variável de classe — compartilhada por todos

    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula
        self.presencas = []
        Aluno.total_alunos += 1  # incrementa sempre que um aluno é criado

aluno1 = Aluno("Ana", "2023001")
aluno2 = Aluno("Bruno", "2023002")

print(Aluno.total_alunos)   # Saída: 2
print(aluno1.total_alunos)  # Saída: 2  ← todos enxergam o mesmo valor
```

> **Quando usar cada uma?**
> - Dado que pertence a **um objeto específico** → variável de instância (`self.nome`)
> - Dado que pertence a **todos os objetos** → variável de classe (`Aluno.total_alunos`)

---

## Métodos de Instância

Métodos de instância são funções que **operam nos atributos de um objeto específico**. Eles sempre recebem `self` como primeiro parâmetro.

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

aluno = Aluno("Ana", "2023001")

print(aluno.adicionar_presenca("2025-07-30"))
# Saída: Presença registrada para Ana em 2025-07-30.

print(aluno.adicionar_presenca("2025-07-30"))
# Saída: Presença já registrada para Ana em 2025-07-30.
```

---

## Métodos de Classe

Métodos de classe operam na **classe em si**, não em um objeto específico. São definidos com o decorador `@classmethod` e recebem `cls` como primeiro parâmetro.

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

aluno1 = Aluno("Ana", "2023001")
aluno2 = Aluno("Bruno", "2023002")

print(Aluno.obter_total_alunos())
# Saída: Total de alunos cadastrados: 2
```

<img width="816" height="600" alt="metodo_classe_vs_instancia" src="https://github.com/user-attachments/assets/bcf96f29-dda4-4fe2-8dcb-3313a39ef3dc" />

---

## Métodos Estáticos

Métodos estáticos **não dependem de instâncias nem da classe**. São funções utilitárias que fazem sentido viver dentro da classe por questão de organização.

São definidos com `@staticmethod` e **não recebem `self` nem `cls`**.

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

print(Aluno.validar_data("2025-07-30"))  # Saída: True
print(Aluno.validar_data("30/07/2025")) # Saída: False
print(Aluno.validar_data("invalido"))   # Saída: False
```

**Quando usar cada tipo de método:**

| Tipo | Decorador | Primeiro parâmetro | Quando usar |
|---|---|---|---|
| Instância | (nenhum) | `self` | Quando precisa acessar ou modificar dados do objeto |
| Classe | `@classmethod` | `cls` | Quando precisa acessar ou modificar dados da classe |
| Estático | `@staticmethod` | (nenhum) | Função utilitária relacionada à classe, sem precisar de dados dela |

<img width="828" height="600" alt="trio_metodos_tabela" src="https://github.com/user-attachments/assets/ac901bb7-25d5-4f11-b9af-e4d82406b54b" />

---

## Sistema completo

Juntando tudo: `Aluno`, `Professor` e `Turma` trabalhando juntos.

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
        if not Aluno.validar_data(data):
            return f"Erro: Data '{data}' está em formato inválido. Use AAAA-MM-DD."
        if aluno not in turma.alunos:
            return f"Erro: {aluno.nome} não está matriculado na turma {turma.codigo}."
        return aluno.adicionar_presenca(data)


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


# Testando o sistema
professor = Professor("Dr. Carlos", "P001")
turma = Turma("T101", professor)
aluno = Aluno("Ana", "2023001")

print(turma.matricular_aluno(aluno))
# Saída: Aluno Ana matriculado na turma T101.

print(professor.registrar_presenca(aluno, turma, "2025-07-30"))
# Saída: Presença registrada para Ana em 2025-07-30.

print(professor.registrar_presenca(aluno, turma, "30/07/2025"))
# Saída: Erro: Data '30/07/2025' está em formato inválido. Use AAAA-MM-DD.

print(Aluno.obter_total_alunos())
# Saída: Total de alunos: 1
```

---

## Exercícios

Use o sistema acima como base. Antes de escrever código, responda no papel as perguntas de cada exercício.

### Exercício 1 — Remover presença de um aluno

**Pense antes:**
- O que o método precisa receber como parâmetro?
- O que acontece se a data não estiver na lista?
- Qual método já existe que você pode usar como referência?

**Esqueleto:**
```python
def remover_presenca(self, data):
    if data in self.presencas:
        # complete aqui
        return f"..."
    return f"..."
```

**Teste esperado:**
```python
aluno.adicionar_presenca("2025-07-30")
print(aluno.remover_presenca("2025-07-30"))
# Saída: Presença de Ana removida em 2025-07-30.
print(aluno.remover_presenca("2025-07-30"))
# Saída: Presença não encontrada para Ana em 2025-07-30.
```

---

### Exercício 2 — Professor remove presença

**Pense antes:**
- O professor já pode registrar presença. Que verificações ele faz?
- O método de remover presença deve ter verificações semelhantes?

**Esqueleto:**
```python
def remover_presenca(self, aluno, turma, data):
    # faça as mesmas verificações que registrar_presenca
    # depois chame o método de remoção do aluno
    pass
```

---

### Exercício 3 — Operações na Turma

Implemente três métodos na classe `Turma`:

**a) Remover aluno**
```python
def remover_aluno(self, aluno):
    # O que verificar antes de remover?
    pass
```

**b) Substituir professor**
```python
def substituir_professor(self, novo_professor):
    # Como guardar quem era o professor anterior?
    pass
```

**c) Aluno com mais presenças**
```python
def aluno_mais_presente(self):
    # Dica: use a função max() com uma função lambda ou key
    # max(self.alunos, key=lambda a: len(a.presencas))
    pass
```

**Teste esperado para c):**
```python
aluno1 = Aluno("Ana", "2023001")
aluno2 = Aluno("Bruno", "2023002")
aluno1.adicionar_presenca("2025-07-28")
aluno1.adicionar_presenca("2025-07-29")
aluno2.adicionar_presenca("2025-07-28")
turma.matricular_aluno(aluno1)
turma.matricular_aluno(aluno2)

mais_presente = turma.aluno_mais_presente()
print(mais_presente.nome)  # Saída: Ana
```

---

## Exercicio

Pegue o codigo no exemplo e desenvolva:

1. Aluno: remover uma data na lista de frequências
2. Professor: remover uma presença
3. Turma: remover aluno da turma, substituir professor, retornar o aluno que tem mais frequencia

