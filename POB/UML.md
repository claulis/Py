# UML: Diagramas de Caso de Uso e Classe

## 📚 Introdução

**UML (Unified Modeling Language)** é uma linguagem gráfica padronizada para modelagem de sistemas de software. Ela fornece notações visuais que facilitam a comunicação entre designers, desenvolvedores e stakeholders.

> "A UML permite que você visualize, especifique, construa e documente os artefatos de um sistema de software intensivo em software." — OMG (Object Management Group)

### Por que usar UML?

- ✅ **Comunicação clara** entre equipes multidisciplinares
- ✅ **Documentação visual** do sistema antes da codificação
- ✅ **Identificação de problemas** em fase de design
- ✅ **Reutilização de padrões** e arquitetura
- ✅ **Facilita manutenção** e evolução do código

---

## 📊 Tipos Principais de Diagramas UML

| Tipo | Propósito | Quando Usar |
|------|----------|-----------|
| **Caso de Uso** | Comportamento do sistema do ponto de vista do usuário | Fase de requisitos e escopo |
| **Classe** | Estrutura estática: classes, atributos, relacionamentos | Design detalhado |
| **Sequência** | Interação temporal entre objetos | Fluxos e protocolos |
| **Atividade** | Fluxo de processos e workflows | Lógica de negócio |
| **Estado** | Mudanças de estado de um objeto | Máquinas de estado |
| **Componente** | Componentes de software e dependências | Arquitetura |
| **Deployment** | Distribuição física do sistema | Infraestrutura |

---

## 1️⃣ Diagrama de Caso de Uso

### O que é?

Um **diagrama de caso de uso** modela o comportamento externo do sistema, descrevendo **quem** (ator) interage **com quê** (caso de uso) e **por quê** (objetivo).

### Elementos Principais

```
┌─────────────────────────────────────────────────────────┐
│  DIAGRAMA DE CASO DE USO - Elementos Básicos           │
├─────────────────────────────────────────────────────────┤
│                                                           │
│  ATOR (Actor):                                           │
│    👤  Representa um papel de usuário ou sistema         │
│                                                           │
│  CASO DE USO (Use Case):                                 │
│    (elipse)  Funcionalidade/tarefa que o sistema faz    │
│                                                           │
│  SISTEMA (System):                                       │
│    [retângulo] Delimita o escopo do sistema             │
│                                                           │
│  RELACIONAMENTOS:                                        │
│    ──→  Associação (ator participa do caso de uso)      │
│    ▷──  Include (caso de uso necessário/obrigatório)    │
│    ◁──  Extend (caso de uso opcional/condicional)       │
│                                                           │
└─────────────────────────────────────────────────────────┘
```

### Exemplo 1: Sistema de Biblioteca

```plantuml
@startuml BibliotecaCasoDeUso
left to right direction
skinparam packageStyle rectangle

actor "Leitor" as Leitor
actor "Bibliotecário" as Bibliotecario
actor "Administrador" as Admin

rectangle "Sistema de Biblioteca" {
    usecase "Buscar Livro" as UC1
    usecase "Emprestar Livro" as UC2
    usecase "Devolver Livro" as UC3
    usecase "Renovar Empréstimo" as UC4
    usecase "Registrar Leitor" as UC5
    usecase "Gerar Relatório" as UC6
    usecase "Validar CPF" as UC7
    
    UC2 ..> UC7 : <<include>>
    UC4 --> UC3 : <<extend>>
}

Leitor --> UC1
Leitor --> UC2
Leitor --> UC3
Leitor --> UC4

Bibliotecario --> UC2
Bibliotecario --> UC3
Bibliotecario --> UC5

Admin --> UC6
Admin --> UC5

@enduml
```

### Descrevendo um Caso de Uso

Cada caso de uso deve ter uma descrição em **formato estruturado**:

#### Exemplo: Caso de Uso "Emprestar Livro"

