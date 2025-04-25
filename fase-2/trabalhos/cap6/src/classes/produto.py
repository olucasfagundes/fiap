class Produto:
    def __init__(self, id_produto, id_produtor, nome, tipo):
        self.id_produto = id_produto
        self.id_produtor = id_produtor
        self.nome = nome
        self.tipo = tipo

    def to_dict(self):
        return {
            "id_produto": self.id_produto,
            "id_produtor": self.id_produtor,
            "nome": self.nome,
            "tipo": self.tipo
        }
