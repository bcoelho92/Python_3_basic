# LISTA
frutas = ['banana', 'maçã', 'caju', 2.3]
print(frutas)

# # print com base no index
# print(frutas[1:3])

# # adicionar e removendo item da lista 
# frutas.append("cacau")
# print(frutas)
# frutas.remove(2.3)
# print(frutas)

# # substituir item
# frutas[1] = 'melão'
# print(frutas)

# # adicionar item com base no index
# frutas.insert(1,'chocolate')
# print(frutas)

# # remover item com base no index
# frutas.pop(2)
# print(frutas)
# fruta_removida = frutas.pop(2)
# print(f"fruta removida: {fruta_removida}")
# print(frutas)

# # ordenar lista - funciona apenas com 1 type 'str' or 'int' or float' etc
# frutas.sort()
# print(frutas)

# # index localizar posição do item
# print(frutas.index('banana'))

# # limpar lista
# frutas.clear()
# print(frutas)

# # contagem de quantas vezes um item aparece
# print(frutas.count('banana'))

# # Como criar uma copia de uma lista
# # modo que replica uma lista causando a a mudança nas duas listas
# frutas2 = frutas
# frutas.append('abacate')
# print(frutas)
# print(frutas2)

# # maneira correta de copiar sem replicar as mudnaças
# frutas2 = frutas
# frutas3 = frutas2.copy()
# frutas3.append('churrasco')
# print(frutas)
# print(frutas2)
# print(frutas3)

# # contar itens
# print(len(frutas))

# TUPLAS 

# # SÃO IMUTAVEIS NÃO PODEM SE MODIFICADAS
# # Oque pode ser feito - .copy .sort .count .index etc..
granja = ('galo', 'galinha', 'ovo')
print(granja)