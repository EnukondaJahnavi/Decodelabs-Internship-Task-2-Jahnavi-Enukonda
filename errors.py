from flask import jsonify
from werkzeug.exceptions import HTTPException

def register_error_handlers(app):
    @app.errorhandler(HTTPException)
    def handle_http_error(error):
        return jsonify({
            "success": False,
            "error": {
                "code": error.code,
                "message": error.description
            }
        }), error.code

    @app.errorhandler(Exception)
    def handle_unexpected_error(error):
        app.logger.exception("Unexpected server error")
        return jsonify({
            "success": False,
            "error": {
                "code": 500,
                "message": "Internal server error."
            }
        }), 500
