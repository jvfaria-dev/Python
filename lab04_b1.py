def recebe_inteiro(mensagem):
    while True:
        try:
            return int(input(mensagem))
        except ValueError:
            print("Por favor, insira um número inteiro válido.")

def soma(a, b, c):
    return a + b + c

numero1 = recebe_inteiro("Digite o primeiro número inteiro: ")
numero2 = recebe_inteiro("Digite o segundo número inteiro: ")
numero3 = recebe_inteiro("Digite o terceiro número inteiro: ")

resultado = soma(numero1, numero2, numero3)

print("A soma dos números informados é:", resultado)
