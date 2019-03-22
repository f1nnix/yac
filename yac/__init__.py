from flask import Flask

from yac.db import db


def create_app(config_filename):
    app = Flask(__name__)
    app.config.from_pyfile('settings.cfg')

    db.init_app(app)

    # from yourapplication.views.admin import admin
    # from yourapplication.views.frontend import frontend
    # app.register_blueprint(admin)
    # app.register_blueprint(frontend)

    return app
