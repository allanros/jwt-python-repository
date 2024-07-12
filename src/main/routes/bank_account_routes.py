from flask import Blueprint, request, jsonify
from src.views.http_types.http_request import HttpRequest

from src.main.composer.user_register_composer import user_register_composer
from src.main.composer.login_creator_composer import login_creator_composer
from src.main.composer.balance_editor_composer import balance_editor_composer

bank_routes_bp = Blueprint('bank_routes', __name__)

@bank_routes_bp.route('/test', methods=['POST'])
def route_test():
    http_request = HttpRequest(body=request.json)
    return jsonify(http_request.body), 200

@bank_routes_bp.route('/bank/registry', methods=['POST'])
def registry_user():
    http_request = HttpRequest(body=request.json)
    response = user_register_composer().handle(request=http_request)

    return jsonify(response.body), response.status_code

@bank_routes_bp.route('/bank/login', methods=['POST'])
def create_login():
    http_request = HttpRequest(body=request.json)
    response = login_creator_composer().handle(request=http_request)

    return jsonify(response.body), response.status_code

@bank_routes_bp.route('/bank/balance/<int:user_id>', methods=['PATCH'])
def edit_balance(user_id):
    http_request = HttpRequest(body=request.json, params={'user_id': user_id})
    response = balance_editor_composer().handle(request=http_request)

    return jsonify(response.body), response.status_code
