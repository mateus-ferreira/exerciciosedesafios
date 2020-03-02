book1 = 'Homo Deus by Yuval Noah Harari, 2015'
book2 = 'Antifragile by Nassim Nicholas Taleb, 2012'
book3 = 'Fooled by Randomness by Nassim Nicholas Taleb, 2001'

# 1) Extraia o titulo do livro da string
sbook1 = book1.split('by')
sbook2 = book2.split('by')
sbook3 = book3.split('by')

# 2) Salve o titulo de cada livro em uma variável
tbook1 = sbook1[0]
tbook2 = sbook2[0]
tcbook3 = '{} by {}'.format(sbook3[0], sbook3[1])
tbook3 = tcbook3

print('book1 = ', tbook1)
print('book2 = ', tbook2)
print('book3 = ', tbook3)

# 3) Quantos caracteres cada título tem?
tambook1 = len(tbook1)
tambook2 = len(tbook2)
tambook3 = len(tbook3)

print('tamanho titulo book1 = ', tambook1)
print('tamanho titulo book2 = ', tambook2)
print('tamanho titulo book3 = ', tambook3)

# 4) Imprima com a formatacao: {Titulo} - {Autor}, {Ano}
abook1 = sbook1[1].split(',')
abook2 = sbook2[1].split(',')
abook3 = sbook3[2].split(',')

newbook1 = '{} - {}, {}'.format(tbook1, abook1[0], abook1[1])
newbook2 = '{} - {}, {}'.format(tbook2, abook2[0], abook2[1])
newbook3 = '{} - {}, {}'.format(tbook3, abook3[0], abook3[1])
print(newbook1)
print(newbook2)
print(newbook3)

# 5) Verifique se uma palavra é uma palindrome perfeita.
# Palindrome perfeito sao palavras que ao serem escritas em ordem reversa,
# resultam na mesma palavra.
# Ignore espacos e caixa alta

palindrome_one = 'ovo'
palindrome_two = 'Natan'
palindrome_three = 'luz azul'
palindrome_four = 'caneta azul'

p_one = palindrome_one[::-1]
if p_one == palindrome_one:
  print('palindrome perfeita 1')
else:
  print('imperfeita 1')

p_two = palindrome_two[::-1]
if p_two.islower() == palindrome_two.islower():
  print('palindrome perfeita 2')
else:
  print('imperfeita 2')

palindrome_three = palindrome_three.replace(' ', '')
p_three = palindrome_three[::-1]
if p_three == palindrome_three:
  print('palindrome perfeita 3')
else:
  print('imperfeita 3')

palindrome_four = palindrome_four.replace(' ', '')
p_four = palindrome_four[::-1]
if (p_four == palindrome_four):
  print('palindrome perfeita 4')
else:
  print('imperfeita 4')