from functools import wraps
from flask import request, make_response, jsonify
from myApp.User.models import User

def auth_decorator():
    def _auth_decorator(f):
        @wraps(f)
        def __auth_decorator(*args, **kwargs):
            # just do here everything what you need
            auth_header = request.headers.get('Authorization')
            if auth_header:
                auth_token = auth_header.split(" ")[1]
            else:
                auth_token = ''
            if auth_token:
                resp = User.decode_auth_token(auth_token)
                if(isinstance(resp, str)):
                    response_object={
                        'status': 'fail',
                        'message': resp
                    }
                    return make_response(jsonify(response_object))
                result = f(*args, **kwargs)
                return result
            else:
                response_object={
                    'status': 'fail',
                    'message': 'Token has not provided'
                }
                return make_response(jsonify(response_object)), 401
        return __auth_decorator
    return _auth_decorator