from abc import ABCMeta, abstractmethod
from itertools import islice
import csv


class Rule:
    __metaclass__ = ABCMeta

    @abstractmethod
    def get_unit_price(count): raise NotImplementedError    


class ItemRule(Rule):
    price = 0
    count = 0
    price = 0
    strict_count = False

    def __init__(self, price, discount_count,
                 discount_price, strict_count):
        self.price = price
        self.discount_count = discount_count
        self.discount_price = discount_price
        self.strict_count = strict_count
    
    def get_unit_price(self, count):
        if not self.discount_count:
            return self.price

        total = 0
        
        if self.strict_count:
            groups = grouper(self.discount_count, range(0, count))
            for group in groups:
                has_discount = len(group) == self.discount_count
                per_unit= self.price if not has_discount else self.discount_price
                total = total + (per_unit * len(group))
        else:
            has_discount = count >= self.discount_count
            per_unit= self.price if not has_discount else self.discount_price
            total = per_unit * count

        return total / count

    
class PricingRules:
    """ item_rules is a dict of item_code -> ItemRule """
    item_rules = {}

    def __init__(self, rules_file):
        with open(rules_file, 'r') as csvfile:
            reader = csv.reader(csvfile, delimiter=",")
            next(reader) # skip header
            for row in filter(None, reader):
                code, _, price, disc_price, disc_count, strict = row
                self.item_rules[code] = ItemRule(float(price), int(disc_count), float(disc_price), bool(int(strict)))


    def get_item_unit_price(self, item_code, count):
        rule = self.item_rules.get(item_code, None)
        if not rule:
            raise ValueError
            
        return rule.get_unit_price(count);


def grouper(n, iterable):
    it = iter(iterable)
    while True:
        chunk = tuple(islice(it, n))
        if not chunk:
            return
        yield chunk        

