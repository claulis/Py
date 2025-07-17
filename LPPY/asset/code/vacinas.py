# Conjunto para armazenar vacinas ativas (mutável)
vacinas_ativas = set()
# Conjunto para armazenar vacinas arquivadas (imutável)
vacinas_arquivadas = frozenset()

while True:
    print("\n=== Gerenciador de Vacinas ===")
    print("1. Adicionar vacina")
    print("2. Listar vacinas")
    print("3. Atualizar vacina")
    print("4. Arquivar vacina")
    print("5. Sair")
    
    opcao = input("Escolha uma opção (1-5): ")
    
    # Adicionar vacina
    if opcao == '1':
        nome = input("Digite o nome da vacina: ")
        fabricante = input("Digite o fabricante: ")
        lote = input("Digite o lote (ex: V001): ")
        # Validação do lote (deve começar com 'V' seguido de números)
        if lote.startswith('V') and lote[1:].isdigit():
            vacina = (nome, fabricante, lote)
            if vacina not in vacinas_ativas:
                vacinas_ativas.add(vacina)
                print(f"Vacina '{nome}' adicionada com sucesso!")
            else:
                print("Erro: Vacina já existe no conjunto de vacinas ativas!")
        else:
            print("Erro: Lote deve começar com 'V' seguido de números (ex: V001)!")
    
    # Listar vacinas
    elif opcao == '2':
        if not vacinas_ativas and not vacinas_arquivadas:
            print("Nenhuma vacina registrada!")
        else:
            print("\n--- Lista de Vacinas ---")
            contador = 1
            # Listar vacinas ativas
            for vacina in vacinas_ativas:
                print(f"{contador}. [Ativa] {vacina[0]} - {vacina[1]} ({vacina[2]})")
                contador += 1
            # Listar vacinas arquivadas
            for vacina in vacinas_arquivadas:
                print(f"{contador}. [Arquivada] {vacina[0]} - {vacina[1]} ({vacina[2]})")
                contador += 1
            print("-----------------------")
    
    # Atualizar vacina
    elif opcao == '3':
        if not vacinas_ativas:
            print("Nenhuma vacina ativa para atualizar!")
        else:
            print("\n--- Vacinas Ativas ---")
            contador = 1
            lista_temp = list(vacinas_ativas)
            for vacina in lista_temp:
                print(f"{contador}. {vacina[0]} - {vacina[1]} ({vacina[2]})")
                contador += 1
            print("----------------------")
            try:
                indice = int(input("Digite o número da vacina para atualizar: ")) - 1
                if 0 <= indice < len(lista_temp):
                    vacina_antiga = lista_temp[indice]
                    nome = input("Novo nome da vacina (deixe vazio para manter): ")
                    fabricante = input("Novo fabricante (deixe vazio para manter): ")
                    lote = input("Novo lote (deixe vazio para manter, ex: V001): ")
                    
                    # Validação do lote se fornecido
                    if lote and not (lote.startswith('V') and lote[1:].isdigit()):
                        print("Erro: Lote deve começar com 'V' seguido de números (ex: V001)!")
                        continue
                    
                    # Manter valores antigos se não fornecidos
                    novo_nome = nome if nome else vacina_antiga[0]
                    novo_fabricante = fabricante if fabricante else vacina_antiga[1]
                    novo_lote = lote if lote else vacina_antiga[2]
                    
                    nova_vacina = (novo_nome, novo_fabricante, novo_lote)
                    if nova_vacina not in vacinas_ativas:
                        vacinas_ativas.discard(vacina_antiga)
                        vacinas_ativas.add(nova_vacina)
                        print("Vacina atualizada com sucesso!")
                    else:
                        print("Erro: A nova vacina já existe no conjunto de vacinas ativas!")
                else:
                    print("Número inválido!")
            except ValueError:
                print("Entrada inválida! Digite um número.")
    
    # Arquivar vacina
    elif opcao == '4':
        if not vacinas_ativas:
            print("Nenhuma vacina ativa para arquivar!")
        else:
            print("\n--- Vacinas Ativas ---")
            contador = 1
            lista_temp = list(vacinas_ativas)
            for vacina in lista_temp:
                print(f"{contador}. {vacina[0]} - {vacina[1]} ({vacina[2]})")
                contador += 1
            print("----------------------")
            try:
                indice = int(input("Digite o número da vacina para arquivar: ")) - 1
                if 0 <= indice < len(lista_temp):
                    vacina = lista_temp[indice]
                    vacinas_ativas.discard(vacina)
                    # Criar um novo frozenset com a vacina arquivada
                    vacinas_arquivadas = frozenset(list(vacinas_arquivadas) + [vacina])
                    print(f"Vacina '{vacina[0]}' arquivada com sucesso!")
                else:
                    print("Número inválido!")
            except ValueError:
                print("Entrada inválida! Digite um número.")
    
    # Sair
    elif opcao == '5':
        print("Saindo do programa...")
        break
    
    else:
        print("Opção inválida! Tente novamente.")