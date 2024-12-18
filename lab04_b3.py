def recebe_inteiro(mensagem):
    while True:
        try:
            int(input(mensagem))
        except:
            print("Insira um número inteiro.")


def media(a, b, c):
    return (a + b + c) / 3


numero1 = int(input("Digite um valor: "))
numero2 = int(input("Digite um valor: "))
numero3 = int(input("Digite um valor: "))

resultado = media(numero1, numero2, numero3)

print("O reultado da média entre os números é de: {}".format(resultado))
