"""
Iterando strings com while
"""

      
nome = "Rafael Costa" # iteráveis

print(len(nome))

string = 0
customizado = ''
while string < len(nome):
    print(nome[string])
    letra = nome[string]
    customizado += f'/{letra}'
    string += 1

print(customizado)
