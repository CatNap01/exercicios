import json
import os

veiculos = 'cadastro_veiculos.json'

def carregar_dados():
    if os.path.exists(veiculos):
         with open(veiculos, 'r', encofing="utf-8") as veículos_json:
            return json.load(veículos_json)
    else:
        return []
    
def obter_informacoes():
    Marca_do_veículo = input("informe a Marca do veículo")

    Modelo_do_veículo = input("informe o modelo do veículo")

    Ano_de_fabricação = input("informe o ano de fabricação do veículo")

    Cor_do_veículo = input("informe as cor que o veículos possue")


    informacao_do_veiculo ={
        "marca": Marca_do_veículo,
        "modelo": Modelo_do_veículo,
        "ano": Ano_de_fabricação,
        "cor": Cor_do_veículo
}

    return informacao_do_veiculo

def cadastrar_veiculo(receber_veiculo):
    db_veiculos = carregar_dados()
    db_veiculos.append(receber_veiculo)

    with open(veiculos, "w", encoding="utf-8") as veículos_json:
        json.dump(db_veiculos, veículos_json, indent=4, ensure_ascii=False)

def mostrar_veiculos(veiculos):
    if veiculos:
        for veiculo in veiculos:
            print(f"""
                marca do veiculo {veiculo["Marca_do_veículo"]}
                modelo do veiculo {veiculo["Modelo_do_veículo"]}
                ano do veiculo {veiculo["Ano_do_veículo"]}
                cor do veiculo {veiculo["Cor_do_veículo"]}
            """)
    else:
        print("não exite nenhum filme cadastrado.")


def iniciar_sistema():
    db_veiculos = carregar_dados()

    while True:
        print("")
        print("="*80)
        print("opção 1 - mostra lista dos veículos")
        print("opção 2 - cadastrar veículos")
        print("opção 3 - sair do sistema")
        print("="*80)

        opcao = input("escolha uma das opções no menu: ")

        if opcao == "1":
            mostrar_veiculos(db_veiculos)
        elif opcao == "2":
            cadastrar_veiculo()
        elif opcao == "3":
            print("sistema finalizado!")
            break
        else:
            print("opção invalida, escolha umadas opções no menu.")

iniciar_sistema()