def calcular_soma_digitos(numero):
    # Inicializa a variável para armazenar a soma dos dígitos
    soma = 0
    
    # Divide o número sucessivamente pelas potências de 10
    # para obter cada dígito separadamente
    divisor = 10000
    
    while divisor >= 1:
        # Obtém o dígito atual
        digito = numero // divisor
        
        # Atualiza o número, retirando o dígito mais significativo
        numero %= divisor
        
        # Soma o dígito encontrado à soma total
        soma += digito
        
        # Atualiza o divisor para a próxima potência de 10
        divisor //= 10

    return soma

# Solicita ao usuário um número inteiro de até 5 dígitos
numero = int(input("Digite um número inteiro de até 5 dígitos: "))

# Verifica se o número fornecido possui até 5 dígitos
if 0 <= numero <= 99999:
    # Calcula a soma dos dígitos e exibe o resultado
    resultado = calcular_soma_digitos(numero)
    print(f"A soma dos dígitos de {numero} é: {resultado}")
else:
    print("Por favor, digite um número inteiro de até 5 dígitos.")
