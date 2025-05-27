import json
import os

filmes = 'cadastro_filmes.json'

def carregar_dados():
    if os.path.exists(filmes):
        with open(filmes, 'r', encofing="utf-8") as arq_json:
            return json.load(arq_json)
    else:
        return []
    
def obter_dados():
    nome_filme = input("informe o nome do filme: ")
    classificacao = input("informe a classificação do filme: ")
    descricao = input("informe a descrição do filme: ")
    categoria = input("informe a categoria do filme: ")

    data_filme = {
        "nome_filme": nome_filme,
        'classificacao': classificacao,
        "descricao": descricao,
        "categoria": categoria,
    }

    return data_filme

def cadastrar_filme(receber_filme):
    db_filmes = carregar_dados()
    db_filmes.append(receber_filme)

    with open(filmes, "w", encoding="utf-8") as arq_json:
        json.dump(db_filmes, arq_json, indent=4, ensure_ascii=False)

def mostrar_filmes(filmes):
    if filmes:
        for filme in filmes:
            print(f"""
                nome do filme {filme["nome_filme"]}
                classificação do filme {filme["classificacao"]}
                descrição do filme {filme["descrição"]}
                categotia do filme {filme["categoria"]}
            """)
    else:
        print("não exite nenhum filme cadastrado.")


def iniciar_sistema():
    db_filmes = carregar_dados()

    while True:
        print("")
        print("="*80)
        print("opção 1 - mostra lista de filmes")
        print("opção 2 - cadastra filme")
        print("opção 3 - sair do sistema")
        print("="*80)

        opcao = input("escolha uma das opções no menu: ")

        if opcao == "1":
            mostrar_filmes()
        elif opcao == "2":
            cadastrar_filme()
        elif opcao == "3":
            print("sistema finalizado!")
            break
        else:
            print("opção invalida, escolha umadas opções no menu.")

iniciar_sistema()