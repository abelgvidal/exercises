from expects import expect, equal
from rules import PricingRules


with description('testing rules'):


    with before.each:
        self.pricing_rules = PricingRules('price_list.json')
    
    with it('discounted item as 2x1 is no discounted with 1 item'):
        unit_price = self.pricing_rules.get_unit_price('VOUCHER', 1)
        expect(unit_price.amount).to(equal(5))
 
    with it('discounted item as 2x1 is discounted with 2 items'):
        unit_price = self.pricing_rules.get_unit_price('VOUCHER', 2)
        expect(unit_price.amount).to(equal(2.5))
       
    with it('discounted item as 2x1 is discounted with 3 items'):
        unit_price = self.pricing_rules.get_unit_price('VOUCHER', 3)
        expect(str(unit_price.amount)[0:4]).to(equal('3.33'))

    with it('discounted item as 2x1 is discounted with 4 items'):
        unit_price = self.pricing_rules.get_unit_price('VOUCHER', 4)
        expect(unit_price.amount).to(equal(2.5))        

    with it('discounted item as 2x1 is discounted with 55 items'):
        unit_price = self.pricing_rules.get_unit_price('VOUCHER', 55)
        expect(str(unit_price.amount)[0:4]).to(equal('2.54'))

    with it('discounted item as >2 is discounted with 2 items'):
        unit_price = self.pricing_rules.get_unit_price('TSHIRT', 2)
        expect(unit_price.amount).to(equal(20))

    with it('discounted item as >2 is discounted with >2 items'):
        for count in range(3,13):
            unit_price = self.pricing_rules.get_unit_price('TSHIRT', count)
            expect(unit_price.amount).to(equal(19))

    with it('not discounted item is not discounted with 1-12 items'):
        for count in range(1, 13):
            unit_price = self.pricing_rules.get_unit_price('PANTS', count)
            expect(unit_price.amount).to(equal(7.5))
            
            
        
