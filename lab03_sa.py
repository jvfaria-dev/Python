import random

nome = input("Digite seu nome: ")

random.seed(hash(nome))
numero_aleatorio = random.randint(0, 99)

tentativas = 0

while True:
    palpite = int(input("Tente adivinhar o número (de 0 a 99): "))

    tentativas += 1

    if palpite < numero_aleatorio:
        print("Tente um número maior.")
    elif palpite > numero_aleatorio:
        print("Tente um número menor.")
    else:
        print(f"Parabéns, {nome}! Você acertou o número {numero_aleatorio} em {tentativas} tentativas.")
        break
