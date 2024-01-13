'''
try -> tentar executar o código
except -> occoreu algum erro ao tentr executar
'''


numero = input('Vou dobrar o número que vc digitar: ')

try:
    print(f'valor inserido: {numero}')
    numero_float = float(numero)
    print(f'O dobro de {numero} é {numero_float * 2:.2f}')

except:
    print('O valor inserido nao e um numero')