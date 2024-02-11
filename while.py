numero_sorteado = 15

numero_escolhido = int(input("Informe um número ente 1 e 20: "))

while numero_escolhido != numero_sorteado:
    print("Você errou,tente novamente...")

    numero_escolhido = int(input("Informe um número ente 1 e 20: "))

print("Parabéns! Você acertou!")

#Exemplo 2 : Contador

contador = 0
while contador < 10:
    print(contador)

    contador = contador + 1
