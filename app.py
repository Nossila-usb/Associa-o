from modulo import *

if __name__ == "__main__":
    aluno1 = Aluno('','','')

    aluno1.nome = input('Informe o nome do aluno: ')
    aluno1.matricula = input('Informe a matricula do aluno: ')
    aluno1.cpf = input('Informe o CPF do aluno: ')
    
    aluno2 = Aluno('','','')

    aluno2.nome = input('Imforme o nome 2º aluno: ')
    aluno2.matricula = input('Imforme a matricula 2º aluno: ')
    aluno2.cpf = input('Imforme o CPF do 2º aluno: ')
   
    
    # instancia o curso
    curso1 = Curso('',0,'')

    

    curso1.nome = input('Informe o nome do curso: ')
    curso1.duracao = int(input('Informe a duracao do curso: '))
    curso1.turno = input('Informe o turno do curso: ')

    # curso 2
    curso2 = Curso('',0,'')

    curso2.nome = input('Informe o nome 2º curso: ')
    curso2.duracao = int(input('Informe a duracao 2º curso: '))
    curso2.turno = input('Informe o turno 2º curso: ')
    
    # cadastrando os alunos instanciados no curso instanciado
    aluno1.increver_curso(curso1)
    aluno1.increver_curso(curso2)
    aluno2.increver_curso(curso1)

    # saida de dados 
    print('\n')
    print(f'Aluno {aluno1.nome} de matricula {aluno1.matricula} esta inscrito no curso {aluno1.lista_curso()}.')
    print(f'Aluno {aluno2.nome} de matricula {aluno2.matricula} esta inscrito no curso {aluno2.lista_curso()}.')
    print(f'No curso {curso1.nome} estao matriculados os alunos: {curso1.listar_alunos()}.')
    print(f'No curso {curso2.nome} estao matriculados os alunos: {curso2.listar_alunos()}.')

