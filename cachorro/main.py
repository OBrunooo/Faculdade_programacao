from dog_class import Dog

def main():
    dog = str(input("Digite um nome para o seu cachorro: "))
    dog = Dog(dog)
    while True:
        print("""=== Menu Principal ===
              
1_ Status
2_ Acordar
3_ Dormir
4_ Alimentar
5_ Brincar
              """)
        option = int(input("Selecione um: "))
        if(option == 1):
            dog.status()
        elif(option == 2):
            dog.wakeup()
        elif(option == 3):
            dog.sleep()
        elif(option ==4):
            dog.feed()
        elif(option == 5):
            dog.play()

main()