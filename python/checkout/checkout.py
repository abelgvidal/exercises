class Product():
    code = None
    name = None
    price = None


class PricingRules():
    pass


class Checkout():
    
    def __init__(self, pricing_rules):
        self.pricing_rules = pricing_rules 

    pricing_rules = None
