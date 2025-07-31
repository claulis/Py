class Professor:
    def __init__(self, nome, id_professor):
        self.nome = nome
        self.id_professor = id_professor

    def registrar_presenca(self, aluno, turma, data):
        if aluno in turma.alunos:
            return aluno.adicionar_presenca(data)
        return f"Aluno {aluno.nome} não está matriculado na turma {turma.codigo}."