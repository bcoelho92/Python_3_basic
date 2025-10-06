#Crie um código onde é solicitado para o usuário inserir dois valores: o ano atual, e o ano de nascimento. O sistema deve calcular quantos anos ele tem de acordo com essas informações e exibir no console.

from datetime import datetime

# ano_atual_syst = str(datetime.now().year)
ano_atual = int(input("Informe ano atual: "))
ano_nesc = int(input("Informe ano do seu nascimento: "))

print(f"Essa é sua idade: {ano_atual - ano_nesc} Ano atual {ano_atual} - ano nasciimento {ano_nesc}." )