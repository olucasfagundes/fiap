from src.utils.insercao import (
    inserir_organizacao, inserir_proprietario, inserir_produtor, inserir_cadastro_tecnico,
    inserir_produto, inserir_plantacao, inserir_safra, inserir_sensor, inserir_dado_coletado,
    inserir_insumo, inserir_safra_insumo
)
from src.utils.relatorios import (
    relatorio_producao_por_safra_json,
    relatorio_insumos_por_safra_json,
    relatorio_umidade_media_por_plantacao_json
)
import os

def menu_principal():
    while True:
        print("\n=== Sistema de Monitoramento Agrícola ===")
        print("1. Inserir dados no sistema")
        print("2. Gerar relatórios em JSON")
        print("0. Sair")
        opcao = input("Escolha uma opção: ")
        if opcao == "1":
            menu_insercao()
        elif opcao == "2":
            menu_relatorios()
        elif opcao == "0":
            print("Saindo...")
            break
        else:
            print("Opção inválida.")

def menu_insercao():
    while True:
        print("\n=== Inserção de Dados ===")
        print("1. ORGANIZACAO")
        print("2. PROPRIETARIO")
        print("3. PRODUTOR")
        print("4. CADASTRO_TECNICO")
        print("5. PRODUTO")
        print("6. PLANTACAO")
        print("7. SAFRA")
        print("8. SENSOR")
        print("9. DADO_COLETADO")
        print("10. INSUMO")
        print("11. SAFRA_INSUMO")
        print("0. Voltar")
        opcao = input("Escolha a entidade para inserir dados: ")
        if opcao == "1":
            inserir_organizacao()
        elif opcao == "2":
            inserir_proprietario()
        elif opcao == "3":
            inserir_produtor()
        elif opcao == "4":
            inserir_cadastro_tecnico()
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

def menu_relatorios():
    pasta = "relatorios"
    if not os.path.exists(pasta):
        os.makedirs(pasta)
    while True:
        print("\n=== Relatórios em JSON ===")
        print("1. Produção por safra")
        print("2. Insumos por safra")
        print("3. Umidade média por plantação")
        print("0. Voltar")
        opcao = input("Escolha o relatório: ")
        if opcao == "1":
            relatorio_producao_por_safra_json(filepath=os.path.join(pasta, "relatorio_producao_por_safra.json"))
        elif opcao == "2":
            relatorio_insumos_por_safra_json(filepath=os.path.join(pasta, "relatorio_insumos_por_safra.json"))
        elif opcao == "3":
            relatorio_umidade_media_por_plantacao_json(filepath=os.path.join(pasta, "relatorio_umidade_media_por_plantacao.json"))
        elif opcao == "0":
            break
        else:
            print("Opção inválida.")
