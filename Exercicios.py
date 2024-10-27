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

# livro: dict = {
# 'título': 'Harry Potter',
# "autor": 'J.K. Rowling',
# "ano": 1997
# }

# for chave, valor in livro.items():
#     print(f'{chave}: {valor}')


# 4 - Escreva um programa que conta o número de ocorrências de cada caractere em uma string usando um dicionário.

# texto: str = 'O rato roeu a roupa do rei de roma'
# dicionario: dict = {}

# for char in texto:
#     if char in dicionario:
#         dicionario[char] += 1
#     else: 
#         dicionario[char] = 1

# print(dicionario)


# 5 - Dada a lista ["maçã", "banana", "cereja"] e o dicionário {"maçã": 0.45, "banana": 0.30, "cereja": 0.65}, calcule o preço total da lista de compras.

# produtos_comprados: dict = {"maçã": 0.45, "banana": 0.30, "cereja": 0.65}

# valor_compras: list = produtos_comprados.values()

# total_compra: float = sum(valor_compras)

# print(total_compra) 

# Exercícios com Dicionários
# Objetivo: Dada uma lista de dicionários representando produtos, atualizar o preço de um produto específico.

# produtos = [
#     {"id": 1, "nome": "Teclado", "preço": 100},
#     {"id": 2, "nome": "Mouse", "preço": 80},
#     {"id": 3, "nome": "Monitor", "preço": 300}
# ]

# produtos[1]["preço"] = 50 #altera

# print(produtos[1]["preço"])

# trabalhando com csv direto no python
import csv

# Caminho para o arquivo CSV
caminho_arquivo = 'exemplo.csv'

# Inicializa uma lista vazia para armazenar os dados
dados = []

# Usa o gerenciador de contexto `with` para abrir o arquivo
with open(caminho_arquivo, mode='r', encoding='utf-8') as arquivo:
    # Cria um objeto leitor de CSV
    leitor_csv = csv.DictReader(arquivo)
    
    # Itera sobre as linhas do arquivo CSV
    for linha in leitor_csv:
        # Adiciona cada linha (um dicionário) à lista de dados
        dados.append(linha)

# Exibe os dados lidos do arquivo CSV
for registro in dados:
    print(registro)
