from exercicio04 import media

alunos = []

def obter_dados_aluno():
    nome_aluno = input("digite o nome do aluno: ")
    serie_aluno = input("digite a série do aluno: ")
    email_aluno = input("digite o email do aluno: ")
    nota01_aluno = int(input("digite a 1° nota do aluno: "))
    nota02_aluno = int(input("digite a 2° nota do aluno: "))
    nota03_aluno = int(input("digite a 3° nota do aluno: "))

    return cadastrar_aluno(nome_aluno, serie_aluno, email_aluno, nota01_aluno, nota02_aluno, nota03_aluno)


def cadastrar_aluno(nome,email,serie, nota01=0, nota02=0, nota03=0):

    notas = [nota01, nota02, nota03]

    aluno = {
        "nome": nome,
        "serie": serie,
        "email": email,
        "notas": notas, 
        "media": media(notas)

}

    alunos.append(aluno)

    return alunos


def mostrar_dados_alunos(dados_alunos):
    for aluno in dados_alunos:
     print(f"nome do aluno: {aluno["nome"]}  email do aluno: {aluno["email"]} | serie do aluno: {aluno["serie"]} | notas do aluno: {aluno["notas"]} | media do aluno: {aluno["media"]}")

    return

def iniciar_sistena():
   while True:
        print("="*80)
        print("opação 1 => mostrar lista de alunos casdrastado: ")
        print("opação 2 => mostrar lista de aluno: ")
        print("opação 3 => sair do sistema: ")
        print("="*80)

        opcao = input("escolha uma das opções acima: ")

        if opcao == "1":
            mostrar_dados_alunos(alunos)
        elif opcao == "2":
            obter_dados_aluno
        else:
            print("sistema finalizado: ")

iniciar_sistena()