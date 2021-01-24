#!/usr/bin/env python3
""" Perform the convertion """
import requests


class Converter(object):
    """ class Converter """

    def __init__(self, input_coin, amount, output_coin):
        """ Initializer.
            Args:
                input_coin: (str) coin to be converted.
                amount: (str) amount to be converted.
                output_coin: (str) coin to which it will be converted.
        """
        self.input_coin = input_coin
        self.amount = amount
        self.output_coin = output_coin

    def check_amount(self):
        """ Check if the amount is valid.
            Args:
                value: (str) value to check.
            Returns:
                (True) If the amount is valid.
                (False) If the amount is invalid.
        """
        allowed_characters = ".0123456789"
        for char in self.amount:
            if char not in allowed_characters:
                return False
        return True

    def check_coins(self):
        """ Check if the coin input and output are in the formats allowed.
            Args:
                None.
            Return:
                (True) If the coin formats are well.
                (False) If the coin formats are no allowed.
        """
        allowed_formats = ('BTC', 'BCC', 'LTC', 'ETH', 'ETC', 'XRP')

        if self.input_coin in allowed_formats and self.output_coin in allowed_formats:
            return True
        else:
            return False

    def convert(self):
        """ Convert the amount from the input coin to the output coin.
            Args:
                None.
            Returns:
                Value converted.
        """
        convertions = requests.get('https://api.binance.com/api/v3/ticker/price?').json()
        concat_coin = self.input_coin + self.output_coin

        # The binance api does not support BTCETH conversion.
        if concat_coin == 'BTCETH':
            return None

        convertion = next(conver for conver in convertions if conver.get('symbol') == concat_coin)
        convertion_factor = float(convertion.get('price'))

        result = convertion_factor * float(self.amount)

        answer = {"input coin": self.input_coin,
                  "output coin": self.output_coin,
                  "input amount": float(self.amount),
                  "output amount": result}

        return answer
