from src.infra.db import conectar, fechar_conexao
from src.classes.organizacao import Organizacao
from src.classes.proprietario import Proprietario
from src.classes.produtor import Produtor
from src.classes.cadastro_tecnico import CadastroTecnico
from src.classes.produto import Produto
from src.classes.plantacao import Plantacao
from src.classes.safra import Safra
from src.classes.sensor import Sensor
from src.classes.dado_coletado import DadoColetado
from src.classes.insumo import Insumo
from src.classes.safra_insumo import SafraInsumo

def input_str(msg, required=True):
    while True:
        val = input(msg)
        if not val and required:
            print("Campo obrigatório. Digite um valor.")
        else:
            return val

def input_int(msg, required=True):
    while True:
        val = input(msg)
        if not val and not required:
            return None
        try:
            return int(val)
        except ValueError:
            print("Valor inválido. Digite um número inteiro.")

def input_float(msg, required=True):
    while True:
        val = input(msg)
        if not val and not required:
            return None
        try:
            return float(val)
        except ValueError:
            print("Valor inválido. Digite um número decimal.")

def inserir_organizacao():
    print("\nInserir ORGANIZACAO")
    id_organizacao = input_str("ID (string): ")
    nome = input_str("Nome: ")
    cnpj = input_str("CNPJ: ")
    id_proprietario = input_str("ID Proprietario (string): ")
    org = Organizacao(id_organizacao, nome, cnpj, id_proprietario)
    print("Organizacao criada:", org.to_dict())
    conn = conectar()
    try:
        with conn.cursor() as cur:
            cur.execute(
                "INSERT INTO organizacao (id_organizacao, nome, cnpj, id_proprietario) VALUES (%s, %s, %s, %s)",
                (id_organizacao, nome, cnpj, id_proprietario)
            )
            conn.commit()
            print("Organizacao inserida no banco de dados.")
    finally:
        fechar_conexao(conn)

def inserir_proprietario():
    print("\nInserir PROPRIETARIO")
    id_proprietario = input_str("ID (string): ")
    nome = input_str("Nome: ")
    cpf = input_str("CPF: ")
    telefone = input_str("Telefone: ", required=False)
    email = input_str("Email: ", required=False)
    prop = Proprietario(id_proprietario, nome, cpf, telefone, email)
    print("Proprietario criado:", prop.to_dict())
    conn = conectar()
    try:
        with conn.cursor() as cur:
            cur.execute(
                "INSERT INTO proprietario (id_proprietario, nome, cpf, telefone, email) VALUES (%s, %s, %s, %s, %s)",
                (id_proprietario, nome, cpf, telefone, email)
            )
            conn.commit()
            print("Proprietario inserido no banco de dados.")
    finally:
        fechar_conexao(conn)

def inserir_produtor():
    print("\nInserir PRODUTOR")
    id_produtor = input_str("ID (string): ")
    id_organizacao = input_str("ID Organizacao (string): ")
    nome = input_str("Nome: ")
    cnpj = input_str("CNPJ: ")
    id_tecnico = input_str("ID Tecnico (string): ")
    prod = Produtor(id_produtor, id_organizacao, nome, cnpj, id_tecnico)
    print("Produtor criado:", prod.to_dict())
    conn = conectar()
    try:
        with conn.cursor() as cur:
            cur.execute(
                "INSERT INTO produtor (id_produtor, id_organizacao, nome, cnpj, id_tecnico) VALUES (%s, %s, %s, %s, %s)",
                (id_produtor, id_organizacao, nome, cnpj, id_tecnico)
            )
            conn.commit()
            print("Produtor inserido no banco de dados.")
    finally:
        fechar_conexao(conn)

def inserir_cadastro_tecnico():
    print("\nInserir CADASTRO_TECNICO")
    id_tecnico = input_str("ID (string): ")
    nome_completo = input_str("Nome completo: ")
    registro_crea = input_str("Registro CREA: ", required=False)
    telefone = input_str("Telefone: ", required=False)
    email = input_str("Email: ", required=False)
    especialidade = input_str("Especialidade: ", required=False)
    tecnico = CadastroTecnico(id_tecnico, nome_completo, registro_crea, telefone, email, especialidade)
    print("Cadastro Tecnico criado:", tecnico.to_dict())
    conn = conectar()
    try:
        with conn.cursor() as cur:
            cur.execute(
                "INSERT INTO cadastro_tecnico (id_tecnico, nome_completo, registro_crea, telefone, email, especialidade) VALUES (%s, %s, %s, %s, %s, %s)",
                (id_tecnico, nome_completo, registro_crea, telefone, email, especialidade)
            )
            conn.commit()
            print("Cadastro Tecnico inserido no banco de dados.")
    finally:
        fechar_conexao(conn)

def inserir_produto():
    print("\nInserir PRODUTO")
    id_produto = input_str("ID (string): ")
    id_produtor = input_str("ID Produtor (string): ")
    nome = input_str("Nome: ")
    tipo = input_str("Tipo: ", required=False)
    prod = Produto(id_produto, id_produtor, nome, tipo)
    print("Produto criado:", prod.to_dict())
    conn = conectar()
    try:
        with conn.cursor() as cur:
            cur.execute(
                "INSERT INTO produto (id_produto, id_produtor, nome, tipo) VALUES (%s, %s, %s, %s)",
                (id_produto, id_produtor, nome, tipo)
            )
            conn.commit()
            print("Produto inserido no banco de dados.")
    finally:
        fechar_conexao(conn)

