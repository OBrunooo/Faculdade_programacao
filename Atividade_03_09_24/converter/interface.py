def welcome():
    print("Bem vindo(a) ao conversor Real/Dollar")

def thanks():
    print("Obrigado por utilizar o nosso conversor de valores")

def cot():
    cot = float(input("Digite a cotação atual do Dollar: "))
    return cot

def convert():
    print("""==== Conversão ====
1- Dollar para Real
2- Real para Dollar""")
    convert= int(input("Conversão (1 ou 2): "))
    return convert

def value():
    value = float(input("Digite o valor: "))
    return value

def menu():
    menu = int(input("""
=== MENU ===
1- Converter outro valor
2- Alterar o tipo de conversão
3- Finalizar o programa                    

Selecione uma opção do menu: """))
    return menu

if __name__ == "__main__":
    welcome()
    cot()
    convert()
    value()
    menu()