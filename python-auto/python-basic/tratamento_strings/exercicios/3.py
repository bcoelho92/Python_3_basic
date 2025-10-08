# Exercício 3 – Detectando palavras proibidas
# Peça ao usuário para escrever uma mensagem. Verifique se ela contém a palavra "bomba", e imprima um alerta se sim.

proibida = "bomba"
frase = str(input("Digite uma frase: "))
if proibida in frase:
    print(f"A palavra '{proibida}'era uma vez bo é proibida!")