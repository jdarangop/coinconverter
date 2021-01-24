#!/usr/bin/env python3
""" Contains the API """
from flask import Flask, request, jsonify
from core.converter import Converter


app = Flask(__name__)


@app.route("/converter", methods=['GET'], strict_slashes=False)
def coinconverter():
    """ coinconverter """

    input_coin = request.args.get('input_coin')
    amount = request.args.get('amount')
    output_coin = request.args.get('output_coin')

    if input_coin is None or amount is None or output_coin is None:
        return jsonify({"error": "Bad Request"}), 400

    conversion = Converter(input_coin, amount, output_coin)

    if conversion.check_amount is False:
        return jsonify({"error": "Bad amount"}), 400

    if conversion.check_coins is False:
        return jsonify({"error": "The API only support BTC, BCC, LTC, ETH, ETC, XRP convertions"}), 404

    if input_coin == output_coin:
        return jsonify({"error": "input_coin must be different to output_coin"}), 400

    if output_coin in ('BCC', 'LTC', 'ETC', 'XRP'):
        return jsonify({"error": "Convertions to BCC, ETC, XRP or LTC are not supported"}), 400

    answer = conversion.convert()

    if answer is None:
        return jsonify({"error": "BTC to ETH conversion not supported"}), 404

    return jsonify(answer), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000', debug='on')
