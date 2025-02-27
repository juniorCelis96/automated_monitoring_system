from src.database.db import get_connection

class HistoricModel():
    @classmethod
    def get_historics(cls):
        try:
            conn = get_connection()
            historics_list = []

            with conn.cursor() as cursor:
                # Consulta con JOIN para obtener host_name, ip y fecha_creacion
                cursor.execute("""
                    SELECT 
                        s.host_name, 
                        s.ip, 
                        m.ram_uso, 
                        m.cpu_uso, 
                        m.disco_uso,
                        m.fecha_creacion  -- Nuevo campo
                    FROM 
                        public.metricas m
                    JOIN 
                        public.servidores s ON m.servidor_id = s.id;
                """)
                result = cursor.fetchall()

                for row in result:
                    # Formatear la fecha en DD-MM-YYYY HH:MM:ss
                    fecha_creacion = row[5]  # Suponiendo que es un objeto datetime
                    fecha_formateada = fecha_creacion.strftime("%d-%m-%Y %H:%M:%S")

                    # Crear un diccionario con los datos
                    historic_data = {
                        "host_name": row[0],      # host_name
                        "ip": row[1],             # ip
                        "ram_uso": row[2],        # ram_uso
                        "cpu_uso": row[3],        # cpu_uso
                        "disco_uso": row[4],      # disco_uso
                        "fecha_creacion": fecha_formateada  # fecha_creacion formateada
                    }
                    historics_list.append(historic_data)

            conn.close()
            return historics_list
        except Exception as e:
            raise Exception("Error al obtener las métricas: ", e)

