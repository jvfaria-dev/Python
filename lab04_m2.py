def posicao(pos0, v0, a, t):
    return pos0 + v0 * t + 0.5 * a * t**2


pos0 = float(input("Digite a posição inicial: "))
v0 = float(input("Digite a velocidade inicial: "))
a = float(input("Digite a aceleração constante "))

for t in range(0,11):
    resultado = posicao(pos0, v0, a, t)
    print("Para t={}, a posição é de {}".format(t, resultado))