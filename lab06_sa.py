def sublista_crescente(lista):
    maior_sublista = []
    sublista_temporaria = [lista[0]]

    for i in range(1, len(lista)):
        if lista[i] == sublista_temporaria[-1] + 1:
            sublista_temporaria.append(lista[i])
        else:
            if len(sublista_temporaria) > len(maior_sublista):
                maior_sublista = sublista_temporaria.copy()
            sublista_temporaria = [lista[i]]

    if len(sublista_temporaria) > len(maior_sublista):
        maior_sublista = sublista_temporaria

    return maior_sublista

entrada = input("Digite uma sequência de números separados por vírgula: ")

numeros = [int(numero.strip()) for numero in entrada.split(',') if numero.strip().isdigit()]

maior_sublista = sublista_crescente(numeros)

print("Maior sublista crescente:", maior_sublista)
