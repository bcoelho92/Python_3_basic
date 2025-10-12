# def saudacao():
#     print("Olá, seja bem-vindo(a)!")

# def saudacao(nome):
#     print(f"Olá {nome}, seja bem-vindo(a)!")
# saudacao("Batata")

# def soma(n1, n2):
#     resultado = n1 + n2
#     print(f'O resultado da soma de {n1} e {n2} é {resultado} !')
# soma(10,5)

# def soma(n1, n2):
#     resultado = n1 + n2
#     return resultado
# print(soma(10,5))

def calculo_desconto(preco, percentual):
    desconto = preco * (percentual / 100)
    preco_final = preco - desconto
    return preco_final
print(f'Valor final com desconto: R$ {calculo_desconto(200, 34)}')
