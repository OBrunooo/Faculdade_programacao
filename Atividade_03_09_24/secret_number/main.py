import random
from .interface import *
from .calc import *

def secret_number():
    play = True
    while play == True:
        joker = random.randint(0, 100)
        welcome()
        introduction()
        attempt = first_attempt()

        attempts = 0
        is_right = False
        while is_right == False:
            attempts = attempts + 1
            check = checking(joker, attempt)
            match check:
                case 'ok':
                    congratulations(joker, attempts)
                    is_right = True
                case 'big':
                    attempt = number_bigger()
                case 'small':
                    attempt = number_small()
        play = play_again()
    thanks()