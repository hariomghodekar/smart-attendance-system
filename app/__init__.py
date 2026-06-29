from flask import Flask

from config import Config
from extensions import db, login_manager


def create_app():

    app = Flask(__name__)

    app.config.from_object(Config)

    db.init_app(app)
    login_manager.init_app(app)

    with app.app_context():
        db.create_all()

    from app.routes.dashboard import dashboard_bp
    from app.routes.student import student_bp
    from app.routes.auth import auth_bp

    app.register_blueprint(dashboard_bp)
    app.register_blueprint(student_bp)
    app.register_blueprint(auth_bp)

    return app