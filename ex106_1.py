import csv
# 1) Implemente o metodo define_default_city de acordo com a docstring definida no inicio da funcao. Utilize a clausula else no loop implementado.

def define_default_city(state):
  with open('capitais-BR.csv') as arquivo:
    csv_reader = csv.reader(arquivo)
    for row in csv_reader:
      for a in row:
        if a.split(";")[0] == state:
          return a.split(";")[1]
          break



professor1 = {'id': 42, 'name': 'Alexandre Abreu', 'age': 30, 'state_origin': 'Minas Gerais', 'courses': ['Inteligência Artificial', 'Mineração de Dados', 'Programação para Internet I', 'Programação para Internet II']}

professor2 = {'id': 37, 'name': 'Denilson Barbosa', 'age': 40, 'state_origin': 'Paraná', 'courses': ['Inteligência Artificial', 'Banco de Dados I', 'Banco de Dados II', 'Programação para Internet I']}

professor1['city_origin'] = define_default_city(professor1['state_origin'])

professor2['city_origin'] = define_default_city(professor1['state_origin'])
