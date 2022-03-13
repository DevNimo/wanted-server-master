from flask import Flask
from app.company.controller import company_api
from app.tag.controller import tag_api
import config


app = Flask(__name__)
app.config.from_object(config)
app.register_blueprint(company_api)
app.register_blueprint(tag_api)


