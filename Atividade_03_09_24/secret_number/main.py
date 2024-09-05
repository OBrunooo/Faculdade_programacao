import random
import interface as i
import calc as c

play_again = True
while play_again == True:
    joker = random.randint(0, 100)
    i.welcome()
    i.introduction()
    attempt = i.first_attempt()

    attempts = 0
    is_right = False
    while is_right == False:
        attempts = attempts + 1
        check = c.checking(joker, attempt)
        match check:
            case 'ok':
                i.congratulations(joker, attempts)
                is_right = True
            case 'big':
                attempt = i.number_bigger()
            case 'small':
                attempt = i.number_small()
    play_again = i.play_again()
i.thanks()