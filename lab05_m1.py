def mdc(x, y):
    if y == 0:
        return x
    else:
        return mdc(y, x % y)

numero1 = int(input("Digite o prímeiro número:  "))
numero2 = int(input("Digite o segundo número: "))

resultado = mdc(numero1, numero2)

print("O resultado do mdc entre os números {} e {} é igual à {}.".format(numero1, numero2, resultado))