def test_criar_e_ler_cliente_serializa_corretamente(client):
    # Cobre a correção do bug de serialização (from_attributes ausente),
    # que antes causava erro de validação ao devolver um objeto ORM.
    resposta = client.post("/clientes", json={"nome": "Ana", "idade": 30})
    assert resposta.status_code == 201
    corpo = resposta.json()
    assert corpo["nome"] == "Ana"
    assert corpo["idade"] == 30
    assert "id" in corpo


def test_atualizar_cliente_com_idade_zero_e_aplicado(client):
    # Cobre a correção do bug "if update_data.idade:", que ignorava idade=0
    # por ser um valor falso em Python.
    criado = client.post("/clientes", json={"nome": "Bruno", "idade": 5}).json()
    resposta = client.put(f"/clientes/{criado['id']}", json={"idade": 0})
    assert resposta.status_code == 200
    assert resposta.json()["idade"] == 0


def test_criar_cliente_com_idade_negativa_e_rejeitado(client):
    resposta = client.post("/clientes", json={"nome": "Carla", "idade": -1})
    assert resposta.status_code == 422


def test_listar_clientes_respeita_paginacao(client):
    for i in range(5):
        client.post("/clientes", json={"nome": f"Cliente {i}", "idade": 20 + i})
    resposta = client.get("/clientes", params={"skip": 1, "limit": 2})
    assert resposta.status_code == 200
    assert len(resposta.json()) == 2


def test_ler_cliente_inexistente_retorna_404(client):
    resposta = client.get("/clientes/9999")
    assert resposta.status_code == 404


def test_acesso_sem_api_key_e_negado(client):
    client.headers.pop("x-api-key")
    resposta = client.get("/clientes")
    assert resposta.status_code == 401


def test_health_check_nao_exige_api_key(client):
    client.headers.pop("x-api-key")
    resposta = client.get("/health")
    assert resposta.status_code == 200
    assert resposta.json() == {"status": "ok"}
