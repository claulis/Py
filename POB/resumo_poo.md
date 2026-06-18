# Resumo POO — Os 4 Pilares em Um Exemplo

Um único sistema mostrando **abstração**, **encapsulamento**, **herança** e **polimorfismo** juntos.

---

## O sistema

Uma escola tem alunos regulares e alunos especiais. O sistema registra presenças, valida notas e gera um boletim para qualquer tipo de aluno.

---

## Código completo anotado

```python
from abc import ABC, abstractmethod


# ╔══════════════════════════════════════════════════════════════╗
# ║  ABSTRAÇÃO                                                   ║
# ║  Modelamos apenas o que importa para o sistema:              ║
# ║  nome, matrícula, nota e presenças.                          ║
# ║  Ignoramos: endereço, telefone, cor dos olhos, etc.          ║
# ╚══════════════════════════════════════════════════════════════╝

class Aluno(ABC):                           # classe abstrata — não pode ser instanciada
    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula
        self.presencas = []
        self.__nota = None                  # ← ENCAPSULAMENTO (ver abaixo)

    # ┌──────────────────────────────────────────────────────────┐
    # │  ENCAPSULAMENTO                                          │
    # │  nota não pode ser qualquer valor — precisa ser 0 a 10. │
    # │  @property controla o acesso e a validação.              │
    # └──────────────────────────────────────────────────────────┘

    @property
    def nota(self):
        return self.__nota

    @nota.setter
    def nota(self, valor):
        if isinstance(valor, (int, float)) and 0 <= valor <= 10:
            self.__nota = round(float(valor), 1)
        else:
            raise ValueError(f"Nota inválida: {valor}. Deve ser entre 0 e 10.")

    @property
    def situacao(self):                     # somente leitura — calculada automaticamente
        if self.__nota is None:
            return "Sem nota"
        return "Aprovado" if self.__nota >= 6.0 else "Reprovado"

    def adicionar_presenca(self, data):
        if data not in self.presencas:
            self.presencas.append(data)

    # ┌──────────────────────────────────────────────────────────┐
    # │  POLIMORFISMO                                            │
    # │  boletim() é abstrato — cada subclasse define           │
    # │  como gera o seu. A função gerar_boletim() chama        │
    # │  .boletim() sem saber qual tipo de aluno está usando.   │
    # └──────────────────────────────────────────────────────────┘

    @abstractmethod
    def boletim(self):
        pass


# ╔══════════════════════════════════════════════════════════════╗
# ║  HERANÇA                                                     ║
# ║  AlunoRegular e AlunoEspecial herdam tudo de Aluno:         ║
# ║  nome, matrícula, presenças, nota, situacao.                ║
# ║  Cada um adiciona apenas o que tem de diferente.            ║
# ╚══════════════════════════════════════════════════════════════╝

class AlunoRegular(Aluno):
    def __init__(self, nome, matricula):
        super().__init__(nome, matricula)   # herda o __init__ de Aluno

    def boletim(self):                      # ← POLIMORFISMO: implementação própria
        return (
            f"[REGULAR] {self.nome} | Matrícula: {self.matricula}\n"
            f"  Nota: {self.nota} | Situação: {self.situacao}\n"
            f"  Presenças: {len(self.presencas)} dia(s)"
        )


class AlunoEspecial(Aluno):
    def __init__(self, nome, matricula, adaptacoes):
        super().__init__(nome, matricula)   # herda o __init__ de Aluno
        self.adaptacoes = adaptacoes        # adiciona o que é específico

    def boletim(self):                      # ← POLIMORFISMO: implementação própria
        return (
            f"[ESPECIAL] {self.nome} | Matrícula: {self.matricula}\n"
            f"  Nota: {self.nota} | Situação: {self.situacao}\n"
            f"  Presenças: {len(self.presencas)} dia(s)\n"
            f"  Adaptações: {', '.join(self.adaptacoes)}"
        )


# ┌──────────────────────────────────────────────────────────────┐
# │  POLIMORFISMO em uso                                         │
# │  gerar_boletim() não sabe se recebe AlunoRegular            │
# │  ou AlunoEspecial — e não precisa saber.                    │
# │  Funciona com qualquer subclasse de Aluno.                   │
# └──────────────────────────────────────────────────────────────┘

def gerar_boletim(aluno):
    print(aluno.boletim())
    print()
```

