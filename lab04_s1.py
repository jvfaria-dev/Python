import math

def graus_para_radianos(angulo_graus):
    return angulo_graus * math.pi / 180

def altura_cateto(hipotenusa, angulo_radianos):
    return hipotenusa * math.cos(angulo_radianos)

def altura_media_geometrica(cateto1, cateto2):
    return math.sqrt(cateto1 * cateto2)

def altura_maxima(cateto1, cateto2):
    return max(cateto1, cateto2)

hipotenusa = float(input("Digite o tamanho da hipotenusa: "))
angulo_graus = float(input("Digite o ângulo (em graus) entre a hipotenusa e um dos catetos: "))

angulo_radianos = graus_para_radianos(angulo_graus)

altura_cateto1 = altura_cateto(hipotenusa, angulo_radianos)
altura_cateto2 = altura_cateto(hipotenusa, math.pi/2 - angulo_radianos)

altura_media = altura_media_geometrica(altura_cateto1, altura_cateto2)

altura_max = altura_maxima(altura_cateto1, altura_cateto2)

print(f"Altura relativa ao cateto 1: {altura_cateto1:.2f}")
print(f"Altura relativa ao cateto 2: {altura_cateto2:.2f}")
print(f"Altura média geométrica: {altura_media:.2f}")

print(f"Altura máxima do triângulo retângulo: {altura_max:.2f}")
