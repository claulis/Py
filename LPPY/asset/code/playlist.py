# Lista para armazenar as músicas (cada música é uma lista com [nome, artista, duração])
playlist = []

while True:
    print("\n=== Gerenciador de Playlist ===")
    print("1. Adicionar música")
    print("2. Listar músicas")
    print("3. Atualizar música")
    print("4. Remover música")
    print("5. Sair")
    
    opcao = input("Escolha uma opção (1-5): ")
    
    # Adicionar música
    if opcao == '1':
        nome = input("Digite o nome da música: ")
        artista = input("Digite o nome do artista: ")
        duracao = input("Digite a duração da música (ex: 3:30): ")
        musica = [nome, artista, duracao]
        playlist.append(musica)
        print(f"Música '{nome}' de {artista} adicionada com sucesso!")
    
    # Listar músicas
    elif opcao == '2':
        if not playlist: #se o objeto não tiver com elementos
            print("A playlist está vazia!")
        else:
            print("\n--- Playlist ---")
            for i in range(len(playlist)):# de 0 até tamanho do array
                print(f"{i+1}. {playlist[i][0]} - {playlist[i][1]} ({playlist[i][2]})")
            print("---------------")
    
    # Atualizar música
    elif opcao == '3':
        if not playlist:
            print("A playlist está vazia!")
        else:
            print("\n--- Playlist ---")
            for i in range(len(playlist)):
                print(f"{i+1}. {playlist[i][0]} - {playlist[i][1]} ({playlist[i][2]})")
            print("---------------")
            try:
                indice = int(input("Digite o número da música para atualizar: ")) - 1
                if 0 <= indice < len(playlist):
                    nome = input("Novo nome da música (deixe vazio para manter): ")
                    artista = input("Novo artista (deixe vazio para manter): ")
                    duracao = input("Nova duração (deixe vazio para manter): ")
                    
                    if nome:
                        playlist[indice][0] = nome
                    if artista:
                        playlist[indice][1] = artista
                    if duracao:
                        playlist[indice][2] = duracao
                    print("Música atualizada com sucesso!")
                else:
                    print("Número inválido!")
            except ValueError:
                print("Entrada inválida! Digite um número.")
    
    # Remover música
    elif opcao == '4':
        if not playlist:
            print("A playlist está vazia!")
        else:
            print("\n--- Playlist ---")
            for i in range(len(playlist)):
                print(f"{i+1}. {playlist[i][0]} - {playlist[i][1]} ({playlist[i][2]})")
            print("---------------")
            try:
                indice = int(input("Digite o número da música para remover: ")) - 1
                if 0 <= indice < len(playlist):
                    musica_removida = playlist[indice][0]
                    playlist.pop(indice)
                    print(f"Música '{musica_removida}' removida com sucesso!")
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