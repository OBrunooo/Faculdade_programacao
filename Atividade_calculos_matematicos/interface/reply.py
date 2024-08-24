def return_menu ():
    reply = ' '
    reply = str(input("Deseja retornar ao menu principal? (s/n) ")).upper()
    while (reply != 'S' and reply !='N') :
        print("Valor digitado incorreto !!!")
        reply = str(input("Deseja retornar ao menu principal? (s/n) ")).upper()
    match reply:
            case 'S':
                return True
            case 'N':
                return False