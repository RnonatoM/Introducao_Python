
'''for variavel in range(10): #range = "faixa em portugues"
    print(variavel)'''


'''for variavel in range(5, 11):
    print(variavel)'''

'''for variavel in range(1, 12, 3):
    print(variavel)'''


'''nota1 = float(input('Informe sua nota 1: '))
nota2 = float(input('Informe sua nota 2: '))
nota3 = float(input('Informe sua nota 3: '))'''

soma = 0

for i in range(1, 4): #Outra forma, for i in range(3):
    nota = float(input(f'Informe a sua nota [i]: '))

    soma = soma + nota 

print(soma / 3)