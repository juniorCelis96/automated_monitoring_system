class Historic():
    def __init__(self, servidor_info, ram_uso, cpu_uso, disco_uso, fecha_creacion)-> None:
        self.servidor_info = servidor_info
        self.ram_uso = ram_uso
        self.cpu_uso = cpu_uso
        self.disco_uso = disco_uso
        self.fecha_creacion = fecha_creacion

    def to_JSON(self):
        return {
            'servidor_info': self.servidor_info,
            'ram': self.ram_uso,
            'cpu': self.cpu_uso,
            'disco': self.disco_uso,
            'fecha': self.fecha_creacion
        }