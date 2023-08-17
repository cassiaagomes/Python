#Exercício
''' Apresente um modelo de classes para representar um abstração de alto nível de
um Sistema de Gestão Acadêmica. O Sistema deve permitir que sejam
cadastrados os cursos, disciplinas e docentes. Alunos são matriculados por curso.
No início do semestre, disciplinas são ofertadas por curso. Os alunos se matriculam nas
disciplina. Há um professor alocado para cada disciplina'''

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

class Docente(Pessoa):
    def __init__(self, nome, idade, area):
        super().__init__(nome, idade)
        self.area = area

class Curso:
    def __init__(self, nome, duracao):
        self.nome = nome
        self.duracao = duracao
        self.disciplinas = []
        self.alunos = []

    def exibir_info(self):
        print(f"Curso: {self.nome}")
        print(f"Duração: {self.duracao}")
        print("Disciplinas:")
        for disciplina in self.disciplinas:
            print(f" - {disciplina.nome}")


class Disciplina:
    def __init__(self, nome, professor):
        self.nome = nome
        self.professor = professor
        self.alunos = []

class Aluno(Pessoa):
    def __init__(self, nome, idade, curso):
        super().__init__(nome, idade)
        self.curso = curso
    
    def exibir_info(self):
        print(f"Aluno: {self.nome}")
        print(f"Idade: {self.idade}")
        if self.curso:
            print(f"Curso: {self.curso.nome}")
        else:
            print("Curso: Não matriculado em nenhum curso")

class SistemaGestaoAcademica:
    def __init__(self):
        self.cursos = []
        self.alunos = []
        self.docentes = []

    def cadastrar_curso(self, nome, duracao):
        curso = Curso(nome, duracao)
        self.cursos.append(curso)
        return curso

    def cadastrar_disciplina(self, nome, professor):
        disciplina = Disciplina(nome, professor)
        professor.area = nome
        professor.disciplina = disciplina
        return disciplina

    def matricular_aluno(self, aluno, curso):
        aluno.curso = curso
        curso.alunos.append(aluno)



