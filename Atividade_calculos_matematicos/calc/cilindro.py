def cylinder ():
    ok_values = False
    while ok_values == False :
        try:
            print("Vamos calular o volume do cilindro \n")
            raio = float(input("Digite o raio do cilindro (em cm): "))
            height = float(input("Digite a altura do cilindro (em cm): "))
            volume = (raio*raio)*3.14159265359*height
            ok_values = True
            return volume
        except: 
            print("valor digitado incorreto")
            ok_values = False
