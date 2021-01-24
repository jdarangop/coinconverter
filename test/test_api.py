#!/usr/bin/env python3
""" Test API """
import unittest
import requests


class TestAPI(unittest.TestCase):
    """ Test the API. """

    # Test a request missing input_coin
    def test_no_input_coin(self):
        """ Test if no passed input_coin. """
        answer = requests.get('http://localhost:5000/converter?amount=100&output_coin=ETH')
        self.assertEqual(answer.status_code, 400)

    # Test a request missing amount
    def test_no_amount(self):
        """ Test if no passed amount. """
        answer = requests.get('http://localhost:5000/converter?input_coin=BCC&output_coin=ETH')
        self.assertEqual(answer.status_code, 400)

    # Test a request missing output_coin
    def test_no_output_coin(self):
        """ Test if no passed output_coin. """
        answer = requests.get('http://localhost:5000/converter?input_coin=BCC&amount=100')
        self.assertEqual(answer.status_code, 400)

    # Should throw an exception: BTC to ETH is not supported.
    def test_BTC_to_ETH(self):
        """ Test BTC to ETH convertion. """
        answer = requests.get('http://localhost:5000/converter?input_coin=BTC&amount=100&output_coin=ETH')
        self.assertEqual(answer.status_code, 404)

    def test_BTC_to_other(self):
        """ Test the API with BTC as an input_coin """
        types_of_coins = ('BCC', 'LTC', 'ETC', 'XRP')
        for coin in types_of_coins:
            answer = requests.get('http://localhost:5000/converter?input_coin=BTC&amount=100&output_coin={}'.format(coin))
            if coin in ('BCC', 'LTC', 'ETC', 'XRP'):
                self.assertEqual(answer.status_code, 400)
            else:
                self.assertEqual(answer.status_code, 200)

    def test_BCC_to_other(self):
        """ Test the API with BCC as an input_coin """
        types_of_coins = ('BTC', 'LTC', 'ETH', 'ETC', 'XRP')
        for coin in types_of_coins:
            answer = requests.get('http://localhost:5000/converter?input_coin=BCC&amount=100&output_coin={}'.format(coin))
            if coin in ('BCC', 'LTC', 'ETC', 'XRP'):
                self.assertEqual(answer.status_code, 400)
            else:
                self.assertEqual(answer.status_code, 200)

    def test_LTC_to_other(self):
        """ Test the API with LTC as an input_coin """
        types_of_coins = ('BTC', 'BCC', 'ETH', 'ETC', 'XRP')
        for coin in types_of_coins:
            answer = requests.get('http://localhost:5000/converter?input_coin=LTC&amount=100&output_coin={}'.format(coin))
            if coin in ('BCC', 'LTC', 'ETC', 'XRP'):
                self.assertEqual(answer.status_code, 400)
            else:
                self.assertEqual(answer.status_code, 200)

    def test_ETH_to_other(self):
        """ Test the API with ETH as an input_coin """
        types_of_coins = ('BTC', 'BCC', 'LTC', 'ETC', 'XRP')
        for coin in types_of_coins:
            answer = requests.get('http://localhost:5000/converter?input_coin=ETH&amount=100&output_coin={}'.format(coin))
            if coin in ('BCC', 'LTC', 'ETC', 'XRP'):
                self.assertEqual(answer.status_code, 400)
            else:
                self.assertEqual(answer.status_code, 200)

    def test_ETC_to_other(self):
        """ Test the API with ETC as an input_coin """
        types_of_coins = ('BTC', 'BCC', 'LTC', 'ETH', 'XRP')
        for coin in types_of_coins:
            answer = requests.get('http://localhost:5000/converter?input_coin=ETC&amount=100&output_coin={}'.format(coin))
            if coin in ('BCC', 'LTC', 'ETC', 'XRP'):
                self.assertEqual(answer.status_code, 400)
            else:
                self.assertEqual(answer.status_code, 200)

    def test_XRP_to_other(self):
        """ Test the API with XRP as an input_coin """
        types_of_coins = ('BTC', 'BCC', 'LTC', 'ETH', 'ETC')
        for coin in types_of_coins:
            answer = requests.get('http://localhost:5000/converter?input_coin=XRP&amount=100&output_coin={}'.format(coin))
            if coin in ('BCC', 'LTC', 'ETC', 'XRP'):
                self.assertEqual(answer.status_code, 400)
            else:
                self.assertEqual(answer.status_code, 200)

    def test_coin_with_same_coin(self):
        """ Test the API with the coin with itself. """
        types_of_coins = ('BTC', 'BCC', 'LTC', 'ETH', 'ETC', 'XRP')
        for coin in types_of_coins:
            answer = requests.get('http://localhost:5000/converter?input_coin={}&amount=100&output_coin={}'.format(coin, coin))
            self.assertEqual(answer.status_code, 400)