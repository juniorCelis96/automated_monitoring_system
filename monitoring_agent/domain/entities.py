class Metric():
    def __init__(self, servidor_id, ram_uso, cpu_uso, disco_uso, fecha_creacion)-> None:
        self.servidor_id = servidor_id
        self.ram_uso = ram_uso
        self.cpu_uso = cpu_uso
        self.disco_uso = disco_uso
        self.fecha_creacion = fecha_creacion

class Notification():
    def __init__(self, servidor_id, supero_umbral, estado_supero_umbral, fecha_creacion)-> None:
        self.servidor_id = servidor_id
        self.supero_umbral = supero_umbral
        self.estado_supero_umbral = estado_supero_umbral
        self.fecha_creacion = fecha_creacion
