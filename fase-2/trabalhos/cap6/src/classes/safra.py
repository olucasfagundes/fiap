class Safra:
    def __init__(self, id_safra, id_plantacao, ano, previsao_producao_kg, producao_real_kg):
        self.id_safra = id_safra
        self.id_plantacao = id_plantacao
        self.ano = ano
        self.previsao_producao_kg = previsao_producao_kg
        self.producao_real_kg = producao_real_kg

    def to_dict(self):
        return {
            "id_safra": self.id_safra,
            "id_plantacao": self.id_plantacao,
            "ano": self.ano,
            "previsao_producao_kg": self.previsao_producao_kg,
            "producao_real_kg": self.producao_real_kg
        }
