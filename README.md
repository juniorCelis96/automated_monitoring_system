# **Sistema de Monitoreo de Servidores**

Este proyecto implementa un sistema de monitoreo para servidores Linux que notifica alertas por Telegram cuando el uso de recursos (RAM, CPU, disco) supera el 75%. Además, permite consultar el estado actual y el histórico de notificaciones a través de un Bot de Telegram.

---

## **Tabla de Contenidos**
1. Descripción del Proyecto
2. Funcionalidades
3. Arquitectura
4. Tecnologías Utilizadas
5. Instalación y Configuración
6. Uso
7. Despliegue
8. Contribución
9. Licencia

---

## **Descripción del Proyecto**
El sistema consta de:
- **Agentes de Monitoreo**: Scripts en Python que capturan métricas de RAM, CPU y disco en servidores Linux.
- **Servicio Centralizado**: API REST que recibe métricas, las almacena en una base de datos y gestiona notificaciones.
- **Bot de Telegram**: Permite consultar el estado actual de los servidores, el histórico de notificaciones y ejecutar acciones correctivas.

---

## **Funcionalidades**
- **Monitoreo en tiempo real**: Captura métricas cada 5 minutos, por medio de un script automatizado con una operación CRON.
- **Alertas por Telegram**: Notifica cuando el uso de recursos supera el 75%.
- **Consultas Por medio del bot**:
  - Estado actual de los servidores. - Comando: 1. /start 2. Button: Estado Actual Del Servidor
  - Histórico de notificaciones. - Comando: 1. /start 2. Button: Histórico Notificaciones
  - /cancel para terminar la sesión del chat
- **Acciones correctivas**: Ejecutar comandos remotos para resolver problemas(Oportunidad de mejor).

---

## **Arquitectura**
El sistema está compuesto por los siguientes componentes:
1. **Agentes de Monitoreo**: Instalados en cada servidor Linux.
2. **Servicio Centralizado**: API REST que recibe y procesa métricas.
3. **Base de Datos**: Almacena métricas y notificaciones.
4. **Bot de Telegram**: Interfaz para consultas y acciones.

Diagrama de Arquitectura(imagenes/diagram_automated_monitoring_system.png)

---

## **Tecnologías Utilizadas**
- **Lenguaje de programación**: Python.
- **Librerías**:
  - `psutil`: Captura de métricas del sistema.
  - `python-telegram-bot`: Interacción con la API de Telegram.
  - `Flask`: Desarrollo del Servicio Centralizado.
  - `requests`: Solicitudes HTTP.
- **Base de datos**: PostgreSQL.
- **Despliegue**: Servidores Linux(en AWS opcional).

---

## **Instalación y Configuración**
### **Requisitos**
- Python 3.8 o superior.
- Acceso a servidores Linux.
- Token de un Bot de Telegram.

### **Pasos**
1. Clona el repositorio:
   ```bash
   git clone https://github.com/juniorCelis96/automated_monitoring_system.git
   ```
2. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```
3. Configura las variables de entorno:
   - Crea un archivo `.env` y define las siguientes variables:
     ```
     TOKEN_TELEGRAM_BOT=tu_token_de_telegram
     DB_HOST=localhost
     DB_USER=usuario
     DB_PASSWORD=contraseña
     DB_NAME=monitoreo
     ```

---

## **Uso**

### **Bot de Telegram**
- Interactúa con el Bot usando los siguientes comandos:
  - `/start`: Muestra el menú principal.
  - `/Historico Notificaciones`: Consulta el histórico de notificaciones.
  - `/Estado Actual Del Servidor`: Consulta el estado actual de los servidores.
  - `/cancel`: Finaliza la conversación.

---

## **Despliegue**
### **Agentes de Monitoreo**
- Instala y ejecuta los agentes en cada servidor Linux.
- Configura un cron job para ejecutar el agente cada 5 minutos:
  ```bash
  */5 * * * * python /ruta/al/agente_monitoreo.py
  ```

### **Servicio Centralizado**
- Despliega el servicio en un servidor con acceso a la base de datos y a Internet.
- Usa un servidor web como Nginx o Apache para exponer la API.

### **Bot de Telegram**
- Aloja el Bot en el mismo servidor que el Servicio Centralizado o en un servidor separado.

---

## **Contribución**
Si deseas contribuir al proyecto, sigue estos pasos:
1. Haz un fork del repositorio.
2. Crea una rama para tu contribución:
   ```bash
   git checkout -b mi-contribucion
   ```
3. Realiza tus cambios y haz commit:
   ```bash
   git commit -m "Descripción de los cambios"
   ```
4. Envía un pull request.

---

## **Licencia**
Este proyecto está bajo libre licencia.

---

## **Contacto**
Si tienes alguna pregunta o sugerencia, no dudes en contactarme:
- **Nombre**: Junior A Celis Bedoya
- **Email**: jr.main.396@gmail.com
- **GitHub**: https://github.com/juniorCelis96
