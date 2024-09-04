def rectangle ():
    ok_values = False
    while(ok_values == False) :
        try:
            print("Vamos o perimetro do retângulo \n")
            base = float(input("Digite a base do retângulo (em cm): "))
            high = float(input("Digite a base do retângulo (em cm): "))
            perimeter = (base*2)+(high*2)
            ok_values = True
            return perimeter
        except: 
            print("valor digitado incorreto")
            ok_values = False