class Carro: 
    def __init__(self, model, brand, max_speed):
        self.model = model
        self.brand = brand 
        self.max_speed = max_speed
        self.is_on = False
        self.speed = 0

    def speed_up(self):
        if(self.is_on == False):
            print("Ligue o carro para acelerar")
        else:
            if((self.speed + 10) > self.max_speed):
                print(f"Você não pode acelerar mais, a velocidade máxima do carro é de {self.max_speed} Km/h")
            elif((self.speed + 10) == self.max_speed):
                self.speed += 10
                print(f"Você acabou de acelerar totalmente o carro. Ele está a {self.speed} km/h")
            else:
                self.speed += 10
                print(f"Você acelerou o carro, agora está a {self.speed} km/h")

    def speed_down(self):
        if(self.is_on == False):
            print("O carro está desligado")
        else:
            if((self.speed - 10) < 0):
                print(f"Você não pode desacelerar mais. O carro já está a {self.speed} Km/h")
            elif((self.speed - 10) == 0):
                print(f"Você acabou de desacelerar totalmente o carro. Ele está a 0 km/h")
                self.speed -= 10
            else:
                self.speed -= 10
                print(f"Você desacelerou o carro, agora está a {self.speed}km/h")

    def turn_on(self):
        if (self.is_on == True):
            print(f"O carro {self.brand} {self.model} já está ligado")
        else:
            print(f"Você ligou o {self.brand} {self.model}")
            self.is_on = True

    def turn_off(self):
        if (self.is_on == False):
            print(f"O carro {self.brand} {self.model} já está desligado")
        else:
            if (self.speed > 0):
                print("Você não pode desligar o carro, ele está em movimento")
            else:
                print(f"Você desligou o {self.brand} {self.model}")
                self.is_on = False


carro1 = Carro('Hilux', 'Toyota', 200)


def show_menu():
    print("""1_ Ligar o carro
2_ Desligar o carro
3_ Acelerar o carro
4_ Freiar o carro
5_ Desligar programa
""")
    
while True:
    show_menu()
    try:
        opcao = int(input("Digite a opção desejada: "))
        if opcao == 1:
            carro1.turn_on()
        elif opcao == 2:
            carro1.turn_off()
        elif opcao == 3:
            carro1.speed_up()
        elif opcao == 4:
            carro1.speed_down()
        elif opcao == 5:
            break
        else:
            print("Valor digitado incorreto")
    except:
        print("Valor digitado incorreto")