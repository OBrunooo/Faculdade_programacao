import calc as c
import interface as i

def main():
    i.initial()
    repeat = True
    while repeat == True :
        opition = i.menu()
        match opition:
            case 1:
                i.result('area', 'triângulo', c.triangulo())
                repeat = i.return_menu()
            case 2:
                i.result('area', 'quadrado', c.quadrado())
                repeat = i.return_menu()
            case 3:
                i.result('area', 'circulo', c.circulo())
                repeat = i.return_menu()
            case 4:
                i.result('volume', 'cilindro', c.cilindro())
                repeat = i.return_menu()
            case 5: 
                repeat = False
        match repeat:
            case False:
                i.final()

if __name__ == "__main__" :
    main ()
        