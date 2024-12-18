import math

def dentroCirculo(x, y, r):
    distancia_centro = math.sqrt(x**2 + y**2)
    return distancia_centro <= r

x = float(input("Digite a coordenada x do ponto: "))
y = float(input("Digite a coordenada y do ponto: "))
raio = float(input("Digite o raio do círculo: "))

if dentroCirculo(x, y, raio):
    print("O ponto está dentro ou sobre a circunferência do círculo.")
else:
    print("O ponto está fora da circunferência do círculo.")    