from database.db_config import get_connection


class MetricModel():
    @classmethod
    def add_metric(cls, metric):
        try:
            conn = get_connection()

            with conn.cursor() as cursor:
                cursor.execute("""
                    INSERT INTO public.metricas(servidor_id, ram_uso, cpu_uso, disco_uso, fecha_creacion)
                    VALUES (%s, %s, %s, %s, %s)""",(metric.servidor_id, metric.ram_uso, metric.cpu_uso, metric.disco_uso, metric.fecha_creacion))
                affected_rows = cursor.rowcount
                conn.commit()
            conn.close()
            return affected_rows
        except Exception as e:
            raise Exception("Error al insertar la metrica: ", e)

    @classmethod
    def get_id_server(cls, ip):
        try:
            conn = get_connection()
            with conn.cursor() as cursor:
                cursor.execute("""
                    SELECT id FROM public.servidores WHERE ip = %s
                """, (ip,))
                result = cursor.fetchone()
            conn.close()
            return result[0] if result else None
        except Exception as e:
            raise Exception("Error al obtener el ID del servidor: ", e)
    
