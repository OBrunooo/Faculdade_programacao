print ("Bem-vindo a UNESC Saúde \n")
nome_do_paciente =  str(input ("Digite o seu nome: \n"))
altura_do_paciente = int(input("Digite o seu altura em cm: \n"))
peso_do_paciente = float(input("Digite o seu peso: \n"))
idade_do_paciente = int(input("Digite o sua idade: \n"))
sexo = str(input("""Digite o seu sexo
1- Masculino
2- Feminino 
"""))
continue_menu = True

# Função para retornar ao menu principal
def retorna_menu () :
    escolha_menu = input("Deseja retornar ao menu anterior ? (s/n)").upper()
    if(escolha_menu != "S") :
        print("Obrigado por usar UNESC Saúde.")
        return False
    else:
        return True

# Função para Calcular o IMC
def calcula_imc (altura, peso) :
    imc_do_paciente = peso / ((altura/100)* (altura/100))
    print(f"O seu IMC é {imc_do_paciente:.2f} \n\n")

# Funcao para calcular a taxa metabolica basal
def calcula_taxa_metabolica (altura, idade, peso) :
    if(sexo == '1'):
        resultado_masc = 66 + (13.8 * peso) + (5 * altura) - (6.8 * idade)
        print (f"Sua taxa metabolica basal é {resultado_masc:.2f} calorias \n\n")
    elif(sexo == '2'):
        resultado_fem = 655 + (9.6 * peso) + (1.8 * altura) - (4.7 * idade)
        print (f"Sua taxa metabolica basal é {resultado_fem:.2f} calorias \n\n")
    else:
        print("Valor digitado incorreto.")

while continue_menu == True :
    print("""=====MENU=====
1 - Calcular IMC
2 - Calcular a Taxa Metabolica Basal
3 - Sair""")
    opcao_desejada = str(input("Digite a opção desejada \n"))

    if(opcao_desejada == "1"):
        calcula_imc(altura_do_paciente, peso_do_paciente)
        continue_menu = retorna_menu()
    elif(opcao_desejada == "2"):
        calcula_taxa_metabolica(altura_do_paciente, idade_do_paciente, peso_do_paciente)
        continue_menu = retorna_menu()
    elif(opcao_desejada == "3"):
        print("Obrigado por usar UNESC Saúde.")
        continue_menu = False
    else:
        print("Valor digitado incorreto")
        continue_menu = retorna_menu ()