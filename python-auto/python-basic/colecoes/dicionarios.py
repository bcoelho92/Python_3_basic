# dicionario

cadastro = {
    'nome':'Bruno',
    'idade':33,
    'cidade':'São Paulo',
    'carros':['Uno', 'Corsa', 'palio'],
    'contatos':{
        'casa':'11 91234-5678',
        'trabalho':'11 98765-4321'
    }
}
print(cadastro)
print()

# # acessando pela chave
# print(cadastro['cidade'])

# # alterando informação
# cadastro['cidade'] = 'Jandira'
# print(cadastro['cidade'])

# # para deletar chave/valor
# del cadastro['cidade']
# print(cadastro)

# # acessar uma list dentro do dict
# print(cadastro['carros'])
# print(cadastro['carros'][2])

# # acessar uma dict dentro de outro dict
# print(cadastro['contatos'])
# print(cadastro['contatos']['casa'])

# # trazer as chaves
# print(cadastro.keys())
# # trazer valores 
# print(cadastro.values())

# # encapisular keys em uma lista
# keys_list = list(cadastro.keys())
# print(keys_list)
# print(keys_list[2])

# # utilizar em loop
# print(cadastro.items())

# # busca sem retornar erro apenas None
# print(cadastro.get('telefones', 'item não existe!'))

# # adicionar e remorver item da dict
# cadastro['error'] = '404 - not found'
# cadastro.update({'salario': 2501, 'jogo': 'got of war'}) # mais de 1 item
# print(cadastro)
# cadastro.pop('error')
# print(cadastro)
# # deletar o contato 'casa' de dentro da dict contatos
# cadastro['contatos'].pop('casa')
# print(cadastro)
