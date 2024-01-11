#conversão de tipos, coerção
#type convertio, typecasting, coercion
#converte um tipo em outro
#tipos imutaveis e primitivos
#str, int, float, bool 
print('\033[1m' + "Conversão de tipos")
print(str(11)+'a')
print(int("34")+20)
print("-=-=-=-=-=-=-=-=-=-=-=-=-\n")

#Variáveis são usadas para salvar algo na memoria do computador
print('\033[1m'+"Variaveis")
nome = "Rafael"
idade = 26
maior_de_idade = idade >= 18
print(" Nome:", nome,"\n","Idade:", idade,"\n","E maior de idade?", maior_de_idade)
print("-=-=-=-=-=-=-=-=-=-=-=-=-\n")

#Operadores Aritiméticos 
print('\033[1m' + "Operadores Aritimeticos")


adicao = 10 + 10
print('Adição', adicao)

subtracao = 10 - 5
print('Subtração', subtracao)

multiplicacao = 10 * 10
print('Multiplicação', multiplicacao)

divisao = 10 / 3  # float
print('Divisão', divisao)

divisao_inteira = 10 // 3
print('Divisão inteira', divisao_inteira)

exponenciacao = 2 ** 10
print('Exponenciação', exponenciacao)

modulo = 55 % 2  # resto da divisão
print('Módulo', modulo)

print(10 % 8 == 0)
print(16 % 8 == 0)
print(10 % 2 == 0)
print(15 % 2 == 0)
print(16 % 2 == 0)

print("-=-=-=-=-=-=-=-=-=-=-=-=-\n")

#Concatenação
print('\033[1m' + "Concatenação")

concatenacao = 'Rafael' + ' ' + 'Costa'
print(concatenacao)

a_dez_vezes = 'A' * 10
tres_vezes_luiz = 3 * 'Rafael'
print(a_dez_vezes)
print(tres_vezes_luiz)

print("-=-=-=-=-=-=-=-=-=-=-=-=-\n")

#Precedência entre Operadores 

# 1. (n + n)
# 2. **
# 3. * / // %
# 4. + -


