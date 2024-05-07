from flask import Flask
from flask import Config

app = Flask(__name__)
# Flask configuration
app.config.from_object(Config)

from app import routes
