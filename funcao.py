# Criação de Funções

# Função Inicial

def saudacao():
    print("Seja Bem vindo(a)!")
    print("Olá, é um prazer ter você fazendo parte  desse curso!")

saudacao()

# Função com parâmetros

def saudacao(nome,curso):
     print(f"Seja Bem vindo(a), {nome}!")
     print(f"Olá, é um prazer ter você fazendo parte  do curso de {curso}!")
saudacao("Evelyn","Python")
saudacao("Maria","JavaScript")

# Função com parâmetros default

def saudacao(nome,curso= "Python"):
     print(f"Seja Bem vindo(a), {nome}!")
     print(f"Olá, é um prazer ter você fazendo parte  do curso de {curso}!")

saudacao("Evelyn","C++")

# Função com retorno

def soma(num1,num2):
     return num1 + num2

resultado = soma(5, 10)
print("O resultado da soma é: ",resultado)

def calculadora(num1,num2,operacao= "+"):
     if operacao == "+":
          return num1 + num2
     elif operacao == "-":
          return num1 - num2
     elif operacao == "/":
          return num1 / num2
     elif operacao == "*":
          return num1 * num2
resultado = calculadora(10, 5, "*")  
print("Resultado: ",resultado)   
     