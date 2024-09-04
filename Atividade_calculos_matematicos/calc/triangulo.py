def triangle ():
    ok_values = False
    while(ok_values == False) :
        try:
            print("Vamos calular a área do triângulo \n")
            base = float(input("Digite a base do triângulo (em cm): "))
            height = float(input("Digite a altura do triângulo (em cm): "))
            area = (base*height)/2
            ok_values = True
            return area
        except: 
            print("valor digitado incorreto")
            ok_values = False
