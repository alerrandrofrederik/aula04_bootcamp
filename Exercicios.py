# Exercícios de Listas e Dicionários

# 1 - Crie uma lista com os números de 1 a 10 e use um loop para imprimir cada número elevado ao quadrado.

# numeros: list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# for i in numeros:
#     print(i ** 2)

# 2 - Dada a lista ["Python", "Java", "C++", "JavaScript"], remova o item "C++" e adicione "Ruby".

# lista: list = ["Python", "Java", "C++", "JavaScript"]

# lista.remove('C++')
# lista.append('Ruby')

# print(lista)

# 3 - Crie um dicionário para armazenar informações de um livro, incluindo título, autor e ano de publicação. Imprima cada informação.

livro: dict = {
'título': 'Harry Potter',
"autor": 'J.K. Rowling',
"ano": 1997
}

for chave, valor in livro.items():
    print(f'{chave}: {valor}')


# 4 - Escreva um programa que conta o número de ocorrências de cada caractere em uma string usando um dicionário.
# 5 - Dada a lista ["maçã", "banana", "cereja"] e o dicionário {"maçã": 0.45, "banana": 0.30, "cereja": 0.65}, calcule o preço total da lista de compras.