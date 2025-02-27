import logging

from datetime import datetime
from domain.entities import Metric
from models.metrics_model import MetricModel

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def save_metric(ip_server, ram_uso, cpu_uso, disco_uso):
    try:
        id_servidor = MetricModel.get_id_server(ip_server)
        fecha_creacion =  datetime.now()
        metric = Metric(id_servidor, ram_uso, cpu_uso, disco_uso,fecha_creacion)
        result = MetricModel.add_metric(metric=metric)
        if result == 1:
            logging.info("Metrica insertada exitosamente")
            # print("Metrica insertada exitosamente")
        else:
            print("No se logró insertar la métrica") 
        return id_servidor
    except Exception as e:
        raise("Error al guardar la métrica: ", e)