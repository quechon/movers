from flask import Flask
from .models import db

# Initialize app
app = Flask(__name__)

# Initialize extentions
db.init_app(app)


# Include view 
from movers import view
