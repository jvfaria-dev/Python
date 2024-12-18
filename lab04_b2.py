def recebe_inteiro(mensagem):
    while True:
        try:
            return int(input(mensagem))
        except ValueError:
            print("Insira um número inteiro.")


def ehpar(numero):
    return numero % 2 == 0

numero1 = recebe_inteiro("Digite um número: ")

if ehpar(numero1):
    print("O número {} é par!".format(numero1))
else:
    print("O número {} é impar".format(numero1))
