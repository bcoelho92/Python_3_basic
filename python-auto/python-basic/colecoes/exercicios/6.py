'''
Crie um sistema de login com dois dicionários: um que guarda as credenciais corretas, e outro dicionário que guarde as informações inseridas pelo usuário. Peça ao usuário para digitar o usuário e senha, e verifique se está correto de acordo com o primeiro dicionário.
Se o usuário e a senha estão corretos → "Login bem-sucedido"
Senão → "Usuário ou senha incorretos"
'''

login_db = {
    'user':'admin',
    'password':'admin123'
}
logoin_usuario = {
    'user': input('Usuario> '),
    'password':input('Sesnha> ')
}

if logoin_usuario['user'] == login_db['user'] and logoin_usuario['password'] == login_db['password']:
    print("Login bem-sucedido")
    # Acessa as informações e etc.
else:
    print("Usuário ou senha incorretos!")