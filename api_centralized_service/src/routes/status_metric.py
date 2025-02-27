import psutil
import socket
from flask import Blueprint, jsonify, request
from src.models.history_metrics_model import HistoricModel

status_metrics_bp = Blueprint('status_metrics', __name__)


@status_metrics_bp.route('/')
def get_status_metrics():
    try:
        # Capturar métricas
        hostname = socket.gethostname()
        ip_address = socket.gethostbyname(hostname)
        ram_uso = psutil.virtual_memory().percent
        cpu_uso = psutil.cpu_percent(interval=1)
        disco_uso = psutil.disk_usage('/').percent

        response = {
            "hostname": hostname,
            "ip": ip_address,
            "ram": ram_uso,
            "cpu": cpu_uso,
            "disco": disco_uso
        }

        return jsonify(response)
    except Exception as e:    
        return jsonify({'message': f'No se logro obtener la métrica actual: {(str(e))}', 'status_code: ': 500})