| Atributo | Descrição |
|----------|-----------|
| **ID** | UC02 |
| **Nome** | Emprestar Livro |
| **Atores** | Leitor, Bibliotecário |
| **Pré-condição** | Leitor cadastrado; Livro disponível |
| **Fluxo Principal** | 1. Leitor solicita livro<br>2. Bibliotecário valida CPF<br>3. Sistema registra empréstimo<br>4. Sistema gera recibo |
| **Fluxo Alternativo** | Se livro indisponível: mostrar outras obras similares |
| **Pós-condição** | Empréstimo registrado; Livro marcado como indisponível |
| **Restrições** | Máximo 3 livros por leitor |

---

## 2️⃣ Diagrama de Classes

### O que é?

Um **diagrama de classes** mostra a estrutura estática do sistema, incluindo:
- **Classes** e seus atributos
- **Métodos** (operações)
- **Relacionamentos** entre classes (herança, composição, agregação)

### Elementos Principais

#### 1. Estrutura de uma Classe

```
┌─────────────────┐
│  Livro          │  ← Nome da classe
├─────────────────┤
│ - isbn: String  │  ← Atributos (dados)
│ - titulo: String│     (- privado, # protegido, + público)
│ - autor: String │
├─────────────────┤
│ + emprestar()   │  ← Métodos (comportamentos)
│ + devolver()    │
│ + renovar()     │
└─────────────────┘
```

#### 2. Modificadores de Acesso

| Símbolo | Significado | Acesso |
|---------|------------|--------|
| **+** | Público | Qualquer classe |
| **-** | Privado | Apenas a própria classe |
| **#** | Protegido | Classe e subclasses |
| **~** | Pacote | Apenas classes do mesmo pacote |

#### 3. Relacionamentos

```plantuml
@startuml Relacionamentos
skinparam classBackgroundColor #FEFCE8
skinparam classArrowColor #333333

class A {
}

class B {
}

class C {
}

class D {
}

class E {
}

class F {
}

A "1" --> "*" B : Associação
C "1" *-- "*" D : Composição (parte obrigatória)
E "1" o-- "*" F : Agregação (parte opcional)

note right of A
  Associação simples:
  A conhece B
end note

note right of C
  Composição:
  D não existe sem C
  (forte dependência)
end note

note right of E
  Agregação:
  F pode existir sem E
  (dependência fraca)
end note

@enduml
```

#### 4. Herança (Generalização)

```plantuml
@startuml Heranca
skinparam classBackgroundColor #E8F4F8
skinparam classArrowColor #333333

class Animal {
    - nome: String
    - idade: int
    --
    + fazer_som(): void
    + mover(): void
}

class Cachorro {
    - raca: String
    --
    + buscar(): void
}

class Gato {
    - cor: String
    --
    + arranhar(): void
}

Animal <|-- Cachorro
Animal <|-- Gato

note right of Animal
  Classe pai (superclasse)
  Define características comuns
end note

note right of Cachorro
  Classe filha (subclasse)
  Herda de Animal
  Adiciona características específicas
end note

@enduml
```

### Exemplo Completo: Sistema de Gerenciamento de Biblioteca

