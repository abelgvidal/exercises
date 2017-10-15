"""
This module contains rules for prices and the object PricingRules.

If you need to add new price functions:
 - add at least one item which this function applies to in the json
   file naming its function with the key "type" and other neccesary 
   attributes like code, name and unit_price. more attributes can also 
   be included if needed
 - define below the funcion with the same name which receives:
   - input: price_info, units
   - output: unit_price
 - add a new element to the PricingRules.rules dictionary
 - et voilá!
"""
import json
from money import Money
from utils import grouper

#
# define here new price functions
#
def xfory(price_info, units):
    """ function to discount per groups. if you pay Y you get X """
    total = 0
    x = price_info.get('x')
    y = price_info.get('y')
    price = price_info.get('unitPrice')

    for group in grouper(x, range(0, units)):
        has_discount = len(group) == x
        per_unit = price if not has_discount else y / x * price
        total = total + (per_unit * len(group))

    return total / units

def bulk(price_info, units):
    """ function for bulk discuount. if you buy more than X units 
        then you pay less per unit """
    has_discount = price_info["bulkNumber"] <= units
    price_key = "bulkPrice" if has_discount else "unitPrice"
    return price_info[price_key]

# no discount rule
unit = lambda price_info, units: price_info["unitPrice"]

#
# end of price functions
#


class PricingRules:
    """
    The object PricingRules takes a list for rules for prices 
    from a json file and matches them with price functions 
    so it can calculate any price for any number of items
    """
    rules = {}
    types = {
        "unit": unit,
        "xfory": xfory,
        "bulk": bulk,
    }

    def __init__(self, rules_file):
        with open(rules_file) as json_data:
            items = json.load(json_data)["items"]
            self.rules = {i['code']: i for i in items}

    def _get_price_func(self, _type):
        return self.types[_type]

    def get_unit_price(self, item_code, count):
        """ how much will I pay for X items for this type? """
        rule = self.rules.get(item_code)
        price_f = self._get_price_func(rule['type'])
        return Money(price_f(rule, count), 'EUR')
