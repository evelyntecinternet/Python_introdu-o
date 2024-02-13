# Criar um  dicionário

dicionario = {}
dicionario = dict()
dicionario = {'nome': "Evelyn", 'idade': 23, "Altura": 1.65 }
print(dicionario)
print(dicionario['idade'])

# Adiconar elementos em um dicionário

dicionario["programador"] = True
print(dicionario)

dicionario['Altura'] = 2
print(dicionario)

# Iterando sobre um dicionário

for chave in dicionario:
    print(chave, dicionario[chave])

# Testando a existência de uma chave

print("peso" in dicionario) 
print("altura" in dicionario)       