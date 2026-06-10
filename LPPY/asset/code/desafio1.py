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

quantidade = int(input("Quantos alunos na turma? "))

for i in range(1, quantidade + 1):
    print(f"\nAluno {i}:")
    nome = input("  Nome: ")
    nota = ler_nota_valida(nome)
    turma.append({"nome": nome, "nota": nota})

gerar_relatorio(turma)
