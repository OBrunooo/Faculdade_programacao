def welcome():
    print("Bem vindo(a) ao conversor Real/Dollar")

def option():
    print("""==== Conversão ====
1- Dollar para Real
2- Real para Dollar                  
                    """)
    option= int(input("Digite qual conversão deseja fazer (1 ou 2)"))
    return option
welcome()
option()