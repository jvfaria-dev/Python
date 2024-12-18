# Solicita ao usuário para inserir dois números inteiros
num1 = int(input("Digite o primeiro número inteiro: "))
num2 = int(input("Digite o segundo número inteiro: "))

# Realiza as operações
soma = num1 + num2
subtracao = num1 - num2
multiplicacao = num1 * num2
divisao_float = num1 / num2
divisao_inteira = num1 // num2
resto_divisao = num1 % num2
potenciacao = num1 ** num2

# Exibe os resultados
print("Resultado:")
print("Soma:", soma)
print("Subtração:", subtracao)
print("Multiplicação:", multiplicacao)
print("Divisão (com resultado como float):", divisao_float)
print("Divisão inteira:", divisao_inteira)
print("Resto da divisão:", resto_divisao)
print("Potenciação:", potenciacao)
