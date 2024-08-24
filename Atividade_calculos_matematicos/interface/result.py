def result (area_volume ,name, calc):
    match area_volume :
        case 'area':
            print(f"A área do {name} é de {calc:.2f}cm² ")
        case 'volume':
            print(f"O volume do {name} é de {calc:.2f}cm³ ")