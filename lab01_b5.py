# Solicita ao usuário para inserir o peso (em kg) e a altura (em metros)
peso = float(input("Digite seu peso (em kg): "))
altura = float(input("Digite sua altura (em metros): "))

# Calcula o Índice de Massa Corporal (IMC)
imc = peso / (altura ** 2)

# Exibe o resultado com duas casas decimais
print("Seu IMC é: {:.2f}".format(imc))
