import interface as i
from calculator import calcula
from converter import converter
from secret_number import secret_number
from to_do_list import to_do_list

def main():
    return_menu = True
    i.welcome()
    while return_menu == True:
        select_menu = i.menu()
        match select_menu:
            case 1:
                calcula()
            case 2:
                converter()
            case 3:
                secret_number()
            case 4:
                to_do_list()
            case 5: 
                return_menu = False
                i.thanks()

main()

