from flask import Flask
from app.company.controller import company_api
import config
from utils.database import db

app = Flask(__name__)
app.config.from_object(config)
app.register_blueprint(company_api)

db.init_db()
