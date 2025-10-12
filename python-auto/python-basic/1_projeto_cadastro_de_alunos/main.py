alunos = []

def cadastro_aluno():
    nome = input("Digite o nome do aluno: ")
    idade = int(input("Digite a idade do aluno: "))
    
    while True:
        nota = float(input("Digite a nota do aluno: "))
        if nota >= 0 and nota <= 10:
            break
        else:
            print("\nNota inválida. Digite uma nota entre 0 e 10.")
    cadastro = {
        'nome': nome,
        'idade': idade,
        'nota': nota
    }
    alunos.append(cadastro)

def listar_alunos():
    if len(alunos) == 0:
        print("\nNão tem alunos cadastrados.") 
        return
    for aluno in alunos:
        print(f'\nAluno: {aluno["nome"]}\nIdade: {aluno["idade"]}\nNota: {aluno["nota"]}\n')
    

def procurar_aluno(nome_aluno):
    for aluno in alunos:
        if aluno['nome'].lower() == nome_aluno.lower():
            print(f'\nAluno: {aluno["nome"]}\nIdade: {aluno["idade"]}\nNota: {aluno["nota"]}\n')
            return
    print("\nAluno não encontrado.")

def deletar_aluno(nome_aluno):
    if len(alunos) == 0:
        print("\nSem alunos cadastrados.")
        return
    for aluno in alunos:
        if aluno['nome'].lower() == nome_aluno.lower():
            alunos.remove(aluno)
            print(f"\nAluno(a) {nome_aluno} deletado(a) com sucesso!")
            break
    else:
        print("\nEsse aluno não foi encontrado.")


def media_de_notas():
    if len(alunos) == 0:
        print("\nSem alunos cadastrados.")
        return
    soma = 0
    for aluno in alunos:
        soma += aluno['nota']
    media = soma / len(alunos)
    print(f"\nA média geral das notas é: {media:.2f}")

while True:
    opcao = int(input("\nO que deseja fazer?\n\n1.Adicionar aluno\n2.Listar todos os alunos\n3.Buscar aluno pelo nome\n4.Remover aluno\n5.Mostrar média geral das notas\n6.Sair\n\n"))
    match opcao:
        case 1:
            cadastro_aluno()
        case 2:
            listar_alunos()
        case 3:
            nome_aluno = input("Qual aluno deseja buscar?: ")
            procurar_aluno(nome_aluno)
        case 4:
            nome_aluno = input("Qual aluno deseja remover?: ")
            deletar_aluno(nome_aluno)
        case 5:
            media_de_notas()
        case 6:
            break