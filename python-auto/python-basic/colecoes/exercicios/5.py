'''Peça para o usuário digitar nome e idade. Guarde esses dados em um dicionário chamado usuario.
Depois, verifique se a idade é maior ou igual a 18:

Se sim, imprima: "Acesso liberado para {nome}"

Se não, imprima: "Acesso negado para {nome}"'''

usuario = {
    "nome":"",
    "idade":""
}

# nome = "Bruno"
# idade = 33

nome = input('Digite seunome: ')
idade = int(input('Digite sua idade: '))

# usuario['nome'] = nome
# usuario['idade'] = idades

usuario.update({'nome':nome, 'idade':idade})
# print(usuario)
    
if usuario['idade'] >= 18:
    print(f"Acesso liberado para {usuario['nome']}")
else:
    print(f"Acesso negado para {usuario['nome']}")