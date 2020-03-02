###
# Exercicios
###

book1 = 'Homo Deus by Yuval Noah Harari, 2015'
book2 = 'Antifragile by Nassim Nicholas Taleb, 2012'
book3 = 'Fooled by Randomness by Nassim Nicholas Taleb, 2001'

palindrome_one = 'ovo'
palindrome_two = 'Natan'
palindrome_three = 'luz azul'
palindrome_four = 'caneta azul'

# 1) Extraia o titulo do livro da string

titulo_livro1, resto1 = book1.split("by")
titulo_livro2, resto2 = book2.split("by")
titulo_livro3, resto3 = book3.rsplit("by",1)

# 2) Salve o titulo de cada livro em uma variável

titulo_livro1 = titulo_livro1.strip()
titulo_livro2 = titulo_livro2.strip()
titulo_livro3 = titulo_livro3.strip()

print(titulo_livro1)
print(titulo_livro2)
print(titulo_livro3)

autor_livro1, ano_livro1 = resto1.split(",")
autor_livro2, ano_livro2 = resto2.split(",")
autor_livro3, ano_livro3 = resto3.split(",")

autor_livro1 = autor_livro1.strip()
autor_livro2 = autor_livro2.strip()
autor_livro3 = autor_livro3.strip()
ano_livro1 = ano_livro1.strip()
ano_livro2 = ano_livro2.strip()
ano_livro3 = ano_livro3.strip()

# 3) Quantos caracteres cada título tem?

print(len(titulo_livro1))
print(len(titulo_livro2))
print(len(titulo_livro3))

# 4) Imprima com a formatacao: {Titulo} - {Autor}, {Ano}

print("{} - {}, {}".format(titulo_livro1, autor_livro1, ano_livro1))
print("{} - {}, {}".format(titulo_livro2, autor_livro2, ano_livro2))
print("{} - {}, {}".format(titulo_livro3, autor_livro3, ano_livro3))

# 5) Verifique se uma palavra é uma palindrome perfeita.

palindrome_two = palindrome_two.lower()
palindrome_three = palindrome_three.replace(" ","")
palindrome_four = palindrome_four.replace(" ","")

print(palindrome_one == palindrome_one[::-1])
print(palindrome_two == palindrome_two[::-1])
print(palindrome_three == palindrome_three[::-1])
print(palindrome_four == palindrome_four[::-1])

# Palindrome perfeito sao palavras que ao serem escritas em ordem reversa resultam na mesma palavra.
# Ignore espacos e caixa alta
