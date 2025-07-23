def exibir_saudacao():
    print("Bem-vindo ao sistema!")
exibir_saudacao()  # Saída: Bem-vindo ao sistema!

def saudacao_personalizada(nome):
    print(f"Olá, {nome}!")
saudacao_personalizada("Alice")  # Saída: Olá, Alice!

def calcular_quadrado(numero):
    return numero * numero
resultado = calcular_quadrado(5)
print(resultado)  # Saída: 25

def saudacao_com_horario(nome, horario="dia"):
    if not horario: 
         print(f"Bom {horario}, {nome}!")
    else:
       print(f"Boa {horario}, {nome}!")
saudacao_com_horario("Bob")  # Saída: Bom manhã, Bob!
saudacao_com_horario("Bob", "tarde")  # Saída: Bom tarde, Bob!

def somar_varios(*numeros):
    return sum(numeros)
print(somar_varios(1, 2, 3))  # Saída: 6
print(somar_varios(1, 2, 3, 4, 5))  # Saída: 15

def exibir_informacoes(**kwargs):
    for chave, valor in kwargs.items():
        print(f"{chave}: {valor}")
exibir_informacoes(nome="Carlos", idade=30)  # Saída: nome: Carlos \n idade: 30

dobrar = lambda *x: sum(x)
print(dobrar(10,20,30))  # Saída: 20