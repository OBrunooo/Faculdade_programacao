from .interface import *
from .calc import *

def converter ():
    # valores iniciais para comecar o while
    return_menu = True
    new_convert = True
    new_value = True

    welcome()
    # cotacão digitada pelo usuário
    price = return_cot()

    while return_menu == True:
        # Se não tiver uma conversão definida ou se o usuário decidir mudar de conversão o programa irá entrar no if
        if new_convert == True :
            convert = option_convert()
            new_convert = False
        # Se não tiver um valor para fazer a conversão ou o usuário decidir fazer a conversão de um novo valor o programa irá entrar no if
        if new_value == True:
            value = select_value()
        # O programa vai executar o cálculo de acordo com o tipo de conversão escolhida anteriormente pelo usuário
        match convert:
            case 1:
                doll_to_real(value,price)
            case 2:
                real_to_doll(value, price)
        # Recebe o valor escolhido no menu
        menu = select_menu()
        match menu:
            case 1:
                # caso o usuário escolha 1 que é referente conversão de um novo valor, o programa irá alterar o new_value para True.
                # Desta forma o programa irá entrar no segundo if dentro deste while
                new_value = True
            case 2:
                # caso o usuário escolha 2 que é referente a alteração do tipo de conversão, o programa irá alterar o new_convert e new_value para True.
                # Desta forma o programa irá entrar no primeiro e segundo if dentro deste while
                new_convert = True
                new_value = True
            case 3:
                # caso o usuário escolha 3 que é referente a finalizar, o programa irá alterar o valor de return_menu para false.
                # Desta forma o while vai encerrar
                return_menu = False
                thanks()



