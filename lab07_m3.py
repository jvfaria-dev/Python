def separa(frase, caractere=""):
    return frase.split(caractere)

def Maior_palavra(palavras):
    return max(palavras, key=len)

def Menor_Palavra(palavras):
    return min(palavras, key=len)

frase = input("Digite uma frase: ")
palavras = separa(frase, "|")

menor = Menor_Palavra(palavras)
maior = Maior_palavra(palavras)

print("A maior palavra é {}".format(maior))
print("A menor palavra é {}".format(menor))