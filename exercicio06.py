clientes =[]

def obter_dados_de_cliente():
    nome = input("digite seu nome completo: ")
    cpf = int(input("digite seu CPF: "))
    rg = input("digite seu RG: ")
    nasc = int(input("digite sua data de nacimento: "))
    endereco = input("digite seu endereço: ")
    cidade =  input("digite sua cidade: ")
    estado = input("digite seu estado: ")
    telefone = int(input("digite seu teledone: "))
    celular = int(input("digite seu teledone: "))
    email = input("digite seu email: ")

    cliente = {
        "nome": nome,
        'cpf':cpf,
        'rg': rg,
        'nasc': nasc,
        'endereco': endereco,
        'cidade': cidade,
        'estado': estado,
        'telefone': telefone,
        "celular": celular,
        "email": email
    }

    return cliente

def cadastrar_cliente(dados_cliente):
    clientes.append(dados_cliente)

    return clientes

def mostrar_dados_clietes(dados_clientes):
    for cliente in dados_clientes:
        print(f"""
                Nome do Cliente: {cliente["nome_do_cliente"]}
                CPF do Cliente: {cliente["nome_do_cliente"]}
                RG do Cliente: {cliente["nome_do_cliente"]}
                Data de nacimento do Cliente: {cliente["nome_do_cliente"]}
                Endereço do Cliente: {cliente["nome_do_cliente"]}
                Cidade do Cliente: {cliente["nome_do_cliente"]}
                Estado do Cliente: {cliente["nome_do_cliente"]}
                Telefone do Cliente: {cliente["nome_do_cliente"]}
                celular do Cliente: {cliente["nome_do_cliente"]}
                email do Cliente: {cliente["nome_do_cliente"]}
              """)
        
def iniciar_sstema():
    while True:
        print("")
        print("="*80)
        print("opção 1 - mostrar lista de cliente")
        print("opção 2 - cadastrar clientes")
        print("opção 3 - sair do sistema")
        print("="*80)

        opcao = input("escolha umas das opçôes do menu: ")

        if opcao == "1":
            mostrar_dados_clietes(clientes)
        elif opcao == "2":
            cadastrar_cliente(obter_dados_de_cliente())
        elif opcao == "3":
            print("sistema finalizado")
            break
        else:
            print("opção invalida, escolha umas das opçôes no menu.")