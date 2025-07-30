def adicionar_item_compras(lista, item, categoria="Alimentos"):
    """Adiciona um item à lista de compras com uma categoria.

    Args:
        lista (list): Lista de dicionários contendo itens.
        item (str): Nome do item.
        categoria (str): Categoria do item (padrão é 'Alimentos').

    Returns:
        None
    """
    lista.append({"item": item, "categoria": categoria})
    print(f"Item '{item}' adicionado na categoria {categoria}.")

def exibir_lista_compras(lista):
    """Exibe os itens da lista de compras numerados.

    Args:
        lista (list): Lista de dicionários contendo itens.

    Returns:
        None
    """
    if not lista:
        print("A lista de compras está vazia!")
        return
    print("\n--- Lista de Compras ---")
    for i, entrada in enumerate(lista, 1):
        print(f"{i}. {entrada['item']} ({entrada['categoria']})")
    print("-----------------------")

# Exemplo de uso
lista_compras = []
adicionar_item_compras(lista_compras, "Arroz")
adicionar_item_compras(lista_compras, "Sabão", "Limpeza")
exibir_lista_compras(lista_compras)