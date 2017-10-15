import json
from money import Money
from utils import grouper


unit = lambda price_info, units: price_info["unitPrice"]

def xfory(price_info, units):
    total = 0
    x = price_info.get('x')
    y = price_info.get('y')
    price = price_info.get('unitPrice')
    
    for group in grouper(x, range(0, units)):
        has_discount = len(group) == x
        per_unit= price if not has_discount else y / x * price 
        total = total + (per_unit * len(group))
        
    return total / units
    
def bulk(price_info, units):
    has_discount = price_info["bulkNumber"] <= units
    price_key = "bulkPrice" if has_discount else "unitPrice"
    return price_info[price_key]


class PricingRules:
    rules = {}
    types = {
        "unit": unit,
        "xfory": xfory,
        "bulk": bulk,
    }

    def __init__(self, rules_file):
        with open('price_list.json') as json_data:
            items = json.load(json_data)["items"]
            self.rules = {i['code']: i for i in items}

    def _get_price_func(self, _type):
        return self.types[_type]
            
    def get_unit_price(self, item_code, count):
        rule = self.rules.get(item_code)
        price_f = self._get_price_func(rule['type'])
        return Money(price_f(rule, count), 'EUR')
