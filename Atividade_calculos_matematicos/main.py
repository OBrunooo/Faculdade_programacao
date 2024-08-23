import initialize
import menu
import result
import triangulo as t
import quadrado as q

initialize.initial()
escolha = menu.menu()

match escolha:
    case 1:
        result.result('triângulo', t.area_triangulo())
    case 2:
        result.result('quadrado', q.area_quadrado())
