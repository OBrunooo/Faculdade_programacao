def quadrado ():
    ok_values = False
    while(ok_values == False) :
        try:
            print("Vamos calular a área do quadrado \n")
            base = float(input("Digite a base do quadrado (em cm): "))
            area = (base*base)
            ok_values = True
            return area
        except: 
            print("valor digitado incorreto")
            ok_values = False
    