```plantuml
@startuml BibliotecaClasse
skinparam classBackgroundColor #FFFACD
skinparam classArrowColor #333333

package "Sistema de Biblioteca" {

    class Pessoa {
        - cpf: String
        - nome: String
        - email: String
        --
        + validar_email(): boolean
        + atualizar_perfil(): void
    }

    class Leitor {
        - id_leitor: int
        - endereco: String
        - telefone: String
        --
        + buscar_livro(): List<Livro>
        + emprestar_livro(): void
        + devolver_livro(): void
        + renovar_emprestimo(): void
    }

    class Bibliotecario {
        - id_funcionario: int
        - departamento: String
        --
        + registrar_leitor(): void
        + remover_leitor(): void
        + gerar_relatorio(): void
        + processar_devolvao(): void
    }

    class Livro {
        - isbn: String
        - titulo: String
        - autor: String
        - ano_publicacao: int
        - disponivel: boolean
        --
        + marcar_como_disponivel(): void
        + marcar_como_indisponivel(): void
        + obter_info(): String
    }

    class Emprestimo {
        - id_emprestimo: int
        - data_emprestimo: Date
        - data_devolucao_prevista: Date
        - data_devolucao_real: Date
        - multa: float
        --
        + calcular_multa(): float
        + renovar(): void
        + finalizar(): void
    }

    class Exemplar {
        - numero_exemplar: int
        - condicao: String
        - localizacao: String
        --
        + verificar_condicao(): String
        + atualizar_localizacao(): void
    }

    ' Relacionamentos
    Pessoa <|-- Leitor
    Pessoa <|-- Bibliotecario
    
    Leitor "1" -- "*" Emprestimo : realiza
    Livro "1" -- "*" Exemplar : contém
    Exemplar "1" -- "*" Emprestimo : sobre
    Bibliotecario "1" -- "*" Leitor : gerencia
    
    note right of Pessoa
        Classe abstrata
        Define atributos comuns
    end note

    note on link
        Um leitor pode fazer
        vários empréstimos
    end note
}

@enduml
```

### Análise da Estrutura

**O que este diagrama nos mostra:**

1. **Herança**: Leitor e Bibliotecário herdam de Pessoa
2. **Associações**:
   - Leitor realiza múltiplos Empréstimos (1 para *)
   - Livro contém múltiplos Exemplares (1 para *)
   - Exemplar participa de múltiplos Empréstimos (1 para *)
3. **Responsabilidades**:
   - Pessoa: dados pessoais
   - Leitor: buscar e emprestar livros
   - Livro: informações bibliográficas
   - Exemplar: dados físicos do livro
   - Empréstimo: controle de datas e multas

---

## 3️⃣ Exemplo Integrado: Sistema de Rede Social

### Diagrama de Caso de Uso

```plantuml
@startuml RedesSocialCasoUso
left to right direction
skinparam packageStyle rectangle

actor "Usuário" as User
actor "Administrador" as Admin

rectangle "Sistema de Rede Social" {
    usecase "Criar Conta" as UC1
    usecase "Fazer Login" as UC2
    usecase "Fazer Logout" as UC3
    usecase "Criar Postagem" as UC4
    usecase "Comentar Postagem" as UC5
    usecase "Curtir Postagem" as UC6
    usecase "Seguir Usuário" as UC7
    usecase "Bloquear Usuário" as UC8
    usecase "Validar Email" as UC9
    usecase "Enviar Notificação" as UC10
    usecase "Suspender Conta" as UC11
    usecase "Visualizar Feed" as UC12
    
    UC1 ..> UC9 : <<include>>
    UC4 ..> UC10 : <<include>>
    UC5 ..> UC10 : <<include>>
    UC6 ..> UC10 : <<include>>
    UC4 --> UC5 : <<extend>>
    UC11 --> UC3 : <<extend>>
}

User --> UC1
User --> UC2
User --> UC3
User --> UC4
User --> UC5
User --> UC6
User --> UC7
User --> UC8
User --> UC12

Admin --> UC11

@enduml
```

### Diagrama de Classes

