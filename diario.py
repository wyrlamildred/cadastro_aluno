from menu import menu
from diario import diario 

def le_diario (): 
    print(ldiario) 
    pass 
  
def salva_diario (): 
    salvar=input("Deseja salvar o diario:")
    if salvar==sim:
        print("Diario Salvo") 
    else:
        salvar==não
        print("Diario não Salvo")
    pass 
  
le_diario() 
opcao = menu() 
while opcao != '9': 
    if opcao == '1': 
        adicionar_matricula() 
    elif opcao == '2':  
        remover_matricula() 
    elif opcao == '3':  
        lancar_notas() 
    elif opcao == '4':  
        lancar_faltas() 
    elif opcao == '5':  
        listar_alunos() 
    elif opcao == '6':  
        verificar_situacao()
    elif opcao == '7':
        le_diario()
 
  
    opcao = menu() 
  
salva_diario()

def diario ()
arquivo = open('diario.txt', 'w')
arquivo.write('Este texto será gravado!')
arquivo. readlines()  
print (diario) 
arquivo.close()