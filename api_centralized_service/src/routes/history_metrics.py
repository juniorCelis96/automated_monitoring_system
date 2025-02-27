from flask import Blueprint, jsonify, request
from src.models.history_metrics_model import HistoricModel

history_metrics_bp = Blueprint('history_metrics', __name__)


@history_metrics_bp.route('/')
def get_history_metrics():
    try:
        historics = HistoricModel.get_historics()
        return jsonify(historics)
    except Exception as e:    
        return jsonify({'message': f'No se logro obtener las métricas históricas: {(str(e))}', 'status_code: ': 500})