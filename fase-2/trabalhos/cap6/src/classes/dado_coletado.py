class DadoColetado:
    def __init__(self, id_dado, id_sensor, timestamp, valor, unidade_medida, observacao):
        self.id_dado = id_dado
        self.id_sensor = id_sensor
        self.timestamp = timestamp
        self.valor = valor
        self.unidade_medida = unidade_medida
        self.observacao = observacao

    def to_dict(self):
        return {
            "id_dado": self.id_dado,
            "id_sensor": self.id_sensor,
            "timestamp": self.timestamp,
            "valor": self.valor,
            "unidade_medida": self.unidade_medida,
            "observacao": self.observacao
        }
