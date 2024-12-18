# Solicita ao usuário para inserir um caractere
caractere = input("Digite um caractere: ")

# Obtém o código ASCII do caractere
codigo_ascii = ord(caractere)

# Calcula o caractere correspondente ao código ASCII anterior
caractere_anterior = chr(codigo_ascii - 1) if codigo_ascii > 0 else None

# Calcula o caractere correspondente ao código ASCII seguinte
caractere_seguinte = chr(codigo_ascii + 1) if codigo_ascii < 127 else None

# Exibe as informações relacionadas ao código ASCII
print("Informações relacionadas ao código ASCII:")
print("1. O código ASCII do caractere:", codigo_ascii)
print("2. O caractere correspondente ao código ASCII anterior:", caractere_anterior)
print("3. O caractere correspondente ao código ASCII seguinte:", caractere_seguinte)
