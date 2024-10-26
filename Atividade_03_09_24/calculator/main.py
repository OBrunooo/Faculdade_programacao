from calculator import calc as c
from calculator import interface as i

def calcula ():
    
    return_menu = True
    select_menu = 2
    i.welcome()
    while return_menu == True:
        match select_menu:
            case 1:
                v1 =i.value1()
                v2 =i.value2()
                c.calc(v1,v2,option)
                select_menu =i.menu()
            case 2:
                option = i.operator()
                v1 =i.value1()
                v2 =i.value2()
                c.calc(v1,v2,option)
                select_menu =i.menu()
            case 3: 
                return_menu = False
                i.thanks()
                

if __name__ == "__main__" :
    calculator()