from expects import *
from checkout import PricingRules, Checkout


with description('testing checkout'):

    with it('testing pricing rules'):
        pricing_rules = PricingRules()
        checkout = Checkout(pricing_rules)
        expect(checkout.pricing_rules).to(equal(pricing_rules))
