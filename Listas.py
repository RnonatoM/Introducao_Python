# > Listas 

# Antes 
nota1 = 7.9
nota2 = 9.7
nota3 = 8.2

# com listas 
notas = [7.9, 9.7, 8.2]

#criando listas
lista = []
lista = list()
lista = [23, 'Raimundo', 3.141559, False]
lista_de_listas = [10, [1,2,3]]


# Indexação e Slices (fatiamento)

lista = [10, 'Raimundo', 3.1415, True]
print(lista[0])
print(lista[1])
print(lista[2])
print(lista[3])






# Slices 
lista = [10, 50, 30, 40, 25, 60, 5]
print(lista[0:3])
print(lista[3:6])
print(lista[3:])
print(lista[2:6:2])




# > iteração com for 
# 1. Utilizando os próprios elementos da lista
for elementos in lista:
    print(elementos)

# 2. Utilizando os indices 
print("Comprimento da Lista: ", len(lista)) #lem = comprimento. 

for i in range(len(lista)):
    print(i)

