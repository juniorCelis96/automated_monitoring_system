import logging
from datetime import datetime
from domain.entities import Notification
from models.notification_model import NotificationModel


logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def save_notification(id_servidor, supero_umbral, estado):
    try:
        fecha_creacion =  datetime.now()
        notificacion = Notification(id_servidor, supero_umbral, estado, fecha_creacion)
        result = NotificationModel.add_notification(notification=notificacion)
        if result == 1:
            logging.info("Notificacion insertada exitosamente")
            # print("Notificacion insertada exitosamente")
            return True
        else:
            logging.info("No se logró insertar la notificación") 
            # print("No se logró insertar la notificación") 
            return False
    except Exception as e:
        raise("Error al guardar la notificacion: ", e)