```plantuml
@startuml RedesSocialClasse
skinparam classBackgroundColor #F0F8FF
skinparam classArrowColor #333333

class Usuario {
    - id_usuario: int
    - username: String
    - email: String
    - senha: String
    - data_criacao: Date
    - ativo: boolean
    --
    + criar_conta(): void
    + fazer_login(): boolean
    + fazer_logout(): void
    + atualizar_perfil(): void
    + bloquear_usuario(): void
    + obter_seguidores(): List<Usuario>
}

class Postagem {
    - id_postagem: int
    - conteudo: String
    - data_criacao: Date
    - quantidade_curtidas: int
    - deletada: boolean
    --
    + editar(): void
    + deletar(): void
    + obter_comentarios(): List<Comentario>
    + contar_curtidas(): int
}

class Comentario {
    - id_comentario: int
    - conteudo: String
    - data_criacao: Date
    - deletado: boolean
    --
    + editar(): void
    + deletar(): void
    + obter_resposta(): List<Comentario>
}

class Curtida {
    - id_curtida: int
    - data_criacao: Date
    - tipo: String
    --
    + remover_curtida(): void
}

class Notificacao {
    - id_notificacao: int
    - tipo: String
    - mensagem: String
    - lida: boolean
    - data_criacao: Date
    --
    + marcar_como_lida(): void
    + deletar(): void
}

' Relacionamentos
Usuario "1" -- "*" Postagem : cria
Usuario "1" -- "*" Comentario : escreve
Usuario "1" -- "*" Curtida : da
Usuario "1" -- "*" Notificacao : recebe

Postagem "1" -- "*" Comentario : contém
Postagem "1" -- "*" Curtida : recebe
Comentario "1" -- "*" Curtida : recebe

Usuario "*" -- "*" Usuario : segue

note right of Usuario
    Relacionamento reflexivo:
    Um usuário segue 
    múltiplos usuários
end note

@enduml
```

---

## 4️⃣ Padrões e Boas Práticas

### ✅ Princípios para Bom Design OOP

| Princípio | Descrição | Exemplo |
|-----------|-----------|---------|
| **SRP** (Single Responsibility) | Cada classe tem UMA responsabilidade | `Pagamento` não deve enviar email |
| **OCP** (Open/Closed) | Aberta para extensão, fechada para modificação | Usar herança ao invés de grandes `if/else` |
| **LSP** (Liskov Substitution) | Subclasses devem substituir superclasses | `Gato` deve funcionar onde `Animal` é esperado |
| **ISP** (Interface Segregation) | Muitas interfaces específicas | `Voador` separado de `Animal` |
| **DIP** (Dependency Inversion) | Depender de abstrações, não implementações | Usar `Animal` ao invés de `Cachorro` específico |

### ❌ Erros Comuns

Um diagrama de classe pode violar princípios SOLID:

**Erro: Responsabilidades Múltiplas**

```plantuml
@startuml ErroResponsabilidades
skinparam classBackgroundColor #FFE4E1

class Veiculo {
    - velocidade: float
    - combustivel: float
    - passageiros: int
    --
    + acelerar(): void
    + frear(): void
    + abrir_porta(): void
    + ligar_radio(): void
    + pagar_seguro(): void
    + fazer_manutencao(): void
    + registrar_multa(): void
}

note right of Veiculo
    ❌ ERRADO: Classe faz TUDO!
    - Movimentação
    - Entretenimento  
    - Seguros
    - Manutenção
    - Gestão legal
end note

@enduml
```

**Solução: Separar Responsabilidades**

```plantuml
@startuml CorrecaoResponsabilidades
skinparam classBackgroundColor #E8F5E9

class Veiculo {
    - velocidade: float
    --
    + acelerar(): void
    + frear(): void
}

class RadioEntretenimento {
    --
    + ligar_radio(): void
    + mudar_estacao(): void
}

class SistemaSeguro {
    --
    + calcular_premio(): float
    + cobrar_seguro(): void
}

class OficinaMecanica {
    --
    + fazer_manutencao(): void
    + diagnosticar(): void
}

Veiculo "1" -- "*" RadioEntretenimento
Veiculo "1" -- "*" SistemaSeguro
Veiculo "1" -- "*" OficinaMecanica

note right of Veiculo
    ✅ CORRETO: Cada classe
    tem UMA responsabilidade
end note

@enduml
```

---

## 5️⃣ Exercícios Práticos

### 🎯 Exercício 1: Sistema de Banco

