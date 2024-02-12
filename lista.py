# Antes
nota1 = 7.9
nota2 = 9.7
nota3 = 8.2

# Com lista
notas = [7.9,9.7,8.2]

# Criando Listas
lista = []
lista = list()
lista = [17,"Evelyn",5.1233,True]
lista_de_listas = [10,[1,2,3]]

# Indexação e Slices(Fatiamentos)

lista = [22,"Evelyn",5.1254,False]

print(lista[0])
print(lista[1])
print(lista[2])
print(lista[3])
#print(lista[4])
print(lista[-1])

# Slices
lista = [10,50,30,40,25,60,5]
print(lista[0:3])
print(lista[3:6])
print(lista[3:])
print(lista[2:6:2])

# INTERAÇÕES com FOR

# 1. utilizando os próprios elementos de uma lista
for elemento in lista:
    print(elemento)

# 2. Utilizando os índices
    
print("Comprimento da lista: ",len(lista))    
for i in range(len(lista)):
    print(lista[i])
# métodos de listas

lista = [1,3,12,8,2]    

# APPEND
print("Antes do Append:",lista)

lista.append(4)

print("Depois do Append:",lista)

# Insert

lista.insert(2, 10)  
print("Depois do Insert:",lista)  

# Extend
lista2 = [1,2,3]

lista.extend(lista2)
print("Depois do Extend:",lista)

# POP

lista.pop()
print("Lista após o POP:",lista)

lista.pop(0)
print("Lista após pop:",lista)

# Remove

lista.remove(3)
print("Depois do remove:",lista)

# Count
print("Quantidade de 2 na lista:",lista.count(2))

# Index
print('Ínice do elemento 12;',lista.index(12))

# Sort
lista.sort(reverse = True)

print(lista)

# Funções para Listas

# len
print(len(lista))

# Sum
print(sum(lista))

# MAX
print("Maior elemento da lista:",max(lista))

# min
print("Menor elemento da lista:",min(lista))