class Insumo:
    def __init__(self, id_insumo, nome, tipo, fornecedor, unidade_medida):
        self.id_insumo = id_insumo
        self.nome = nome
        self.tipo = tipo
        self.fornecedor = fornecedor
        self.unidade_medida = unidade_medida

    def to_dict(self):
        return {
            "id_insumo": self.id_insumo,
            "nome": self.nome,
            "tipo": self.tipo,
            "fornecedor": self.fornecedor,
            "unidade_medida": self.unidade_medida
        }
