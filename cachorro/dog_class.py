class Dog():
    def __init__(self, name):
        self.name = name
        self.hungry = 0 
        self.tired = 0 
        self.is_sleep = True
        self.life = True

    def status(self):
        print(f"""Nome: {self.name}
Fome: {self.hungry}
Cansaço: {self.tired}
Sono: {'Dormindo' if self.is_sleep == True else "Acordado"} 
Estado vital: {'Vivo' if self.life == True else 'Morto'}
""")
        
    def dead (self):
        self.hungry = 0
        self.hungry = 0 
        self.tired = 0 
        self.sleep = False
        self.life = False

    def wakeup (self):
        if (self.life == False):
            print(f"Infelizmente o {self.name} está morto, não pode acordar")
        else:
            if(self.is_sleep == False):
                print(f"O {self.name} já está acordado !")
            else:
                print(f"{self.name} foi acordado")
                self.is_sleep = False

    def sleep (self):
        if (self.life == False):
            print(f"Infelizmente o {self.name} está morto, não pode dormir")
        else:
            if(self.is_sleep == True):
                print(f"O {self.name} já está dormindo !")
            else:
                print(f"{self.name} foi dormir")
                self.is_sleep = True
                self.tired = 0

    
    def feed(self):
        if (self.life == False):
            print(f"Infelizmente o {self.name} está morto, não pode comer")
        elif (self.is_sleep == True):
            print(f"{self.name} está dormindo !")
        else:
            if(self.hungry == 0):
                print(f"O {self.name} já está completamente alimentado")
            else:
                print(f"O {self.name} foi alimentado !")
                self.hungry = 0
        

    def play(self):
        if (self.life == False):
            print(f"Infelizmente o {self.name} está morto, não pode brincar")
        elif (self.is_sleep == True):
            print(f"{self.name} está dormindo !")
        else:
            if (self.hungry == 5):
                play = int(input("""Seu cão está com 5 de fome. 
Se brincar mais uma vez ele irá morrer !!!
Deseja brinca mesmo assim?
Digite 1 para brincar ou 2 para não brincar: """))
                if (play == 1):
                    print(f"{self.name} brincou até morrer :( ")
                    return self.dead(self)
                if (play == 2):
                    return print(f"{self.name} não brincou, mas ainda está com fome, alimente-o novamente")
            elif(self.tired == 4):
                play = int(input("""Seu cão está com 4 de cansaço. 
Se brincar mais uma vez ele irá dormir !!!
Deseja brinca mesmo assim?
Digite 1 para brincar ou 2 para não brincar: """))
                if (play == 1):
                        print(f"{self.name} brincou até dormir")
                        self.tired += 1
                        self.hungry += 1
                        self.is_sleep = True
                if (play == 2):
                    return print(f"{self.name} não brincou, mas ainda está com cansado, faça-o dormir novamente")
            else:
                print(f"O {self.name} brincou")
                self.tired += 1
                self.hungry += 1
        

        