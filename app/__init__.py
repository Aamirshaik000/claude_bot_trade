"""Flask application factory."""

from flask import Flask

from .dashboard.routes import dashboard_bp


def create_app() -> Flask:
    app = Flask(__name__)
    app.config.from_mapping(
        SECRET_KEY="dev",
        BINANCE_BASE_URL="https://api.binance.com",
    )

    app.register_blueprint(dashboard_bp)
    return app