def inserir_plantacao():
    print("\nInserir PLANTACAO")
    id_plantacao = input_str("ID (string): ")
    id_produto = input_str("ID Produto (string): ")
    area_total_ha = input_float("Área total (ha): ", required=False)
    localizacao_gps = input_str("Localização GPS: ", required=False)
    plant = Plantacao(id_plantacao, id_produto, area_total_ha, localizacao_gps)
    print("Plantacao criada:", plant.to_dict())
    conn = conectar()
    try:
        with conn.cursor() as cur:
            cur.execute(
                "INSERT INTO plantacao (id_plantacao, id_produto, area_total_ha, localizacao_gps) VALUES (%s, %s, %s, %s)",
                (id_plantacao, id_produto, area_total_ha, localizacao_gps)
            )
            conn.commit()
            print("Plantacao inserida no banco de dados.")
    finally:
        fechar_conexao(conn)

def inserir_safra():
    print("\nInserir SAFRA")
    id_safra = input_str("ID (string): ")
    id_plantacao = input_str("ID Plantacao (string): ")
    ano = input_int("Ano (int): ", required=False)
    previsao_producao_kg = input_float("Previsão produção (kg): ", required=False)
    producao_real_kg = input_float("Produção real (kg): ", required=False)
    safra = Safra(id_safra, id_plantacao, ano, previsao_producao_kg, producao_real_kg)
    print("Safra criada:", safra.to_dict())
    conn = conectar()
    try:
        with conn.cursor() as cur:
            cur.execute(
                "INSERT INTO safra (id_safra, id_plantacao, ano, previsao_producao_kg, producao_real_kg) VALUES (%s, %s, %s, %s, %s)",
                (id_safra, id_plantacao, ano, previsao_producao_kg, producao_real_kg)
            )
            conn.commit()
            print("Safra inserida no banco de dados.")
    finally:
        fechar_conexao(conn)

def inserir_sensor():
    print("\nInserir SENSOR")
    id_sensor = input_str("ID (string): ")
    id_safra = input_str("ID Safra (string): ")
    tipo_sensor = input_str("Tipo sensor: ", required=False)
    status_operacional = input_str("Status operacional: ", required=False)
    fabricante = input_str("Fabricante: ", required=False)
    localizacao_gps = input_str("Localização GPS: ", required=False)
    sensor = Sensor(id_sensor, id_safra, tipo_sensor, status_operacional, fabricante, localizacao_gps)
    print("Sensor criado:", sensor.to_dict())
    conn = conectar()
    try:
        with conn.cursor() as cur:
            cur.execute(
                "INSERT INTO sensor (id_sensor, id_safra, tipo_sensor, status_operacional, fabricante, localizacao_gps) VALUES (%s, %s, %s, %s, %s, %s)",
                (id_sensor, id_safra, tipo_sensor, status_operacional, fabricante, localizacao_gps)
            )
            conn.commit()
            print("Sensor inserido no banco de dados.")
    finally:
        fechar_conexao(conn)

def inserir_dado_coletado():
    print("\nInserir DADO_COLETADO")
    id_dado = input_str("ID (string): ")
    id_sensor = input_str("ID Sensor (string): ")
    timestamp = input_str("Timestamp (YYYY-MM-DD HH:MM:SS): ", required=False)
    valor = input_float("Valor: ", required=False)
    unidade_medida = input_str("Unidade de medida: ", required=False)
    observacao = input_str("Observação: ", required=False)
    dado = DadoColetado(id_dado, id_sensor, timestamp, valor, unidade_medida, observacao)
    print("Dado coletado criado:", dado.to_dict())
    conn = conectar()
    try:
        with conn.cursor() as cur:
            cur.execute(
                "INSERT INTO dado_coletado (id_dado, id_sensor, timestamp, valor, unidade_medida, observacao) VALUES (%s, %s, %s, %s, %s, %s)",
                (id_dado, id_sensor, timestamp, valor, unidade_medida, observacao)
            )
            conn.commit()
            print("Dado coletado inserido no banco de dados.")
    finally:
        fechar_conexao(conn)

def inserir_insumo():
    print("\nInserir INSUMO")
    id_insumo = input_str("ID (string): ")
    nome = input_str("Nome: ")
    tipo = input_str("Tipo: ", required=False)
    fornecedor = input_str("Fornecedor: ", required=False)
    unidade_medida = input_str("Unidade de medida: ", required=False)
    insumo = Insumo(id_insumo, nome, tipo, fornecedor, unidade_medida)
    print("Insumo criado:", insumo.to_dict())
    conn = conectar()
    try:
        with conn.cursor() as cur:
            cur.execute(
                "INSERT INTO insumo (id_insumo, nome, tipo, fornecedor, unidade_medida) VALUES (%s, %s, %s, %s, %s)",
                (id_insumo, nome, tipo, fornecedor, unidade_medida)
            )
            conn.commit()
            print("Insumo inserido no banco de dados.")
    finally:
        fechar_conexao(conn)

def inserir_safra_insumo():
    print("\nInserir SAFRA_INSUMO")
    id_safra = input_str("ID Safra (string): ")
    id_insumo = input_str("ID Insumo (string): ")
    quantidade = input_float("Quantidade: ", required=False)
    si = SafraInsumo(id_safra, id_insumo, quantidade)
    print("SafraInsumo criado:", si.to_dict())
    conn = conectar()
    try:
        with conn.cursor() as cur:
            cur.execute(
                "INSERT INTO safra_insumo (id_safra, id_insumo, quantidade) VALUES (%s, %s, %s)",
                (id_safra, id_insumo, quantidade)
            )
            conn.commit()
            print("SafraInsumo inserido no banco de dados.")
    finally:
        fechar_conexao(conn)
