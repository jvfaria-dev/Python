ano_corrente = int(input("Digite o ano corrente: "))
idade = int(input("Digite sua idade para avalição: "))
ano_nascimento = int(input("Digite o ano que você nasceu: "))
 
idade_aproximada = ano_corrente - ano_nascimento
idade_aproximada_proxima = idade_aproximada - 1

if idade_aproximada == idade:
    print(f" A idade foi validada! Você ainda vai fazer aniversário esse ano!")
elif idade == idade_aproximada:
    print("Já fez aniversário esse ano! Feliz aniversário atrasado!")
else:
    print("Idade não validada!")