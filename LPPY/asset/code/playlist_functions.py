# Lista para armazenar as músicas
playlist = []

def display_menu():
    print("\n=== Gerenciador de Playlist ===")
    print("1. Adicionar música")
    print("2. Listar músicas")
    print("3. Atualizar música")
    print("4. Remover música")
    print("5. Sair")
    return input("Escolha uma opção (1-5): ")

def add_song(playlist):
    nome = input("Digite o nome da música: ")
    artista = input("Digite o nome do artista: ")
    duracao = input("Digite a duração da música (ex: 3:30): ")
    musica = [nome, artista, duracao]
    playlist.append(musica)
    print(f"Música '{nome}' de {artista} adicionada com sucesso!")

def list_songs(playlist):
    if not playlist:
        print("A playlist está vazia!")
    else:
        print("\n--- Playlist ---")
        for i, song in enumerate(playlist, 1):
            print(f"{i}. {song[0]} - {song[1]} ({song[2]})")
        print("---------------")

def update_song(playlist):
    if not playlist:
        print("A playlist está vazia!")
        return
    list_songs(playlist)
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

def remove_song(playlist):
    if not playlist:
        print("A playlist está vazia!")
        return
    list_songs(playlist)
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

while True:
    opcao = display_menu()
    
    if opcao == '1':
        add_song(playlist)
    elif opcao == '2':
        list_songs(playlist)
    elif opcao == '3':
        update_song(playlist)
    elif opcao == '4':
        remove_song(playlist)
    elif opcao == '5':
        print("Saindo do programa...")
        break
    else:
        print("Opção inválida! Tente novamente.")