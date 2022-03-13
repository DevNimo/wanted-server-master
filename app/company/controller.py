from flask import request
from flask.blueprints import Blueprint

from app.company import service
from utils.web_utils import process_api

company_api = Blueprint('company_api', __name__)


@company_api.route('/search', methods=['GET'])
@process_api
def get_company_name_autocomplete(lang=None):
    company_name = request.args.get('query')
    return service.get_auto_search_by_company_name(company_name, lang)


@company_api.route('/companies/<company_name>', methods=['GET'])
@process_api
def get_company_search(company_name, lang=None):
    res = service.get_by_company_name(company_name, lang)
    if 'company_name' not in res:
        raise Exception
    return res


@company_api.route('/companies', methods=['POST'])
@process_api
def create_new_company(lang=None):
    json_data = request.get_json()
    return service.create_new_company(json_data, lang)
