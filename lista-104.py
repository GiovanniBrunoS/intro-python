###
# Exercicios
###

# 1) Crie uma funcao que receba duas listas e verifique se elas são iguais. Cada elemento e sua ordem devem ser o
# mesmo. Retorne True ou False.


def list_check(x, y):
    if x == y:
        return True
    else:
        return False

# 2) Crie uma funcao que verifica se duas strings são palindromes perfeitas. Faca as 'limpeza'/sanitizacao
# necessarias.  Retorne True ou False.


def string_check(x, y):
    y = y[::-1]
    x = x.replace(" ","")
    y = y.replace(" ","")
    x = x.lower()
    y = y.lower()
    if x == y:
        return True
    else:
        return False

#
# OBS.: Utilize apenas o que foi estudado ate agora
