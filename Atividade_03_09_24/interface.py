def welcome():
    print("Bem vindo ao Sistema de Programas")

def menu ():
    menu_option = int(input("""=== MENU PRINCIPAL ===
1- Calculadora
2- Conversor Dollar/Real
3- Jogo do número secreto
4- Lista de tarefas
5- Finalizar programa geral
                             
Selecione um programa: """))
    return menu_option

def thanks():
    print("Obrigado por utilizar os nossos programas !")