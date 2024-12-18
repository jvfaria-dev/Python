def vogais_em_asteristicos(frase):
    vogais = "aeiouAEIOU"
    for i in vogais:
        frase = frase.replace(i, "*")
    return frase


frase = input("Digite uma frase: ")

print("Frase sem vogais: {}".format(vogais_em_asteristicos(frase)))
