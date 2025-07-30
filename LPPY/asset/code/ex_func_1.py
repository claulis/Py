def gerar_saudacao(nome, turno="manhã"):
    """Gera uma saudação personalizada com base no nome e turno do dia.

    Args:
        nome (str): Nome da pessoa.
        turno (str): Turno do dia (manhã, tarde ou noite). Padrão é 'manhã'.

    Returns:
        str: Saudação formatada.
    """
    turnos_validos = ["manhã", "tarde", "noite"]
    if turno.lower() not in turnos_validos:
        turno = "manhã"  # Volta ao padrão se inválido
    return f"Bom {turno.capitalize()}, {nome}!"

# Exemplo de uso
print(gerar_saudacao("Ana"))  # Saída: Bom Manhã, Ana!
print(gerar_saudacao("João", "tarde"))  # Saída: Bom Tarde, João!
print(gerar_saudacao("Maria", "noite"))  # Saída: Bom Noite, Maria!