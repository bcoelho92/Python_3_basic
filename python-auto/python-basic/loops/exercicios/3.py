'''
Peça ao usuário que vá digitando valores para guardar no cofrinho (em reais).
Quando o usuário digitar 0, o programa para e mostra o total economizado.
'''

cofrinho = 0
soma = None
while soma != 0:
      print('''
Bem-vindo(a) ao cofrinho!
Digite o valor que deseja guardar, ex: 10.50 ou 10 reais.
para finalizar o cofrinho digite 0.
            ''')
      soma = float(input('Digite um valor em reais : '))
      print('\nBom trabalho!')
      cofrinho += soma

print(f'Esse é o total do seu cofrionho R$ {cofrinho}')