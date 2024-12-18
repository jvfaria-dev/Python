def remove_duplicatas(lista):
    lista_sduplicatas = []
    elementos = set()

    for i in lista:
        if i not in elementos:
            elementos.add(i)
            lista_sduplicatas.append(i)

    return lista_sduplicatas

entrada = input("Digite uma sequência de números separados por vírgula: ")

numeros = [int(numero.strip()) for numero in entrada.split(',') if numero.strip().isdigit()]

numeros_sduplicatas = remove_duplicatas(numeros)

print("Lista original:", numeros)
print("Lista sem duplicatas:", numeros_sduplicatas)
