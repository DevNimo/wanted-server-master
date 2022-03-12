from flask import request, g, current_app
from flask.blueprints import Blueprint
from app.models import Company
from utils.web_utils import process_api

company_api = Blueprint('company_api', __name__)


@company_api.route('/search', methods=['GET'])
@process_api
def get_company_name_autocomplete(lang=None):
    db = current_app.config['my_database']
    return print(type(db))


@company_api.route('/companies/<company_code>', methods=['GET'])
@process_api
def get_company_search(company_code, lang=None):
    print(company_code)
    raise Exception


@company_api.route('/companies', methods=['POST'])
@process_api
def create_new_company(lang=None):
    json_data = g.json
    raise Exception


@company_api.route('/tag', methods=['GET'])
@process_api
def get_company_search_by_tag_name(lang=None):
    d = request.args.get('query')
    print(d)
    raise Exception


@company_api.route('/companies/<company_code>/tags', methods=['PUT'])
@process_api
def update_new_tag(lang=None):
    json_data = g.json
    raise Exception
