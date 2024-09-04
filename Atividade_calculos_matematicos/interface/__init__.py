from .initial import *
from .menu import *
from .reply import *
from .result import *
from .final import *
import calc as c

def run_program():
    initial()
    back_menu = True
    while back_menu == True :
        opition = menu()
        match opition:
            case 1:
                result('area', 'triângulo', c.triangle())
                back_menu = return_menu()
            case 2:
                result('perímetro', 'retangulo', c.rectangle())
                back_menu = return_menu()
            case 3:
                result('area', 'circulo', c.circle())
                back_menu = return_menu()
            case 4:
                result('volume', 'cilindro', c.cylinder())
                back_menu = return_menu()
            case 5: 
                back_menu = False
        match back_menu:
            case False:
                final()