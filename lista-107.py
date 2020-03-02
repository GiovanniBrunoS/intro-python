###
# Exercicio
###

# 1) Imprima os metodos disponiveis para uma lista e para uma tupla.

list = []
tuple = ()
list_dir = dir(list)
tuple_dir = dir(tuple)
print(list_dir)
print(tuple_dir)

# 2) Faca um metodo para retornar apenas as diferencas entre as duas de metodos


def diff_methods(list1, list2):
    print("Métodos únicos de list: ", set(list1) - set(list2))
    print("Métodos únicos de tuple: ", set(list2) - set(list1))


diff_methods(list_dir, tuple_dir)

# 3) Adicione as coordenadas (latitude, longitude) para os dicts professor1, professor2 e professor3. Copie os dicts do arquivo 106.py

professor1 = {'id': 42, 'name': 'Alexandre Abreu', 'age': 30, 'state_origin': 'Minas Gerais', 'courses': ['Inteligência Artificial', 'Mineração de Dados', 'Programação para Internet I', 'Programação para Internet II']}
professor2 = {'id': 37, 'name': 'Denilson Barbosa', 'age': 40, 'state_origin': 'Paraná', 'courses': ['Inteligência Artificial', 'Banco de Dados I', 'Banco de Dados II', 'Programação para Internet I']}
professor3 = dict(id=28, name='Jorge Armino', idade=37, state_origin='Rio Grande do Sul', courses=['Filosofia', 'Informática e Sociedade'] )

professor1['coordinates'] = 0,0
professor2['coordinates'] = 0,0
professor3['coordinates'] = 0,0