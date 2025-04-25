import json
from src.infra.db import conectar, fechar_conexao

def salvar_json(dados, caminho):
    with open(caminho, "w", encoding="utf-8") as f:
        json.dump(dados, f, ensure_ascii=False, indent=4)

def relatorio_producao_por_safra_json(filepath="relatorios/relatorio_producao_por_safra.json"):
    """
    Gera um relatório com a produção prevista e real por safra.
    """
    conn = conectar()
    try:
        with conn.cursor() as cur:
            cur.execute("""
                SELECT s.id_safra, s.ano, p.nome as produto, s.previsao_producao_kg, s.producao_real_kg
                FROM safra s
                JOIN plantacao pl ON s.id_plantacao = pl.id_plantacao
                JOIN produto p ON pl.id_produto = p.id_produto
                ORDER BY s.ano DESC
            """)
            rows = cur.fetchall()
            colnames = [desc[0] for desc in cur.description]
            dados = [dict(zip(colnames, row)) for row in rows]
            salvar_json(dados, filepath)
            print(f"Relatório salvo em {filepath}")
    finally:
        fechar_conexao(conn)

def relatorio_insumos_por_safra_json(filepath="relatorios/relatorio_insumos_por_safra.json"):
    """
    Gera um relatório com o total de insumos aplicados por safra.
    """
    conn = conectar()
    try:
        with conn.cursor() as cur:
            cur.execute("""
                SELECT s.id_safra, s.ano, p.nome as produto, i.nome as insumo, si.quantidade, i.unidade_medida
                FROM safra s
                JOIN safra_insumo si ON s.id_safra = si.id_safra
                JOIN insumo i ON si.id_insumo = i.id_insumo
                JOIN plantacao pl ON s.id_plantacao = pl.id_plantacao
                JOIN produto p ON pl.id_produto = p.id_produto
                ORDER BY s.ano DESC, i.nome
            """)
            rows = cur.fetchall()
            colnames = [desc[0] for desc in cur.description]
            dados = [dict(zip(colnames, row)) for row in rows]
            salvar_json(dados, filepath)
            print(f"Relatório salvo em {filepath}")
    finally:
        fechar_conexao(conn)

def relatorio_umidade_media_por_plantacao_json(filepath="relatorios/relatorio_umidade_media_por_plantacao.json"):
    """
    Gera um relatório com a média dos valores de sensores de umidade por plantação.
    """
    conn = conectar()
    try:
        with conn.cursor() as cur:
            cur.execute("""
                SELECT pl.id_plantacao, p.nome as produto, AVG(dc.valor) as media_umidade
                FROM plantacao pl
                JOIN safra s ON pl.id_plantacao = s.id_plantacao
                JOIN sensor se ON s.id_safra = se.id_safra
                JOIN dado_coletado dc ON se.id_sensor = dc.id_sensor
                WHERE se.tipo_sensor ILIKE '%umidade%'
                GROUP BY pl.id_plantacao, p.nome
                ORDER BY media_umidade DESC
            """)
            rows = cur.fetchall()
            colnames = [desc[0] for desc in cur.description]
            dados = [dict(zip(colnames, row)) for row in rows]
            salvar_json(dados, filepath)
            print(f"Relatório salvo em {filepath}")
    finally:
        fechar_conexao(conn)
