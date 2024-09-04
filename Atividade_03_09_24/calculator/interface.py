def welcome ():
    print("""Bem vindo(a) calculadora""")

def value1():
    value1 = float(input("Digite o primeiro valor: "))
    return value1

def value2():
    value2 = float(input("Digite o segundo valor: "))
    return value2

def menu ():
    option = (input("""==== MENU ====
Adição: +
Subtração: -
Multiplicação: X
Divisão: /   

Escolha o sua operacação:                                                                                                                     
"""))
    return option
    

if __name__ == "__main__" :
    menu()