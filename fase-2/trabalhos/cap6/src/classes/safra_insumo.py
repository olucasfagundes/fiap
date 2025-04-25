class SafraInsumo:
    def __init__(self, id_safra, id_insumo, quantidade):
        self.id_safra = id_safra
        self.id_insumo = id_insumo
        self.quantidade = quantidade

    def to_dict(self):
        return {
            "id_safra": self.id_safra,
            "id_insumo": self.id_insumo,
            "quantidade": self.quantidade
        }
