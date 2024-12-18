# Função para converter segundos para horas, minutos e segundos
def converter_segundos(intervalo_segundos):
    horas = intervalo_segundos // 3600
    minutos = (intervalo_segundos % 3600) // 60
    segundos = intervalo_segundos % 60
    return horas, minutos, segundos

# Solicitar ao usuário o intervalo de tempo em segundos
intervalo_segundos = int(input("Digite o intervalo de tempo em segundos: "))

# Chamar a função para converter e obter o resultado
horas, minutos, segundos = converter_segundos(intervalo_segundos)

# Apresentar o resultado
print("Resultado da conversão:")
print("Horas:", horas)
print("Minutos:", minutos)
print("Segundos:", segundos)
