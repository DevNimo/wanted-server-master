from flask import request, g, current_app
from flask.blueprints import Blueprint

from app.company.service import get_auto_search_by_company_name, get_by_company_name
from utils.web_utils import process_api

company_api = Blueprint('company_api', __name__)


@company_api.route('/search', methods=['GET'])
@process_api
def get_company_name_autocomplete(lang=None):
    company_name = request.args.get('query')
    return get_auto_search_by_company_name(company_name, lang)


@company_api.route('/companies/<company_name>', methods=['GET'])
@process_api
def get_company_search(company_name, lang=None):
    res = get_by_company_name(company_name, lang)
    if 'company_name' not in res:
        raise Exception
    return res


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

