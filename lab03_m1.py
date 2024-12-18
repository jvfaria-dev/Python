try:
    lado = int(input("Digite o tamanho do lado do quadrado de coordenadas: "))
    if lado <= 0:
        print("Por favor, digite um tamanho válido para o lado do quadrado.")
    else:
        for i in range(lado):
            for j in range(lado):
                print(f'({i},{j})')
except ValueError:
    print("Por favor, digite um número inteiro válido.")
