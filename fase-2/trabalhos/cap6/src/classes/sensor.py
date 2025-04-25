class Sensor:
    def __init__(self, id_sensor, id_safra, tipo_sensor, status_operacional, fabricante, localizacao_gps):
        self.id_sensor = id_sensor
        self.id_safra = id_safra
        self.tipo_sensor = tipo_sensor
        self.status_operacional = status_operacional
        self.fabricante = fabricante
        self.localizacao_gps = localizacao_gps

    def to_dict(self):
        return {
            "id_sensor": self.id_sensor,
            "id_safra": self.id_safra,
            "tipo_sensor": self.tipo_sensor,
            "status_operacional": self.status_operacional,
            "fabricante": self.fabricante,
            "localizacao_gps": self.localizacao_gps
        }
