from rules import ItemRule


class Item():
    code = None
    name = None
    price = None

class Checkout():
    
    def __init__(self, pricing_rules):
        self.pricing_rules = pricing_rules 

    pricing_rules = None


