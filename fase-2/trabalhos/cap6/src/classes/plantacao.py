class Plantacao:
    def __init__(self, id_plantacao, id_produto, area_total_ha, localizacao_gps):
        self.id_plantacao = id_plantacao
        self.id_produto = id_produto
        self.area_total_ha = area_total_ha
        self.localizacao_gps = localizacao_gps

    def to_dict(self):
        return {
            "id_plantacao": self.id_plantacao,
            "id_produto": self.id_produto,
            "area_total_ha": self.area_total_ha,
            "localizacao_gps": self.localizacao_gps
        }
