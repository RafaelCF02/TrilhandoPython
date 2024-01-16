"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
print('\033[1m' + 'Atividade 1\n')

while True:
    num = input("Digite um numero inteiro: ")

    if num.isdigit():
        num = int(num)
        if num % 2 == 0:
            print("O numero escolhido é Par")
            break
        else:
            print("O numero escolhido é ímpar")
            break
    else:
        print("O valor digitado não é um número inteiro!")

print("\n-=-=-=-=--=-=-=-=-=-=-=-=-=-\n")
"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
print('\033[1m' + 'Atividade 2\n')

try:
    hora_input = input("Que horas são? ")
    horas_str, minutos_str = hora_input.split(':') 
    
    horas = int(horas_str)
    minutos = int(minutos_str)

    if 0 <= horas <= 11:
        print("Bom dia")
    elif 12 <= horas <= 17:
        print("Boa tarde")
    else:
        print("Boa noite")
except:
    print("Ocorreu um ERRO com o horário inserido")

print("\n-=-=-=-=--=-=-=-=-=-=-=-=-=-\n")


"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande".
"""
print('\033[1m' + 'Atividade 3\n')

try:
    nome = input("Digite seu nome: ").capitalize()

    if len(nome) <= 4:
        print(f'{nome} seu nome é bem curto')
    elif len(nome) <= 6:
        print(f'{nome} seu nome tem um tamanho normal!')
    else:
        print(f'{nome} seu nome é bem grande em')
        print('La ele' + '\U0001F923')
except:
    print("O nome inserido não possui apenas letras,por favor reescreva")

print("\n-=-=-=-=--=-=-=-=-=-=-=-=-=-\n")
