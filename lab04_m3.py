def recebeInteiro(mensagem):
    while True:
        try:
            numero = int(input(mensagem))
            if numero <= 0:
                print("Por favor, insira um número inteiro positivo.")
                continue
            return numero
        except ValueError:
            print("Por favor, insira um número inteiro válido.")

def mdc(a, b):
    while b != 0:
        a, b = b, a % b
    return a

numero1 = recebeInteiro("Digite o primeiro número inteiro positivo: ")
numero2 = recebeInteiro("Digite o segundo número inteiro positivo: ")

divisor_comum = mdc(numero1, numero2)

print(f"O MDC de {numero1} e {numero2} é {divisor_comum}.")
