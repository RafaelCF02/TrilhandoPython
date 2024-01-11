print('\033[1m' + "Calculo do IMC ")
print("-=-=-=-=-=-=-=-=-=-=-=-")

nome = str(input("Digite Seu nome:" ))
altura = float(input("Digite sua altura: "))
peso = float(input("Digite seu Peso: "))
imc = peso/(altura*altura)

print(f"{nome} tem {altura} de altura, pesa {peso}")
print(f"Seu IMC é {imc}")

print("-=-=-=-=-=-=-=-=-=-=-=-")

