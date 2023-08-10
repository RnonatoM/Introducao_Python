numero_sorteado = 15

numero_escolhido = int(input('Informe um número entre 1 e 20: '))

"""if numero_sorteado == numero_escolhido:
    print('Voce acertou!')
else:
    print('voce errou!')"""

while numero_escolhido != numero_sorteado:
    print('voce errou o número, tente novamente...')

    numero_escolhido = int(input('Informe um numero entre 1 e 20: '))

print('Parabéns, jogado! Voce acertou!')


# Exemplo 02: ESTRUTURA COM COMPUTADOR 
contador = 0

while contador < 5:
    print(contador)

    contador = contador + 1