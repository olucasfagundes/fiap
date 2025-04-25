class Produtor:
    def __init__(self, id_produtor, id_organizacao, nome, cnpj, id_tecnico):
        self.id_produtor = id_produtor
        self.id_organizacao = id_organizacao
        self.nome = nome
        self.cnpj = cnpj
        self.id_tecnico = id_tecnico

    def to_dict(self):
        return {
            "id_produtor": self.id_produtor,
            "id_organizacao": self.id_organizacao,
            "nome": self.nome,
            "cnpj": self.cnpj,
            "id_tecnico": self.id_tecnico
        }
