import calc
import interface

def main ():
    interface.welcome()
    option = interface.menu()
    v1 = interface.value1()
    v2 = interface.value2()
    calc.calc(v1,v2,option)

if __name__ == "__main__" :
    main()