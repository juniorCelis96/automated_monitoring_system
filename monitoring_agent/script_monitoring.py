import psutil
import socket
from controller.metric_controller import save_metric
from controller.notification_controller import save_notification
from controller.msg_group_telegram_controller import ChatBotTelegram


def enviar_mensaje_telegram(mensaje):
    print(mensaje)

try:
    # Capturar métricas
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    ram_uso = psutil.virtual_memory().percent
    cpu_uso = psutil.cpu_percent(interval=1)
    disco_uso = psutil.disk_usage('/').percent

    # Guardar métricas en la base de datos
    metric_is_save = save_metric(ip_server=ip_address, ram_uso=ram_uso, cpu_uso=cpu_uso, disco_uso=disco_uso)

    # Verificar umbrales
    supero_umbral = {
        "uso_cpu": cpu_uso > 75,
        "uso_ram": ram_uso > 75,
        "uso_disco_duro": disco_uso > 75
    }
    estado_supero_umbral = any(supero_umbral.values())

    # Guardar notificación si se superó el umbral
    if estado_supero_umbral:
        id_server = metric_is_save
        result = save_notification(id_server, supero_umbral, estado_supero_umbral)

        if result:
            # Enviar alerta a Telegram
            mensaje = f"🚨 Alerta: el servidor host: {hostname}@ip:{ip_address}, presenta un consumo de recursos mayor al 75%\n"
            mensaje += f"🔴 CPU: {cpu_uso} %\n" if supero_umbral["uso_cpu"] else f"✅ CPU: {cpu_uso} %\n"
            mensaje += f"🔴 RAM: {ram_uso} %\n" if supero_umbral["uso_ram"] else f"✅ RAM: {ram_uso} %\n"
            mensaje += f"🔴 Disco Duro: {disco_uso} %\n" if supero_umbral["uso_disco_duro"] else f"✅ Disco Duro: {disco_uso} %\n"
            ChatBotTelegram.send_msg_group_telegram(mensaje)  # Función para enviar mensaje a Telegram
        else: 
            print("Hubo un error al intentar notificar")
except Exception as e:
    raise("Error al intentar monitorear el servidor: ", e)