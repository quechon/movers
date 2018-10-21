from flask import Flask
from .models import db
from .form import csrf
from .config import DevelopmentConfig

# Initialize app
app = Flask(__name__)

app.config.from_object(DevelopmentConfig)

# Initialize extentions
db.init_app(app)
csrf.init_app(app)


# Include view
from movers.main.view import main
from movers.api.view import api

app.register_blueprint(main)
app.register_blueprint(api, url_prefix='/api')
