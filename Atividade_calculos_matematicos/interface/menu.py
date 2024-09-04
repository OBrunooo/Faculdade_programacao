def menu ():
    ok_values = False
    while ok_values == False :
        try:
            print("""---- MENU ----
1- Área do triângulo
2- Perímetro do retângulo
3- Área do circulo
4- Volume do cilíndro 
5- Finalizar programa                 
        """)
            option = int(input("Escolha uma das opções para calcular: "))
            ok_values = True
            return option
        except: 
            print("valor digitado incorreto")
            ok_values = False