import math

def calcular_area_circulo(raio):
    # Utilize o valor de PI fornecido (3.14159)
    pi = 3.14159
    # Fórmula da área do círculo: A = π * r^2
    area = pi * raio ** 2
    return area

# Solicita ao usuário o raio do círculo
raio = float(input("Digite o raio do círculo: "))

# Calcula e exibe a área do círculo
area_circulo = calcular_area_circulo(raio)
print(f"A área do círculo com raio {raio} é: {area_circulo:.2f}")
