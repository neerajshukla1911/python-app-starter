from sanic import Blueprint
from .demo_api import demo_api

api_v1 = Blueprint('api_v1')


api_v1.add_route(demo_api, '/demo-api/', methods=['GET'])