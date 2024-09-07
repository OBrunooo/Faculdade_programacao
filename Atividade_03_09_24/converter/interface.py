def welcome():
    print("Bem vindo(a) ao conversor Real/Dollar")

def thanks():
    print("Obrigado por utilizar o nosso conversor de valores")

def return_cot():
    cot = float(input("Digite a cotação atual do Dollar: "))
    return cot

def option_convert():
    print("""==== Conversão ====
1- Dollar para Real
2- Real para Dollar""")
    convert= int(input("Conversão (1 ou 2): "))
    return convert

def select_value():
    value = float(input("Digite o valor: "))
    return value

def select_menu():
    menu = int(input("""
=== MENU CONVERSOR ===
1- Converter outro valor
2- Alterar o tipo de conversão
3- Finalizar o programa                    

Selecione uma opção do menu: """))
    return menu

if __name__ == "__main__":
    welcome()
    return_cot()
    option_convert()
    select_value()
    select_menu()