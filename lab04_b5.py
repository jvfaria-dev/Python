def recebe_inteiro(mensagem):
    while True:
        try:
            return int(input(mensagem))
        except:
            print("Insira um número inteiro.")


def maximo(a, b, c):
    if a > b > c:
        maior = a
    elif a < b > c:
        maior = b
    elif a < b < c:
        maior = c
    return maior


numero1 = int(input("Digite um número: "))
numero2 = int(input("Digite um número: "))
numero3 = int(input("Digite um número: "))

resultado = maximo(numero1, numero2, numero3)
print("O maior número é o {}".format(resultado))
