import requests, logging
from decouple import config

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

class ChatBotTelegram():
    @classmethod
    def send_msg_group_telegram(cls, mensaje):
        TOKEN = config('TOKEN_TELEGRAM_BOT')
        CHAT_ID = config('ID_TELEGRAM_GROUP')
        MENSAJE = mensaje

        url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

        # Parámetros del mensaje
        params = {
            "chat_id": CHAT_ID,
            "text": MENSAJE
        }

        # Enviar el mensaje
        response = requests.get(url, params=params)

        # Verificar la respuesta
        if response.status_code == 200:
            logging.info("Mensaje enviado con éxito!")
            # print("Mensaje enviado con éxito!")
        else:
            print("Error al enviar el mensaje:", response.json())