# Arquitetura e Estrutura do Projeto MVC

Esta pasta implementa o MVC descrito em [`PDS/arquitetura.md`](/PDS/arquitetura.md#11-mvc-model-view-controller): um sistema de gerenciamento de pedidos (`Pedido`, `ItemPedido`) de uma loja online, persistido com SQLAlchemy em um arquivo SQLite local. Além dos três papéis clássicos do MVC, o projeto aplica os cinco princípios SOLID (explicados em [`solid.md`](/PDS/solid.md)) na divisão interna do que costuma ser só o "Controller": a lógica de negócio e o acesso a dados vivem em classes próprias, cada uma com uma única razão para mudar.

## Estrutura de pastas

```
mvc/
├── main.py                            # ponto de entrada
├── requirements.txt
├── config/
│   └── database.py                    # engine SQLAlchemy + fábrica de sessões
├── models/
│   ├── base.py                        # Base declarativa do SQLAlchemy
│   ├── pedido.py                      # Model: Pedido
│   └── item_pedido.py                 # Model: ItemPedido
├── views/
│   └── pedido_view.py                 # View: PedidoView
├── repositories/
│   ├── ipedido_repository.py          # Interface: IPedidoRepository (DIP)
│   └── pedido_repository.py           # Implementação: PedidoRepository (SQLAlchemy)
├── services/
│   └── pedido_service.py              # Regra de negócio: PedidoService (SRP)
└── controllers/
    └── pedido_controller.py           # Controller: só orquestra
```

`models/`, `views/` e `controllers/` são os três papéis clássicos do MVC. `repositories/` isola o acesso a dados atrás de uma interface (DIP); `services/` concentra a regra de negócio (SRP). Juntas, essas duas pastas são o que mantém o Controller magro.

## Visão geral da arquitetura

```mermaid
graph TD
    MAIN[main.py] -->|cria tabelas| BASE[Base.metadata]
    MAIN -->|instancia| REPO[PedidoRepository]
    MAIN -->|instancia| SERV[PedidoService]
    MAIN -->|instancia| CTRL[PedidoController]
    CTRL -->|delega para| SERV
    SERV -->|depende da abstração| IREPO[IPedidoRepository]
    IREPO -.implementada por.-> REPO
    REPO -->|acessa via| DB[config/database.py]
    CTRL -->|aciona| VIEW[PedidoView]
    SERV -->|valida e cria| PED[Pedido]
    PED -->|um-para-muitos, cascade| ITEM[ItemPedido]
```

O Controller não fala com o banco nem decide regra de negócio — ele recebe um `PedidoService` e uma `PedidoView` prontos (injeção de dependência) e só coordena os dois. Quem acessa o banco é `PedidoRepository`; quem decide o que é um pedido válido é `PedidoService`. Nenhuma seta liga `PedidoController` diretamente a `PedidoRepository` ou a `Pedido` — tudo passa pelo `PedidoService` no meio.

---

## As classes, uma a uma

### `Base`, `Pedido`, `ItemPedido` — `models/`

```python
# base.py
from sqlalchemy.orm import declarative_base

Base = declarative_base()
```

```python
# pedido.py
from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import relationship
from datetime import date
from .base import Base

class Pedido(Base):
    __tablename__ = 'pedido'
    id = Column(Integer, primary_key=True, autoincrement=True)
    cliente = Column(String(100))
    data_pedido = Column(Date, default=date.today)
    itens = relationship("ItemPedido", back_populates="pedido", cascade="all, delete-orphan")
```

```python
# item_pedido.py
from sqlalchemy import Column, Integer, String, ForeignKey, DECIMAL
from sqlalchemy.orm import relationship
from .base import Base

class ItemPedido(Base):
    __tablename__ = 'item_pedido'
    id = Column(Integer, primary_key=True, autoincrement=True)
    pedido_id = Column(Integer, ForeignKey('pedido.id'))
    produto = Column(String(100))
    quantidade = Column(Integer)
    preco = Column(DECIMAL(10,2))

    pedido = relationship("Pedido", back_populates="itens")
```

`Base` dá a `Pedido` e `ItemPedido` o mapeamento automático para tabelas do SQLAlchemy. `Pedido` guarda `cliente` e `data_pedido`, com `cascade="all, delete-orphan"` garantindo que apagar um pedido apaga seus itens junto. `ItemPedido` guarda `produto`, `quantidade` e `preco` (como `DECIMAL`, não `float`, para não perder precisão em dinheiro), ligado ao `Pedido` pela chave estrangeira `pedido_id`. Os Models são só estrutura de dados — não sabem calcular nada, não sabem validar nada, não sabem se persistir sozinhos.

### `PedidoView` — `views/pedido_view.py`

```python
from models.pedido import Pedido

class PedidoView:
    @staticmethod
    def exibir_pedidos(pedidos):
        for p in pedidos:
            print(f"Pedido {p.id} - Cliente: {p.cliente} - Data: {p.data_pedido}")
            for i in p.itens:
                print(f"  Produto: {i.produto}, Quantidade: {i.quantidade}, Preço: {i.preco}")

    @staticmethod
    def exibir_mensagem(mensagem):
        print(mensagem)

    @staticmethod
    def exibir_erro(erro):
        print(f"Erro: {erro}")
```

Três métodos estáticos, sem estado, cada um só formatando texto para o console. É a única classe do projeto que efetivamente lê `Pedido.itens` para exibição — nenhuma outra classe existe para mostrar dado ao usuário.

### `IPedidoRepository` — `repositories/ipedido_repository.py`

```python
from abc import ABC, abstractmethod
from typing import List
from models.pedido import Pedido

class IPedidoRepository(ABC):
    @abstractmethod
    def create(self, pedido: Pedido) -> Pedido: pass

    @abstractmethod
    def read_by_id(self, pedido_id: int) -> Pedido: pass

    @abstractmethod
    def read_all(self) -> List[Pedido]: pass

    @abstractmethod
    def update(self, pedido: Pedido) -> Pedido: pass

    @abstractmethod
    def delete(self, pedido_id: int) -> None: pass
```

Esta interface é o Princípio da Inversão de Dependência (DIP) em código: define o contrato que qualquer forma de persistir um `Pedido` precisa cumprir, sem dizer nada sobre *como*. `PedidoService`, mais abaixo, depende só deste contrato — nunca da implementação concreta.

### `PedidoRepository` — `repositories/pedido_repository.py`

```python
from sqlalchemy.exc import SQLAlchemyError
from config.database import SessionLocal
from models.pedido import Pedido
from repositories.ipedido_repository import IPedidoRepository
from typing import List

class PedidoRepository(IPedidoRepository):
    def __init__(self):
        self.db = SessionLocal()

    def create(self, pedido: Pedido) -> Pedido:
        try:
            self.db.add(pedido)
            self.db.commit()
            self.db.refresh(pedido)
            return pedido
        except SQLAlchemyError as e:
            self.db.rollback()
            raise ValueError(f"Erro ao criar pedido: {str(e)}")

    def read_by_id(self, pedido_id: int) -> Pedido:
        try:
            return self.db.get(Pedido, pedido_id)
        except SQLAlchemyError as e:
            raise ValueError(f"Erro ao ler pedido: {str(e)}")

    def read_all(self) -> List[Pedido]:
        try:
            return self.db.query(Pedido).all()
        except SQLAlchemyError as e:
            raise ValueError(f"Erro ao listar pedidos: {str(e)}")

    def update(self, pedido: Pedido) -> Pedido:
        try:
            self.db.commit()
            self.db.refresh(pedido)
            return pedido
        except SQLAlchemyError as e:
            self.db.rollback()
            raise ValueError(f"Erro ao atualizar pedido: {str(e)}")

    def delete(self, pedido_id: int) -> None:
        try:
            pedido = self.read_by_id(pedido_id)
            if not pedido:
                raise ValueError("Pedido não encontrado")
            self.db.delete(pedido)
            self.db.commit()
        except SQLAlchemyError as e:
            self.db.rollback()
            raise ValueError(f"Erro ao deletar pedido: {str(e)}")

    def close(self):
        self.db.close()
```

Esta classe concentra **toda** a conversa com o SQLAlchemy — sessão, `commit`, `rollback`, tratamento de `SQLAlchemyError` — e nada mais. É o Princípio da Responsabilidade Única (SRP) aplicado ao acesso a dados: a única razão para esta classe mudar é uma mudança na forma de persistir. Cada exceção de banco vira um `ValueError` genérico antes de sair da classe, para que o resto do projeto nunca precise importar nada do SQLAlchemy.

### `PedidoService` — `services/pedido_service.py`

```python
from datetime import date
from typing import Any, Dict, List
from models.item_pedido import ItemPedido
from models.pedido import Pedido
from repositories.ipedido_repository import IPedidoRepository

class PedidoService:
    def __init__(self, repository: IPedidoRepository):
        self.repository = repository

    def create_pedido(self, cliente: str, itens_data: List[Dict[str, Any]]) -> Pedido:
        if not cliente:
            raise ValueError("Cliente é obrigatório")
        if not itens_data:
            raise ValueError("Pelo menos um item é obrigatório")

        pedido = Pedido(cliente=cliente)
        pedido.itens = [ItemPedido(**item) for item in itens_data]
        return self.repository.create(pedido)

    def read_pedido_by_id(self, pedido_id: int) -> Pedido:
        pedido = self.repository.read_by_id(pedido_id)
        if not pedido:
            raise ValueError("Pedido não encontrado")
        return pedido

    def read_all_pedidos(self) -> List[Pedido]:
        return self.repository.read_all()

    def update_pedido(self, pedido_id: int, novo_cliente: str = None, nova_data: date = None) -> Pedido:
        pedido = self.read_pedido_by_id(pedido_id)
        if novo_cliente:
            pedido.cliente = novo_cliente
        if nova_data:
            pedido.data_pedido = nova_data
        return self.repository.update(pedido)

    def delete_pedido(self, pedido_id: int) -> None:
        self.repository.delete(pedido_id)
```

É aqui que mora a regra de negócio: um pedido precisa de um `cliente` e de pelo menos um item para existir (`create_pedido`); uma atualização só troca o que foi de fato informado (`update_pedido`); buscar um pedido inexistente é um erro (`read_pedido_by_id`). O construtor recebe `repository: IPedidoRepository`, não `PedidoRepository` — essa assinatura é o DIP inteiro: o módulo de alto nível (a regra de negócio) depende de uma abstração, não de uma implementação concreta amarrada ao SQLAlchemy.

### `PedidoController` — `controllers/pedido_controller.py`

```python
from datetime import date
from typing import Any, Dict, List
from services.pedido_service import PedidoService
from views.pedido_view import PedidoView

class PedidoController:
    def __init__(self, service: PedidoService, view: PedidoView):
        self.service = service
        self.view = view

    def criar_e_salvar_pedido(self, cliente: str, itens_data: List[Dict[str, Any]]):
        try:
            pedido = self.service.create_pedido(cliente, itens_data)
            self.view.exibir_mensagem("Pedido salvo com sucesso!")
            return pedido
        except ValueError as e:
            self.view.exibir_erro(str(e))

    def atualizar_e_exibir_pedido(self, pedido_id: int, novo_cliente: str = None, nova_data: date = None):
        try:
            pedido = self.service.update_pedido(pedido_id, novo_cliente, nova_data)
            self.view.exibir_mensagem("Pedido atualizado com sucesso!")
            self.view.exibir_pedidos([pedido])
        except ValueError as e:
            self.view.exibir_erro(str(e))

    def deletar_e_exibir(self, pedido_id: int):
        try:
            self.service.delete_pedido(pedido_id)
            self.view.exibir_mensagem("Pedido deletado com sucesso!")
        except ValueError as e:
            self.view.exibir_erro(str(e))

    def listar_e_exibir(self):
        try:
            pedidos = self.service.read_all_pedidos()
            self.view.exibir_pedidos(pedidos)
        except ValueError as e:
            self.view.exibir_erro(str(e))
```

Não há nenhuma linha de SQLAlchemy, nenhum `commit`, nenhuma regra de negócio aqui. Cada método faz exatamente uma coisa: chama o `PedidoService`, e usa o resultado ou a exceção `ValueError` para decidir o que mandar a `PedidoView` exibir. A única razão para esta classe mudar é uma mudança em *como o resultado deve ser comunicado ao usuário*, não em como ele é calculado ou persistido.

### Configuração — `config/database.py`

```python
import logging
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

logging.getLogger('sqlalchemy.engine').setLevel(logging.WARNING)

DATABASE_URL = "sqlite:///db_pedidos.db"

engine = create_engine(DATABASE_URL, echo=False, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(bind=engine)
```

Um arquivo SQLite local, criado automaticamente na primeira execução, sem exigir nenhuma instalação externa. Não usa `isolation_level="AUTOCOMMIT"`: com autocommit, cada instrução seria persistida assim que executada, e os `rollback()` dentro de `PedidoRepository` não teriam mais nada para desfazer.

### Ponto de entrada — `main.py`

```python
from models.base import Base
from config.database import engine
from repositories.pedido_repository import PedidoRepository
from services.pedido_service import PedidoService
from views.pedido_view import PedidoView
from controllers.pedido_controller import PedidoController

Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    repository = PedidoRepository()
    service = PedidoService(repository)
    view = PedidoView()
    controller = PedidoController(service, view)

    itens_data = [
        {'produto': 'Smartphone', 'quantidade': 1, 'preco': 1500.00},
        {'produto': 'Capinha', 'quantidade': 1, 'preco': 50.00}
    ]
    controller.criar_e_salvar_pedido('Ana Paula', itens_data)

    controller.deletar_e_exibir(18)  # ID de exemplo; ajuste conforme necessário

    controller.listar_e_exibir()

    repository.close()
```

`Base.metadata.create_all(bind=engine)` cria as tabelas no SQLite se elas ainda não existirem. O bloco principal monta a cadeia de dependências à mão — `PedidoRepository` é injetado em `PedidoService`, que é injetado (junto com `PedidoView`) em `PedidoController` — e então demonstra o ciclo completo: criar um pedido, tentar deletar um que provavelmente não existe (para mostrar o caminho de erro), listar tudo, e fechar a sessão do repositório.

---

## Como os princípios SOLID aparecem aqui

**SRP** — `PedidoRepository` só persiste, `PedidoService` só decide regra de negócio, `PedidoController` só orquestra entrada e saída. Cada classe tem uma única razão para mudar, e essa razão está no nome da pasta onde ela mora.

**DIP** — `PedidoService.__init__` recebe `repository: IPedidoRepository`, não `PedidoRepository`. O módulo de alto nível (a regra de negócio) não depende do módulo de baixo nível (o SQLAlchemy); os dois dependem da abstração `IPedidoRepository`.

Os outros três aparecem de forma mais discreta: **OCP**, porque adicionar uma segunda implementação de `IPedidoRepository` (um repositório em memória, por exemplo) não exige modificar `PedidoService`; **LSP**, porque qualquer implementação de `IPedidoRepository` pode substituir `PedidoRepository` sem quebrar `PedidoService`; **ISP** não tem um exemplo dedicado aqui, porque `IPedidoRepository` já nasce pequena — os cinco métodos que ela declara são os únicos que qualquer consumidor de fato usa.

---

## Este projeto e o Django

Django resolveria boa parte desse mesmo problema com bem menos código — e é justamente o que ele deixa de fora que este projeto torna visível. Em [`PDS/arquitetura.md`](/PDS/arquitetura.md) isso é explicado em profundidade; aqui, ponto a ponto, com as classes desta pasta como referência:

`Pedido` e `ItemPedido`, em Django, seriam um `models.Model` com `.save()` e `.objects.filter()` prontos — o padrão Active Record. O papel que aqui pertence a `PedidoRepository` estaria fundido dentro do próprio Model; não existiria uma classe separada cuidando só de persistência, porque o Django não pede uma.

`IPedidoRepository` e `PedidoRepository` não têm equivalente pronto no framework. O Django não oferece Repository Pattern nativamente — quem quer essa separação entre domínio e persistência precisa construí-la à mão, exatamente como foi feito nesta pasta.

`PedidoService` também não é nativo do Django. A convenção oficial do framework é *fat models, thin views*: a regra de negócio normalmente entra direto no Model ou na View. Uma camada de serviço explícita como esta é uma escolha de arquitetura que um projeto Django adota por conta própria quando cresce o suficiente para justificar o isolamento.

`PedidoController` corresponde ao que Django chama de `views.py` — que, apesar do nome, ocupa o papel de Controller do MVC clássico, não o de View. `PedidoView` corresponde aos templates.

Ou seja: esta pasta implementa, com Python puro e SQLAlchemy, o que o Django exigiria construir manualmente caso um projeto real precisasse da mesma separação entre regra de negócio e acesso a dados.

## Como executar o exemplo completo

```bash
cd PDS/mvc
pip install -r requirements.txt
python main.py
```
