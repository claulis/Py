def _payload_pedido():
    return {
        "cliente": "Empresa X",
        "itens": [
            {"produto": "Teclado", "quantidade": 2, "preco": 150.0},
            {"produto": "Mouse", "quantidade": 1, "preco": 80.5},
        ],
    }


def test_criar_e_ler_pedido_serializa_itens_corretamente(client):
    # Cobre a correção do bug de serialização (from_attributes ausente) para
    # o schema aninhado PedidoOutSchema -> ItemPedidoOutSchema.
    resposta = client.post("/pedidos", json=_payload_pedido())
    assert resposta.status_code == 201
    corpo = resposta.json()
    assert corpo["cliente"] == "Empresa X"
    assert len(corpo["itens"]) == 2
    assert corpo["itens"][0]["produto"] == "Teclado"


def test_criar_pedido_sem_itens_e_rejeitado(client):
    resposta = client.post("/pedidos", json={"cliente": "Empresa Y", "itens": []})
    assert resposta.status_code == 400


def test_atualizar_pedido_substitui_itens(client):
    # Cobre a melhoria que permite atualizar os itens de um pedido existente.
    criado = client.post("/pedidos", json=_payload_pedido()).json()
    resposta = client.put(
        f"/pedidos/{criado['id']}",
        json={"itens": [{"produto": "Monitor", "quantidade": 1, "preco": 900.0}]},
    )
    assert resposta.status_code == 200
    corpo = resposta.json()
    assert len(corpo["itens"]) == 1
    assert corpo["itens"][0]["produto"] == "Monitor"


def test_deletar_pedido_inexistente_retorna_404(client):
    resposta = client.delete("/pedidos/9999")
    assert resposta.status_code == 404


def test_listar_pedidos_respeita_paginacao(client):
    for _ in range(3):
        client.post("/pedidos", json=_payload_pedido())
    resposta = client.get("/pedidos", params={"skip": 0, "limit": 2})
    assert resposta.status_code == 200
    assert len(resposta.json()) == 2
