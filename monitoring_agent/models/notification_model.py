import json
from database.db_config import get_connection


class NotificationModel():
    @classmethod
    def add_notification(cls, notification):
        try:
            conn = get_connection()
            with conn.cursor() as cursor:
                cursor.execute("""
                    INSERT INTO notificaciones (servidor_id, supero_umbral, estado_supero_umbral, fecha_creacion)
                    VALUES (%s, %s, %s, %s)""",
                    (notification.servidor_id, json.dumps(notification.supero_umbral), 
                        notification.estado_supero_umbral, notification.fecha_creacion))  # Guardar fecha actual

                affected_rows = cursor.rowcount
                conn.commit()
            
            conn.close()
            return affected_rows
        except Exception as e:
            raise Exception("Error al insertar la notificación: ", e)
