# 1) Crie uma funcao que receba duas listas e verifique se elas são iguais. Cada elemento e sua ordem devem ser o mesmo. Retorne True ou False.

def comparar(lista1, lista2):
  if lista1 == lista2:
    return True
  else:
    return False

l1 = ['a', 'b', 'c']
l2 = ['a', 'b', 'c']

c = comparar(l1, l2)
print(c)

l2 = ['a', 'c', 'c']

c = comparar(l1, l2)
print(c)

# 2) Crie uma funcao que verifica se duas strings são palindromes perfeitas. Faca as 'limpeza'/sanitizacao necessarias.  Retorne True ou False.

def palindrome(palavra1, palavra2):
  palavra1 = palavra1.strip()
  palavra1 = palavra1.replace(' ', '')
  palavra1 = palavra1.lower()

  palavra2 = palavra2.strip()
  palavra2 = palavra2.replace(' ', '')
  palavra2 = palavra2.lower()

  if palavra1 == palavra2:
    return True
  else:
    return False

p1 = 'Natan'
p2 = 'natan'

p = palindrome(p1, p2)
print(p)