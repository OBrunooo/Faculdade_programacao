def result (area_volume_perrimete ,name, calc):
    match area_volume_perrimete :
        case 'area':
            print(f"A área do {name} é de {calc:.2f}cm² ")
        case 'volume':
            print(f"O volume do {name} é de {calc:.2f}cm³ ")
        case 'perímetro':
            print(f"O perímetro do {name} é de {calc:.2f}cm")