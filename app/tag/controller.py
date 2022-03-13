from flask import request
from flask.blueprints import Blueprint

from app.tag import service
from utils.web_utils import process_api

tag_api = Blueprint('tag_api', __name__)


@tag_api.route('/tags', methods=['GET'])
@process_api
def get_compnay_by_tag(lang=None):
    tag_name = request.args.get('query')
    return service.get_compnay_by_tag(tag_name, lang)


@tag_api.route('/companies/<company_name>/tags', methods=['PUT'])
@process_api
def update_new_tag(company_name, lang=None):
    json_data = request.get_json()
    return service.tag_update_by_company(company_name, json_data, lang)


@tag_api.route('/companies/<company_name>/tags/<tag_name>', methods=['DELETE'])
@process_api
def delete_tag_by_company(company_name, tag_name, lang=None):
    return service.tag_delete_by_company(company_name, tag_name, lang)
