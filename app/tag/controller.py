from flask import request, g, current_app
from flask.blueprints import Blueprint

from app.company.service import get_auto_search_by_company_name, get_by_company_name
from utils.web_utils import process_api

tag_api = Blueprint('tag_api', __name__)


@tag_api.route('/tag', methods=['GET'])
@process_api
def get_company_search_by_tag_name(lang=None):
    d = request.args.get('query')
    print(d)
    raise Exception


@tag_api.route('/companies/<company_code>/tags', methods=['PUT'])
@process_api
def update_new_tag(lang=None):
    json_data = g.json
    raise Exception

