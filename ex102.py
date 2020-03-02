days_list = ['mon','tues','wed','thurs','fri', 'sat', 'sun']
list = ['a', 1, 3.14159265359]

print(days_list)
print(list)

# Como selecionar 'wed' pelo indice?
print(days_list[2])

# Como verificar o tipo de 'mon'?
print(type(days_list[0]))

# Como separar 'wed' até 'fri'?
days = days_list[2:4] #sem incluir 'fri'
days = days_list[2:5] #incluindo 'fri'
print(days)

# Quais as maneiras de selecionar 'fri' por indice?
print(days_list[4])
print(days_list[4:5])

# Qual eh o tamanho dos dias e days_list?
print(len(days_list[:]))
print(len(days_list[0]))
print(len(days_list[1]))
print(len(days_list[2]))
print(len(days_list[3]))
print(len(days_list[4]))
print(len(days_list[5]))
print(len(days_list[6]))

# Como inverter a ordem dos dias?
days_list_reverse = days_list[::-1]
print(days_list_reverse)

# Como inserir a palavra 'zero' entre 'a' e 1 de list?
list.insert(1, "zero")
print(list)

# Como atribuir o ultimo elemento de list na variavel ultimo_elemento e remove-lo de list?
ultimo_elemento = list[-1]
print(ultimo_elemento)
del(list[-1])
print(list)

# Como limpar list?
del(list[:])
print(list)

# Como deletar list?
del(list)