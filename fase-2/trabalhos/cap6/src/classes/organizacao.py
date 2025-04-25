class Organizacao:
    def __init__(self, id_organizacao, nome, cnpj, id_proprietario):
        self.id_organizacao = id_organizacao
        self.nome = nome
        self.cnpj = cnpj
        self.id_proprietario = id_proprietario

    def to_dict(self):
        return {
            "id_organizacao": self.id_organizacao,
            "nome": self.nome,
            "cnpj": self.cnpj,
            "id_proprietario": self.id_proprietario
        }
