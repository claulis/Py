class Turma:
    def __init__(self, codigo, professor):
        self.codigo = codigo
        self.professor = professor
        self.alunos = []  # Lista para armazenar alunos


    def atualizar_professor(self,novo_professor):
        prof_antigo = self.professor
        self.professor=novo_professor
        return f"O prof antigo é {prof_antigo.nome} e o atual é {self.professor.nome}"

    def matricular_aluno(self, aluno):
        if aluno not in self.alunos:
            self.alunos.append(aluno)
            return f"Aluno {aluno.nome} matriculado na turma {self.codigo}."
        return f"Aluno {aluno.nome} já está matriculado na turma {self.codigo}."

    def listar_frequencia(self):
        resultado = f"Frequência da turma {self.codigo}:\n"
        for aluno in self.alunos:
            resultado += aluno.consultar_frequencia() + "\n"
        return resultado