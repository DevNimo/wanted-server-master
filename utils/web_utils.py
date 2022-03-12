import json

from functools import wraps
from flask import request, jsonify, g
from werkzeug.wrappers import Response


def process_api(api_func):
    @wraps(api_func)
    def decorator(*args, **kwargs):
        try:
            lang = request.headers.get('x-wanted-language')
            ret = api_func(*args, lang=lang, **kwargs)
            if type(ret) == Response:
                return ret
            return _make_response(ret)
        except Exception as e:
            return _make_error_response(e)

    return decorator


def _make_response(result):
    if result is None:
        return Response()
    return Response(response=json.dumps(result, ensure_ascii=False), mimetype='application/json')


def _make_error_response(result_msg, code=0):
    resp = jsonify({"code": code, 'message': str(result_msg)})
    resp.status_code = 404

    return resp

