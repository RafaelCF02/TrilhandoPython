''' Calculadora com while '''

while True:
    numero_um = input("Digite um numero: ")
    numero_dois = input("Digite outro numero: ")
    operador = input("Escolha o operador ['+','-','*','/']: ")
    validacao = None

    try:
        primeiro_numero = float(numero_um)
        segundo_numero = float(numero_dois)
        validacao = True

    except:
        validacao = None
        print("O numero digitado é inválido")
        continue
    
    operadores_permitidos = '+-*/'

    if validacao == True and operador in operadores_permitidos:
        if operador == '+':
            print(f'Resultado: {primeiro_numero + segundo_numero}')
        elif operador == '-':
            print(f'Resultado: {primeiro_numero - segundo_numero}')
        elif operador == '*':
            print(f'Resultado: {primeiro_numero * segundo_numero}')
        elif operador == '/':
            print(f'Resultado: {primeiro_numero / segundo_numero}')
        
    if operador not in operadores_permitidos:
        print("Operador invalido")
        continue

    if len(operador) > 1:
        print('Operador invalido')
        continue

    sair = input("Deseja Sair? ").lower()
    if sair[0] == 's':
        break
    else:
        continue