from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes
from decouple import config
import requests

# Configuración del Bot
application = ApplicationBuilder().token(config('TOKEN_TELEGRAM_BOT')).build()

# Endpoints de la API REST
API_BASE_URL = "http://127.0.0.1:5000/api/v1"
HISTORICO_ENDPOINT = f"{API_BASE_URL}/historico-notificaciones"
ESTADO_ACTUAL_ENDPOINT = f"{API_BASE_URL}/estado-actual"

# Comando /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Crear botones
    keyboard = [
        [InlineKeyboardButton("Histórico notificaciones", callback_data="historico")],
        [InlineKeyboardButton("Estado actual del servidor", callback_data="estado_actual")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    # Enviar mensaje con botones
    await update.message.reply_text("Hola, ¿cómo estás?\nElige una opción:", reply_markup=reply_markup)

# Comando /cancel
async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hasta pronto. Si tienes otra solicitud, estoy al tanto. 😊")

# Manejar clics en los botones
async def button_click(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "historico":
        # Obtener histórico de notificaciones
        response = requests.get(HISTORICO_ENDPOINT)
        if response.status_code == 200:
            notificaciones = response.json()
            mensaje = formatear_historico(notificaciones)
            await query.edit_message_text(mensaje)
        else:
            await query.edit_message_text("Error al obtener el histórico de notificaciones.")

    elif query.data == "estado_actual":
        # Obtener estado actual del servidor
        response = requests.get(ESTADO_ACTUAL_ENDPOINT)
        if response.status_code == 200:
            estado = response.json()
            mensaje = formatear_estado_actual(estado)
            await query.edit_message_text(mensaje)
        else:
            await query.edit_message_text("Error al obtener el estado actual del servidor.")

# Formatear histórico de notificaciones
def formatear_historico(notificaciones):
    mensaje = f"Histórico de métricas:\n"
    mensaje += "----------------------------------------\n"
    for notificacion in notificaciones:
        mensaje += f"🖥 ServerHostName@IP: {notificacion['host_name']}@{notificacion['ip']}\n"
        mensaje += f"📅 Fecha: {notificacion['fecha_creacion']}\n"
        mensaje += f"🔢 RAM: {notificacion['ram_uso']}%, CPU: {notificacion['cpu_uso']}%, Disco: {notificacion['disco_uso']}%\n"
        mensaje += "----------------------------------------\n"
    return mensaje

# Formatear estado actual del servidor
def formatear_estado_actual(estado):
    # Verificar si se superó algún umbral
    supero_umbral = {
        "uso_cpu": estado['cpu'] > 75,
        "uso_ram": estado['ram'] > 75,
        "uso_disco_duro": estado['disco'] > 75
    }
    estado_supero_umbral = any(supero_umbral.values())

    # Construir el mensaje
    if estado_supero_umbral:
        # Mensaje de alerta
        mensaje = f"🚨 Alerta: el servidor {estado['hostname']} ({estado['ip']}) presenta un consumo de recursos mayor al 75%\n"
        mensaje += "----------------------------------------\n"
        mensaje += f"🔴 CPU: {estado['cpu']} %\n" if supero_umbral["uso_cpu"] else f"✅ CPU: {estado['cpu']} %\n"
        mensaje += f"🔴 RAM: {estado['ram']} %\n" if supero_umbral["uso_ram"] else f"✅ RAM: {estado['ram']} %\n"
        mensaje += f"🔴 Disco Duro: {estado['disco']} %\n" if supero_umbral["uso_disco_duro"] else f"✅ Disco Duro: {estado['disco']} %\n"
        mensaje += "----------------------------------------\n"
    else:
        # Mensaje de estado normal
        mensaje = f"Estado actual del servidor: {estado['hostname']} ({estado['ip']})\n"
        mensaje += "----------------------------------------\n"
        mensaje += f"🔢 RAM: {estado['ram']}%\n"
        mensaje += f"🔢 CPU: {estado['cpu']}%\n"
        mensaje += f"🔢 Disco: {estado['disco']}%\n"
        mensaje += "----------------------------------------\n"

    return mensaje

# Registrar manejadores de comandos y botones
application.add_handler(CommandHandler("start", start))
application.add_handler(CommandHandler("cancel", cancel))
application.add_handler(CallbackQueryHandler(button_click))

# Iniciar el Bot
application.run_polling(allowed_updates=Update.ALL_TYPES)