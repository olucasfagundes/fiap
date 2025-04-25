class Proprietario:
    def __init__(self, id_proprietario, nome, cpf, telefone, email):
        self.id_proprietario = id_proprietario
        self.nome = nome
        self.cpf = cpf
        self.telefone = telefone
        self.email = email

    def to_dict(self):
        return {
            "id_proprietario": self.id_proprietario,
            "nome": self.nome,
            "cpf": self.cpf,
            "telefone": self.telefone,
            "email": self.email
        }
