from random import randint

escolhidos = []
while len(escolhidos) < 5:
    numero = randint(1, 30)
    if numero not in escolhidos:
        escolhidos.append(numero)

print("Tente adivinhar um dos números escolhidos (entre 1 e 30):")
acertou = False
while not acertou:
    chute = int(input("Seu palpite: "))
    if chute in escolhidos:
        print("Você acertou.")
        acertou = True
    else:
        print("Este número não está na lista.")

print("Os números escolhidos foram:", escolhidos)
