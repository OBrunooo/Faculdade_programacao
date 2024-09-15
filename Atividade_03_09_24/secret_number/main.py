import random
from secret_number import interface as i
from secret_number import calc as c

def secret_number():
    play = True
    while play == True:
        secret_number = random.randint(0, 100)
        i.welcome()
        i.introduction()
        attempt = i.first_attempt()

        attempts = 0
        is_right = False
        while is_right == False:
            attempts = attempts + 1
            check = c.checking(secret_number, attempt)
            match check:
                case 'ok':
                    i.congratulations(secret_number, attempts)
                    is_right = True
                case 'big':
                    attempt = i.number_bigger()
                case 'small':
                    attempt = i.number_small()
        play = i.play_again()
    i.thanks()