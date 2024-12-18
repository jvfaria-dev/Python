def recebe_inteiro(mensagem):
    while True:
        try:
            return (int(input(mensagem)))
        except:
            print("Insira um número válido.")


def fatorial(numero):
    if numero == 0:
        return 1
    else: 
        return numero * fatorial(numero - 1)

numero1 = int(input("Digite um número: "))

resultado = fatorial(numero1)
print("O resultado do fatorial é: {}".format(resultado))
