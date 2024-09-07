def welcome():
    print("=== Bem vindo(a) ao jogo do número secreto ===\n")

def thanks():
    print("obrigado por utilizar o nosso jogo do número secreto !")

def introduction():
    print("Neste jogo o computador vai gerar um número aleatório entre 0 e 100. Você tem que adivinhar qual valor foi gerado:")

def first_attempt ():
    attempt = int(input("Dê o seu primeiro chute: "))
    return attempt

def number_bigger():
    attempt = int(input("""O seu chute foi alto. Tente novamente
Digite outro valor: """))
    return attempt

def number_small():
    attempt = int(input("""O seu chute foi baixo. Tente novamente
Digite outro valor: """))
    return attempt

def congratulations(number, attempts):
    print (f"Parabéns, você acertou o número {number} em {attempts} tentativas")

def play_again ():
    again = str(input("Deseja jogar novamente ? (s/n)")).upper()
    match again:
        case 'S':
            return True
        case 'N':
            return False
