pares = []

while True:
    numero = int(input("Digite um número inteiro: "))
    if numero is 0:
        break
    if numero % 2 == 0:
        pares.append(numero)

if pares:
    print("Os números pares: {}.".format(pares))
else:
    print("Não possui números impares.")
