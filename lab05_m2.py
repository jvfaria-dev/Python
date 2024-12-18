from lab05_m1 import mdc

def mmc(x, y):
    return (x * y) // mdc(x, y)
    
numero1 = int(input("Digite o prímeiro número: "))
numero2 = int(input("Digite o segundo número: "))

resultado = mmc(numero1, numero2)
print("O mmc entre os números {} e {} é igual à: {}.".format(numero1, numero2, resultado))