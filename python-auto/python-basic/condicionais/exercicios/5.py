# Seu programa deve verificar se o usuário tem direito a frete grátis. As regras são:

# O valor da compra deve ser maior ou igual a 100

# E o cliente precisa estar cadastrado no programa de fidelidade

# Se as duas condições forem verdadeiras, mostre: "Frete grátis aplicado!"
# Caso contrário: "Frete não disponível gratuitamente."

Compra_min = 100 
cli_fidelidade = True

valor_compra = float(input("informe o valor da compra: "))

if valor_compra > Compra_min and cli_fidelidade:
    print("Que top, frete grátis aplicado!")
else:
    print("Frete não disponível gratuitamente.")
