from config import config
from flask import Flask
from flask_cors import CORS

from src.utils.error_handler import ErrorHandler

from src.routes.history_metrics import history_metrics_bp
from src.routes.status_metric import status_metrics_bp


def create_app(config_name):
    app = Flask(__name__)
    CORS(app, resources={"*": {"origins": "http://localhost:3000"}})
    app.config.from_object(config[config_name])
    app.register_blueprint(history_metrics_bp, url_prefix='/api/v1/historico-notificaciones')
    app.register_blueprint(status_metrics_bp, url_prefix='/api/v1/estado-actual')
    app.register_error_handler(404, ErrorHandler.page_not_found)
    return app

if __name__ == '__main__':
    app = create_app('development')
    app.run()