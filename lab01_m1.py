# Função para converter Celsius para Fahrenheit
def celsius_para_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# Função para converter Fahrenheit para Celsius
def fahrenheit_para_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

# Solicitar ao usuário a temperatura em Celsius
temperatura_celsius = float(input("Digite a temperatura em Celsius: "))

# Converter para Fahrenheit e apresentar o resultado
temperatura_fahrenheit = celsius_para_fahrenheit(temperatura_celsius)
print("Resultado da conversão de Celsius para Fahrenheit:", temperatura_fahrenheit, "F")

# Solicitar ao usuário a temperatura em Fahrenheit
temperatura_fahrenheit = float(input("Digite a temperatura em Fahrenheit: "))

# Converter para Celsius e apresentar o resultado
temperatura_celsius = fahrenheit_para_celsius(temperatura_fahrenheit)
print("Resultado da conversão de Fahrenheit para Celsius:", temperatura_celsius, "C")