Modele um sistema bancário com os seguintes requisitos:

**Atores:**
- Clientes
- Caixas (funcionários)
- Gerente
- Sistema Externo (BCB - Banco Central)

**Casos de Uso:**
- Criar Conta
- Depositar
- Sacar
- Transferir
- Consultar Saldo
- Solicitar Empréstimo
- Pagar Fatura

**Classes:**
- Pessoa
- Cliente
- Funcionario
- ContaBancaria
- Transacao
- Emprestimo

**Desafio:** Crie o diagrama de caso de uso e o diagrama de classes com todos os relacionamentos apropriados.

---

### 🎯 Exercício 2: Sistema de E-commerce

Analise um e-commerce real (Mercado Livre, Amazon) e modele:

1. **Diagrama de Caso de Uso** com:
   - Cliente normal
   - Vendedor
   - Administrador
   - Mínimo 10 casos de uso

2. **Diagrama de Classes** com:
   - Produto
   - Pedido
   - ItemPedido
   - Cliente
   - Carrinho
   - Avaliação
   - Pagamento
   - Entrega

---

### 🎯 Exercício 3: Refatoração de Design

Dado este diagrama **problemático**, identifique violações de SOLID e refatore:

```plantuml
@startuml ExercicioRefatoracao
skinparam classBackgroundColor #FFE4E1

class Funcionario {
    - id: int
    - nome: String
    --
    + lidar_com_vendas(): void
    + processar_boleto(): void
    + fazer_relatorio(): void
    + limpar_chao(): void
    + consertar_impressora(): void
    + responder_email(): void
    + gerir_estoq(): void
}

@enduml
```

**Questões:**
1. Quantas responsabilidades esta classe tem?
2. Qual princípio SOLID está sendo violado?
3. Refatore dividindo em múltiplas classes apropriadas

---

## 📖 Referências e Leitura Complementar

### Livros
- **"UML Destilado"** - Martin Fowler
- **"Notação e Modelagem de Processos"** - Freund & Rücker
- **"Clean Architecture"** - Robert C. Martin
- **"Design Patterns"** - Gang of Four

### Ferramentas Online
- [PlantUML Editor](http://www.plantuml.com/plantuml/uml/)
- [Lucidchart](https://www.lucidchart.com)
- [Draw.io](https://www.draw.io)
- [StarUML](http://staruml.io/)

### Documentação Oficial
- [OMG UML Specification](https://www.omg.org/spec/UML/)
- [PlantUML Documentation](https://plantuml.com)

---

## 🔑 Resumo dos Conceitos

| Conceito | Definição | Quando Usar |
|----------|-----------|-----------|
| **Caso de Uso** | Descrição de interação entre ator e sistema | Levantamento de requisitos |
| **Classe** | Molde para objetos com atributos e métodos | Design de software |
| **Herança** | Relação "é um" entre classes | Compartilhar código comum |
| **Agregação** | Relação "tem um" (fraca) | Composição opcional |
| **Composição** | Relação "parte de" (forte) | Dependência obrigatória |
| **Interface** | Contrato sem implementação | Define comportamento esperado |
| **Polimorfismo** | Mesmo método, múltiplas implementações | Flexibilidade e extensibilidade |

---

## 📝 Conclusão

A modelagem com UML é fundamental para:

✅ **Comunicação**: Visualizar ideias antes de codificar  
✅ **Documentação**: Registrar decisões de design  
✅ **Qualidade**: Identificar falhas no design cedo  
✅ **Reutilização**: Padrões e arquitetura claros  
✅ **Manutenção**: Sistema compreensível e evolutivo  

> "Um diagrama bem feito poupa mil linhas de código"

---

**Autoria:** Prof. Claudio  
**Disciplina:** Engenharia de Software / Programação Orientada a Objetos  
**Instituto:** IFB - Campus Valparaíso de Goiás  
**Licença:** CC BY-NC-SA 4.0
