def comeca_nao_branco(frase):
    while frase and frase[0] in [' ', '\t', '\n']:
        frase = frase[1:]
    return frase

def limpa_brancos(frase):
    while frase and frase[-1] in [' ', '\t', '\n']:
        frase = frase[:-1]
    return frase

frase = input("Digite uma palavra ou frase contendo caracteres brancos no início e no final: ")

print("Frase sem brancos:", limpa_brancos(comeca_nao_branco(frase)))
