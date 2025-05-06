def cadastrar_aluno(nome,email,serie):
    alunos = []

    aluno = {
        "nome": nome,
        "serie": serie,
        "email": email
}

    alunos.append(aluno)

    return alunos

print(cadastrar_aluno("Victo", "victo@victo.com", "3° TB"))