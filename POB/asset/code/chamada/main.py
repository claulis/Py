from aluno import Aluno
from professor import Professor
from turma import Turma

# Criando instâncias
aluno1 = Aluno("Ana", "2023001")
aluno2 = Aluno("Bruno", "2023002")
professor = Professor("Dr. Carlos", "P001")
turma = Turma("T101", professor)

# Matriculando alunos
print(turma.matricular_aluno(aluno1))
print(turma.matricular_aluno(aluno2))

# Registrando presenças
print(professor.registrar_presenca(aluno1, turma, "2025-07-30"))
print(professor.registrar_presenca(aluno2, turma, "2025-07-30"))
print(professor.registrar_presenca(aluno1, turma, "2025-07-31"))

# Listando frequência
print(turma.listar_frequencia())