---

## Executando o sistema

```python
# Criando alunos
ana = AlunoRegular("Ana", "2023001")
bruno = AlunoEspecial("Bruno", "2023002", ["tempo estendido", "prova ampliada"])

# Registrando presenças
ana.adicionar_presenca("2025-07-28")
ana.adicionar_presenca("2025-07-29")
ana.adicionar_presenca("2025-07-30")

bruno.adicionar_presenca("2025-07-28")
bruno.adicionar_presenca("2025-07-30")

# Atribuindo notas (passa pelo setter — encapsulamento)
ana.nota = 8.5
bruno.nota = 5.0

# Gerando boletins (polimorfismo — mesma função, comportamentos diferentes)
gerar_boletim(ana)
gerar_boletim(bruno)

# Tentativa de nota inválida
ana.nota = 11
```

**Saída:**
```
[REGULAR] Ana | Matrícula: 2023001
  Nota: 8.5 | Situação: Aprovado
  Presenças: 3 dia(s)

[ESPECIAL] Bruno | Matrícula: 2023002
  Nota: 5.0 | Situação: Reprovado
  Presenças: 2 dia(s)
  Adaptações: tempo estendido, prova ampliada

ValueError: Nota inválida: 11. Deve ser entre 0 e 10.
```

---

## Onde está cada pilar

| Pilar | Onde aparece no código | O que faz |
|---|---|---|
| **Abstração** | Classe `Aluno` | Modela só o que o sistema precisa: nome, matrícula, nota, presenças |
| **Encapsulamento** | `@property nota` e `@property situacao` | Controla acesso à nota; impede valores inválidos; calcula situação automaticamente |
| **Herança** | `AlunoRegular(Aluno)` e `AlunoEspecial(Aluno)` | Reutiliza tudo de `Aluno`; cada subclasse adiciona apenas o que é específico |
| **Polimorfismo** | Método `boletim()` e função `gerar_boletim()` | A mesma função gera o boletim de qualquer tipo de aluno sem saber qual é |

---

## O fluxo visual

```
          ┌─────────────────────────────┐
          │         Aluno (ABC)         │  ← ABSTRAÇÃO: modela a entidade
          │  nome, matricula, presencas │
          │  @property nota             │  ← ENCAPSULAMENTO: protege o dado
          │  @property situacao         │
          │  @abstractmethod boletim()  │  ← POLIMORFISMO: contrato obrigatório
          └──────────────┬──────────────┘
                         │ HERANÇA
           ┌─────────────┴──────────────┐
           │                            │
  ┌────────┴────────┐        ┌──────────┴──────────┐
  │  AlunoRegular   │        │    AlunoEspecial     │
  │  boletim()      │        │  adaptacoes          │
  │  (versão A)     │        │  boletim()           │
  └─────────────────┘        │  (versão B)          │
                             └──────────────────────┘
                                        │ POLIMORFISMO
                             ┌──────────┴──────────┐
                             │   gerar_boletim()   │
                             │  funciona com       │
                             │  qualquer Aluno     │
                             └─────────────────────┘
```

---

## Em uma frase cada

- **Abstração** — *"O que esse objeto precisa ter?"* Você escolhe os atributos relevantes e ignora o resto.
- **Encapsulamento** — *"Quem pode mexer nisso e como?"* Você controla o acesso e valida os dados.
- **Herança** — *"O que esse tipo de aluno tem em comum com todos os outros?"* Você reaproveita sem repetir.
- **Polimorfismo** — *"Posso tratar tipos diferentes da mesma forma?"* A função não precisa saber qual tipo está usando.
