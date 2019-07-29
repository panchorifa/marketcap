"""
Market REST API
"""
import traceback

from flask import Flask, jsonify, request
from market.service import MarketService, ServiceError
from market.settings import DEFAULT_COINS_LIMIT

MARKET_SERVICE = MarketService()

def create_app():
    """ Flask app """
    app = Flask(__name__, static_url_path='')

    @app.route('/ping', methods=['GET'])
    def ping():
        """ Ping route """
        return jsonify(ping='pong')

    @app.route('/market', methods=['GET'])
    def get_coins():
        """
        Returns coins from coinmarketcap.com(settings.MARKET_URL)

        :statuscode 200: no error
        :statuscode 403: invalid creds
        """
        try:
            limit = request.args.get('limit', DEFAULT_COINS_LIMIT)
            limit =  None if limit == '0' else int(limit)
            market = MARKET_SERVICE.market(limit)
            return jsonify({'market': market.json()})
        except Exception:
            traceback.print_exc()

    @app.route('/coins/<name>', methods=['GET'])
    def get_coin(name):
        """
        Returns coin from coinmarketcap.com(settings.COIN_URL)

        :statuscode 200: no error
        :statuscode 403: invalid creds
        """
        try:
            coin = MARKET_SERVICE.coin(name)
            values = coin.json()
            values['name'] = name.lower().capitalize()
            return jsonify({'coin': values})
        except ServiceError as error:
            traceback.print_exc()
            return 'error', error.status_code


    @app.before_request
    def option_autoreply():
        """
        Always reply 200 on OPTIONS request
        """
        if request.method == 'OPTIONS':
            resp = app.make_default_options_response()

            headers = None
            if 'ACCESS_CONTROL_REQUEST_HEADERS' in request.headers:
                headers = request.headers['ACCESS_CONTROL_REQUEST_HEADERS']

            resp_headers = resp.headers

            # Allow the origin which made the XHR
            resp_headers['Access-Control-Allow-Origin'] = \
                request.headers['Origin']
            # Allow the actual method
            resp_headers['Access-Control-Allow-Methods'] = \
                request.headers['Access-Control-Request-Method']
            # Allow for 10 seconds
            resp_headers['Access-Control-Max-Age'] = "10"

            # keep current headers
            if headers is not None:
                resp_headers['Access-Control-Allow-Headers'] = headers
            return resp


    @app.after_request
    def set_allow_origin(resp):
        """
        Set origin for GET, POST, PUT, DELETE requests
        """
        resp_headers = resp.headers
        # Allow crossdomain for other HTTP Verbs
        if request.method != 'OPTIONS' and 'Origin' in request.headers:
            resp_headers['Access-Control-Allow-Origin'] = \
                request.headers['Origin']
        return resp

    return app

create_app()
