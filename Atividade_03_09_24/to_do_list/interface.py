def welcome():
    print("Bem vindo(a) a lista de tarefas")

def thanks():
    print("obrigado por utilizar o nosso sistema de lista de tarefas !")

def menu():
    option_menu = int(input("""=== MENU ===
1- Adicionar tarefa                            
2- Mostrar lista
3- Retirar tarefa
4- Reiniciar lista                            
5- Finalizar programa
Selecione: """))
    return option_menu

def add_task ():
    task = str(input("Digite a tarefa que deseja adicioanar a sua lista: "))
    return task

def show_list(list):
    print("--- LISTA ---")
    if list == []:
        print ('Você não adicionou item a sua lista !!!')
    else:
        for i in range (len(list)):
            print(f"{i+1}- {list[i]}")

def remove_task():
    remove = int(input("Digite o número da tarefa que deseja retirar: "))
    return remove