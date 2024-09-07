from .calc import *
from .interface import *

def calculator ():
    return_menu = True
    select_menu = 2
    welcome()
    while return_menu == True:
        match select_menu:
            case 1:
                v1 = value1()
                v2 = value2()
                calc(v1,v2,option)
                select_menu = menu()
            case 2:
                option = operator()
                v1 = value1()
                v2 = value2()
                calc(v1,v2,option)
                select_menu = menu()
            case 3: 
                return_menu = False
                thanks()
                



if __name__ == "__main__" :
    calculator()