# Operadores lógicos
# and (e) or (ou) not (não)
# or - Qualquer condição verdadeira avalia
# toda a expressão como verdadeira.
# Se qualquer valor for considerado verdadeiro,
# a expressão inteira será avaliada naquele valor.
# São considerados falsy (que vc já viu)
# 0 0.0 '' False
# Também existe o tipo None que é
# usado para representar um não valor

print('\033[1m' + "Operdores Logicos\n")
entrar = input("Deseja [E]ntrar? ")
senha = input('Senha: ')

senha_correta = 'abc'

if entrar == 'E' or 'e' and senha == senha_correta:
    print("Acesso Permitido")
else:
    print("Acesso Negado")

print("\n=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n")
'''
Interpolação de strings
s- string
d e i - int
f- float
x e X - Hexdecimal
'''
print('\033[1m' + "Interpolacao de Strings\n")

nome = 'Rafael'
num = 69.02
interpol = '%s, o preco eh %.2f' %(nome, num)
print(interpol)
print(
    'conversao de um numero para hexadecimal\n'
    '%i em hexadecimal eh %04X' %(43,43)
    )

print("\n=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n")

"""
Formatação básica de strings
s - string
d - int
f - float
.<número de dígitos>f
x ou X - Hexadecimal
(Caractere)(><^)(quantidade)
> - Esquerda
< - Direita
^ - Centro
= - Força o número a aparecer antes dos zeros
Sinal - + ou -
Ex.: 0>-100,.1f
Conversion flags - !r !s !a 
"""

print('\033[1m' + "Formatacao de Strings\n")

variavel = 'ABC'
print(f'{variavel}')
print(f'{variavel: >10}')
print(f'{variavel: <10}.')
print(f'{variavel: ^10}.')
print(f'{1000.4873648123746:0=+10,.1f}')
print(f'O hexadecimal de 1500 é {1500:04X}')
print(f'{variavel!r}')

print("\n=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n")
