def ler_nota_valida(nome):
    """Lê e valida uma nota entre 0 e 10."""
    while True:
        try:
            nota = float(input(f"  Nota de {nome}: "))
            if 0 <= nota <= 10:
                return nota
            print("  Nota inválida! Digite um valor entre 0 e 10.")
        except ValueError:
            print("  Entrada inválida! Digite um número.")


def classificar(nota):
    """Retorna a situação do aluno com base na nota."""
    if nota >= 7:
        return "Aprovado"
    elif nota >= 5:
        return "Recuperação"
    else:
        return "Reprovado"


def gerar_relatorio(turma):
    """Exibe o relatório completo da turma."""
    notas = [a["nota"] for a in turma]

    print("\n" + "=" * 45)
    print(f"{'Nome':<20} {'Nota':>6}  {'Situação'}")
    print("-" * 45)
    for aluno in turma:
        print(f"{aluno['nome']:<20} {aluno['nota']:>6.1f}  {classificar(aluno['nota'])}")

    print("-" * 45)
    print(f"  Média da turma : {sum(notas) / len(notas):.2f}")
    print(f"  Maior nota     : {max(notas):.1f}")
    print(f"  Menor nota     : {min(notas):.1f}")
    print("=" * 45)





# --- Programa principal ---
turma = []

while True:
    print("\n=== Gerenciador de Turma com Estatísticas ===")
    print("1. Adicionar aluno")
    print("2. Remover Aluno")
    print("3. Sair")
    opcao = int(input("\nEscolha uma opção (1-3): "))

    match opcao:
     case 1:
         nome = input("  Nome: ")
         nota = ler_nota_valida(nome)
         turma.append({"nome": nome, "nota": nota})
         gerar_relatorio(turma)

     case 2:
          if not turma:
            print("A turma está vazia!")
          else:
            print("\n--- Turma ---")
            for i in range(len(turma)):
                print(f"{i+1}. {turma[i]}")
            print("---------------")
            try:
                indice = int(input("Digite o número do aluno para remover: ")) - 1
                if 0 <= indice < len(turma):
                    aluno_removido = turma[indice]
                    turma.pop(indice)
                    print(f"Aluno '{aluno_removido}' removido com sucesso!")
                    gerar_relatorio(turma)
                else:
                    print("Número inválido!")
            except ValueError:
                print("Entrada inválida! Digite um número.")
     case 3:
           print("Saindo do programa...")
           break
     case _:
           print("Opção inválida! Tente novamente.")
