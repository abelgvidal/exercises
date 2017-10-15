from expects import expect, equal, raise_error
from checkout import Checkout
from rules import PricingRules

pricing_rules = PricingRules('price_list.json')

with description('testing checkout'):

    with before.each:
        self.checkout = Checkout(pricing_rules)

    with it('total with voucher, tshirt, pants'):
        [self.checkout.scan(item) for item in ['VOUCHER','TSHIRT', 'PANTS']]
        expect(self.checkout.total().amount).to(equal(32.50))

    with it('total with voucher, tshirt, voucher'):
        [self.checkout.scan(item) for item in ['VOUCHER','TSHIRT', 'VOUCHER']]
        expect(self.checkout.total().amount).to(equal(25))

    with it('total with tshirt, tshirt, tshirt, voucher, tshirt'):
        [self.checkout.scan(item) for item in ['TSHIRT','TSHIRT','TSHIRT','VOUCHER','TSHIRT']]
        expect(self.checkout.total().amount).to(equal(81))
        
    with it('total with one pant'):
        self.checkout.scan('PANTS')
        expect(self.checkout.total().amount).to(equal(7.5))

    with it('total with four pants'):
        [self.checkout.scan('PANTS') for i in range(0,4)]
        expect(self.checkout.total().amount).to(equal(30))

        
    with it('testing checkout construct receives pricing_rule object'):
        pricing_rules = PricingRules('price_list.json')
        checkout = Checkout(pricing_rules)
        expect(checkout.pricing_rules).to(equal(pricing_rules))

    with it('testing checkout fails when not receiving PricingRules object'):
        def callback():
            pricing_rules = object()
            c = Checkout(pricing_rules)
            
        expect(callback).to(raise_error(TypeError))
