primeiro_valor = input("Digite um valor: ")
segundo_valor = input("Digite um segundo valor: ")

if primeiro_valor > segundo_valor:
    print(f'O primeiro valor = {primeiro_valor} eh maior que o segundo valor = {segundo_valor} ')
elif primeiro_valor == segundo_valor:
    print(f"Os valores {primeiro_valor} e {segundo_valor} sao iguais")
elif  primeiro_valor < segundo_valor:
    print(f'O segundo valor = {segundo_valor} eh maior que o primeiro valor = {primeiro_valor} ')
    