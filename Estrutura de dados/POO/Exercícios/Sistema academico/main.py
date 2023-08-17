from sistema import *

sistema = SistemaGestaoAcademica()

curso = sistema.cadastrar_curso("TSI", "3 anos")
professor = Docente("Thiago", 40, "")
disciplina_calculo = sistema.cadastrar_disciplina("Cálculo", professor)

aluno= Aluno("Cássia", 22, None)
sistema.matricular_aluno(aluno, curso)

curso.exibir_info()
aluno.exibir_info()


