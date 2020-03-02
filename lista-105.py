###
# Exercicios
###

# Usando a lista: ['a','b','c']
# 1) Faca um loop para retornar: ['A','B','C']


def upper_loop(l):
    return [letter.upper() for letter in l]


letters = ['a', 'b', 'c']
print(upper_loop(letters))

# Usando os numeros: [0, 1, 3, 4, 5]
# 2) Faca um loop para retornar a soma de todos os elementos da listas


def sum_loop(l):
    sum = 0
    for num in l:
        sum += num
    return sum


numbers = [0, 1, 3, 4, 5]
print(sum_loop(numbers))

# 3) Faca um loop para retornar apenas os numeros impares


def odd_loop(l):
    return [num for num in l if num % 2]


print(odd_loop(numbers))

# usando a string: 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut
# labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip
# ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat
# nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id
# est laborum.'
# 4) Conte quantas palavras de tamanho >= 5 existe nessa string

string = "Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et " \
         "dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex " \
         "ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu " \
         "fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt " \
         "mollit anim id est laborum."

string_treated = string.replace(",", "")
string_treated = string_treated.replace(".", "")
string_split = string_treated.split()

print(len([word for word in string_split if len(word) >= 5]))

# 5) Usando list comprehension, crie uma lista com os multiplos de 3 de 0 ate 100

print([num for num in range(0,100) if not num % 3])

# Faca uma funcao para encontrar os numeros primos no intervalo [2, 10), mas nao utilize a clausula else do for


def prime_loop():
    prim = []
    for i in range(2,10):
        for j in range(2,i+1):
            if i == j:
                prim.append(i)
                break
            elif i % j == 0:
                break
    print(prim)


prime_loop()
