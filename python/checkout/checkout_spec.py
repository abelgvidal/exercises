from expects import expect, equal
from checkout import Checkout
from rules import PricingRules


with description('testing checkout'):

    with it('testing checkout construct receives pricing_rule object'):
        pricing_rules = PricingRules("inventory.csv")
        checkout = Checkout(pricing_rules)
        expect(checkout.pricing_rules).to(equal(pricing_rules))
