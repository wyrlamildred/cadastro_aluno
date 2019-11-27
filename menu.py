from menu import menu
from diario import diario 
def menu (): 
    print ('Menu:') 
    print ('   1 - Matricular aluno') 
    print ('   2 - Remover matricula') 
    print ('   3 - Lancar notas') 
    print ('   4 - Lancar faltas') 
    print ('   5 - Listar alunos matriculados') 
    print ('   6 - Verificar situaçao de alunos')
    print ('   7 - Ver o Diario')
    print ('   9 - Sair') 
    opt = input('Digite a opcao desejada: ') 
    return opt 
