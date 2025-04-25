from src.infra.db import conectar, fechar_conexao
from src.utils.menu import menu_principal, menu_insercao
from src.utils.insercao import (
    inserir_proprietario,
    inserir_organizacao,
    inserir_cadastro_tecnico,
    inserir_produtor,
    inserir_produto,
    inserir_plantacao,
    inserir_safra,
    inserir_sensor,
    inserir_dado_coletado,
    inserir_insumo,
    inserir_safra_insumo
)

def menu_insercao_loop():
    while True:
        opcao = menu_insercao()
        # Ordem conforme dependências do banco de dados:
        if opcao == "1":
            inserir_proprietario()
        elif opcao == "2":
            inserir_organizacao()
        elif opcao == "3":
            inserir_cadastro_tecnico()
        elif opcao == "4":
            inserir_produtor()
        elif opcao == "5":
            inserir_produto()
        elif opcao == "6":
            inserir_plantacao()
        elif opcao == "7":
            inserir_safra()
        elif opcao == "8":
            inserir_sensor()
        elif opcao == "9":
            inserir_dado_coletado()
        elif opcao == "10":
            inserir_insumo()
        elif opcao == "11":
            inserir_safra_insumo()
        elif opcao == "0":
            break
        else:
            print("Opção inválida.")

def main():
    while True:
        opcao = menu_principal()
        if opcao == "1":
            menu_insercao_loop()
        elif opcao == "2":
            # Gerar relatórios em JSON
            pass
        elif opcao == "0":
            print("Saindo do sistema.")
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()
