# Verificação de Diferença: Crie um código que peça para o usuário inserir dois nomes. Depois verifique se os dois nomes são diferentes. Se forem, exiba "Os nomes digitados são diferentes.".

nome1 = str(input("Digite primeiro nome: "))
nome2 = str(input("Digite segundo nome: "))

if nome1 != nome2:
    print("Os nomes digitados são diferentes.")