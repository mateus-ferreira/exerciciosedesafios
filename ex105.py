## Usando a lista: ['a','b','c']
# 1) Faca um loop para retornar: ['A','B','C']

letras = ['a', 'b', 'c']

for i in range(3):
  letras[i] = letras[i].upper()

print(letras)

## Usando os numeros: [0, 1, 3, 4, 5]
# 2) Faca um loop para retornar a soma de todos os elementos da listas
# 3) Faca um loop para retornar apenas os numeros impares

numeros = [0, 1, 3, 4, 5]
soma = 0
for i in range(5):
  soma += numeros[i]

print(soma)


for i in range(5):
  if numeros[i] != 0:
    if numeros[i]%2 == 1:
      print(numeros[i])

## usando a string: 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'
# 4) Conte quantas palavras de tamanho >= 5 existe nessa string

string = 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'

string = string.replace(',', '')
string = string.replace('.', '')
stringseparada = string.split(' ')

tamanho = 0

for i in range(len(stringseparada)):
  if len(stringseparada[i]) >= 5:
    tamanho += 1

print(tamanho,  'palavras com 5 ou mais letras')

# 5) Usando list comprehension, crie uma lista com os multiplos de 3 de 0 ate 100

lista = [i*3 for i in range(34)]
print(lista)

# Faca uma funcao para encontrar os numeros primos no intervalo [2, 10), mas nao utilize a clausula else do for

contador = 0

for i in range(2,10):
  for j in range(2,i):
    if i%j == 0:
      contador += 1
  
  if contador == 0:
    print(i, ' é primo')