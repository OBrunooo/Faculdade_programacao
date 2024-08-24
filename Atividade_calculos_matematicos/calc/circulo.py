def circulo ():
    ok_values = False
    while ok_values == False :
        try:
            print("Vamos calular a área do circulo \n")
            raio = float(input("Digite o raio do circulo (em cm): "))
            area = (raio*raio)*3.14159265359
            ok_values = True
            return area
        except: 
            print("valor digitado incorreto")
            ok_values =  False

        