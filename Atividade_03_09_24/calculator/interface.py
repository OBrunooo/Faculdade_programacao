def welcome ():
    print("""Bem vindo(a) calculadora""")

def thanks():
    print("Obrigado por utilizar a nossa calculadora !")

def value1():
    value1 = float(input("Digite o primeiro valor: "))
    return value1

def value2():
    value2 = float(input("Digite o segundo valor: "))
    return value2

def operator ():
    option = (input("""==== Operação ====
Adição: +
Subtração: -
Multiplicação: X
Divisão: /   

Escolha o sua operacação:                                                                                                                     
"""))
    return option

def menu ():
    select_menu = int(input("""=== MENU CALCULADORA === 
1- Fazer outra conta
2- Alterar a operação
3- Finalizar programa
"""))
    return select_menu

if __name__ == "__main__" :
    menu()