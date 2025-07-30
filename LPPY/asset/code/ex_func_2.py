def calcular_preco_com_desconto(preco, desconto):
    """Calcula o preço final de um produto após aplicar um desconto.

    Args:
        preco (float): Preço original do produto.
        desconto (float): Percentual de desconto (0 a 100).

    Returns:
        float: Preço com desconto aplicado.

    Raises:
        ValueError: Se o desconto for inválido.
    """
    if not 0 <= desconto <= 100:
        raise ValueError("Desconto deve estar entre 0 e 100.")
    if preco < 0:
        raise ValueError("Preço não pode ser negativo.")
    return preco * (1 - desconto / 100)

# Exemplo de uso
try:
    print(calcular_preco_com_desconto(100.00, 20))  # Saída: 80.0
    print(calcular_preco_com_desconto(50.00, 10))  # Saída: 45.0
    print(calcular_preco_com_desconto(100.00, 150))  # Levanta erro
except ValueError as e:
    print(f"Erro: {e}")