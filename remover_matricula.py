def remover_matricula (): 
    aluno=str(input("Digite o nome do aluno:"))
    aluno=aluno.upper()
    if aluno in laluno:
        laluno.remove(aluno) 
        print('Aluno Removido')
    else:
        print('Esse Aluno Não Está Matriculado') 
    pass 