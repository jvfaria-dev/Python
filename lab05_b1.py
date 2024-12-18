def troca(a, b):
    return b, a

entrada = str(input("Digite dois números separados por vírgula: "))

try:
    a, b = map(int, entrada.split(','))
except ValueError:
    print("Escreva um número separado por vírgula.")
else:
    a, b = troca(a, b)
print("O novo valor de a é igual a {}".format(a))
print("O novo valor de b é igual a {}".format(b))
