class CadastroTecnico:
    def __init__(self, id_tecnico, nome_completo, registro_crea, telefone, email, especialidade):
        self.id_tecnico = id_tecnico
        self.nome_completo = nome_completo
        self.registro_crea = registro_crea
        self.telefone = telefone
        self.email = email
        self.especialidade = especialidade

    def to_dict(self):
        return {
            "id_tecnico": self.id_tecnico,
            "nome_completo": self.nome_completo,
            "registro_crea": self.registro_crea,
            "telefone": self.telefone,
            "email": self.email,
            "especialidade": self.especialidade
        }
