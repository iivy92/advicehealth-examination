from flask import Flask
from flask import jsonify
from src.handlers.person import handler_person
from src.handlers.vehicle import handler_vehicle
from src.utils.exceptions import InvalidUsage


def create_app():
    app = Flask(__name__)
    
    app.register_blueprint(handler_person)
    app.register_blueprint(handler_vehicle)

    @app.errorhandler(InvalidUsage)
    def handle_invalid_usage(error):
        response = jsonify(error.to_dict())
        response.status_code = error.status_code
        return response

    return app
