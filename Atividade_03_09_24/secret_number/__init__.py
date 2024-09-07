from .main import secret_number

# def secret_number():
#     play_again = True
#     while play_again == True:
#         joker = random.randint(0, 100)
#         welcome()
#         introduction()
#         attempt = first_attempt()

#         attempts = 0
#         is_right = False
#         while is_right == False:
#             attempts = attempts + 1
#             check = checking(joker, attempt)
#             match check:
#                 case 'ok':
#                     congratulations(joker, attempts)
#                     is_right = True
#                 case 'big':
#                     attempt = number_bigger()
#                 case 'small':
#                     attempt = number_small()
#         play_again = play_again()
#     thanks()