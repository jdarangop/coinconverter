#!/usr/bin/env python3
""" Test Converter """
import unittest
from core.converter import Converter


class TestConverter(unittest.TestCase):
    """ Test the converter methods. """

    def test_check_amount_int(self):
        """ Test the check_amount method with an integer amount. """
        converter_test = Converter('LTC', '150', 'ETH')
        self.assertTrue(converter_test.check_amount())

    def test_check_amount_float(self):
        """ Test the check_amount method with an float amount. """
        converter_test = Converter('LTC', '33.78', 'ETH')
        self.assertTrue(converter_test.check_amount())

    def test_check_amount_string(self):
        """ Test the check_amount method with an string amount. """
        converter_test = Converter('LTC', '150none', 'ETH')
        self.assertFalse(converter_test.check_amount())

    def test_check_amount_negative(self):
        """ Test the check_amount method with an negative amount. """
        converter_test = Converter('LTC', '-33.78', 'ETH')
        self.assertFalse(converter_test.check_amount())

    def test_check_coins_wrong_input_coin(self):
        """ Test the check_coins with a wrong input_coin"""
        converter_test = Converter('ADA', '1', 'BCC')
        self.assertFalse(converter_test.check_coins())

    def test_check_coins_wrong_output_coin(self):
        """ Test the check_coins with a wrong input_coin"""
        converter_test = Converter('BCC', '1', 'DOGE')
        self.assertFalse(converter_test.check_coins())

    def test_check_coins_BTC_to_other(self):
        """ Test the check_coins between BTC and others. """
        types_of_coins = ('BTC', 'BCC', 'LTC', 'ETH', 'ETC', 'XRP')
        for coin in types_of_coins:
            converter_test = Converter('BTC', '1', coin)
            self.assertTrue(converter_test.check_coins())

    def test_check_coins_BCC_to_other(self):
        """ Test the check_coins between BCC and others. """
        types_of_coins = ('BTC', 'BCC', 'LTC', 'ETH', 'ETC', 'XRP')
        for coin in types_of_coins:
            converter_test = Converter('BCC', '2', coin)
            self.assertTrue(converter_test.check_coins())

    def test_check_coins_LTC_to_other(self):
        """ Test the check_coins between LTC and others. """
        types_of_coins = ('BTC', 'BCC', 'LTC', 'ETH', 'ETC', 'XRP')
        for coin in types_of_coins:
            converter_test = Converter('LTC', '1', coin)
            self.assertTrue(converter_test.check_coins())

    def test_check_coins_ETH_to_other(self):
        """ Test the check_coins between ETH and others. """
        types_of_coins = ('BTC', 'BCC', 'LTC', 'ETH', 'ETC', 'XRP')
        for coin in types_of_coins:
            converter_test = Converter('ETH', '1', coin)
            self.assertTrue(converter_test.check_coins())

    def test_check_coins_ETC_to_other(self):
        """ Test the check_coins between ETC and others. """
        types_of_coins = ('BTC', 'BCC', 'LTC', 'ETH', 'ETC', 'XRP')
        for coin in types_of_coins:
            converter_test = Converter('ETC', '1', coin)
            self.assertTrue(converter_test.check_coins())

    def test_check_coins_XRP_to_other(self):
        """ Test the check_coins between XRP and others. """
        types_of_coins = ('BTC', 'BCC', 'LTC', 'ETH', 'ETC', 'XRP')
        for coin in types_of_coins:
            converter_test = Converter('XRP', '1', coin)
            self.assertTrue(converter_test.check_coins())