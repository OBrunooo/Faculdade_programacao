def calc (v1, v2, option):
    match option:
        case '-' | 'subtração':
            print(f"A subtração de {v1} - {v2} = {v1-v2} ")
        case '+' | 'adição':
            print(f"A adição de {v1} + {v2} = {v1+v2} ")
        case 'X' | 'x' | 'multiplicação':
            print(f"A multiplicação de {v1} - {v2} = {v1*v2} ")
        case '/' | 'divisão':
            print(f"A divisão de {v1} / {v2} = {v1/v2} ")