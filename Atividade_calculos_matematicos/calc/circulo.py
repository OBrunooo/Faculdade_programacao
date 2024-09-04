def circle ():
    ok_values = False
    while ok_values == False :
        try:
            print("Vamos calular a área do circulo \n")
            radius = float(input("Digite o raio do circulo (em cm): "))
            area = (radius*radius)*3.14159265359
            ok_values = True
            return area
        except: 
            print("valor digitado incorreto")
            ok_values =  False

        