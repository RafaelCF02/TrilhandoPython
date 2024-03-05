import random

strings = ['lapis', 'teste', 'bola', 'caneta', 'cama']

palavra = random.choice(strings)

print('Adivinhe a palavra')
print(f'Dica a plavra possui {len(palavra)} letras')
print('Voce tera 6 tentativas\n')

tentativas = 0

while tentativas < 6:
  tentativa = input('Digite uma palavra: ').lower()
  tentativas += 1

  if tentativa == palavra:
    print('Parabens, voce acertou')
    break

  else:
    dica = ''
    for i in range(len(palavra)):

      if i < len(tentativa) and tentativa[i] == palavra[i]:
        dica += tentativa[i]

      else:
        dica += '_'

    print(f'Dica: {dica}')
    print(f'Você ainda tem {6 - tentativas} tentativas restantes\n')

print("A plavra e:",palavra)
