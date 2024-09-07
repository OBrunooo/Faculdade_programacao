import interface as i
from calculator import main as calc
from converter import main as convert
from secret_number import main as s_number
from to_do_list import main as td_list

def main():
    return_menu = True
    i.welcome()
    while return_menu == True:
        select_menu = i.menu()
        match select_menu:
            case 1:
                calc.calculator()
            case 2:
                convert.converter()
            case 3:
                s_number.secret_number()
            case 4:
                td_list.to_do_list()
            case 5: 
                return_menu = False
                i.thanks()

main()

