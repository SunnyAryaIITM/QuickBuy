import os
from flask import Flask

from application.config import LocalDevelopmentConfig
from application.database import db
from application.models import *
from application.controllers import *

app = None

def create_app():
    app = Flask(__name__, template_folder="templates")
    if os.getenv('ENV', "development") == "production":
        app.logger.info("Currently no production config is setup.")
        raise Exception("Currently no production config is setup.")
    else:
        app.logger.info("Staring Local Development.")
        print("Staring Local Development")
        app.config.from_object(LocalDevelopmentConfig)
    db.init_app(app)
    with app.app_context():
        # db.drop_all()
        db.create_all()
    app.register_blueprint(App)
    app.logger.info("App setup complete")
    return app

app = create_app()
app.secret_key="sunny@quick"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port = 5000)