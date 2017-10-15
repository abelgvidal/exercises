from money import Money
from rules import PricingRules


class Checkout():

    items = None
    pricing_rules = None

    def __init__(self, pricing_rules):
        if not isinstance(pricing_rules, PricingRules):
            raise TypeError("checkout must receive a PricingRules object")
        self.pricing_rules = pricing_rules
        self.items = {}

    def scan(self, item):
        if item not in self.items:
            self.items[item] = 1
        else:
            self.items[item] += 1

    def total(self):
        result = Money('0', 'EUR')

        for item, units in self.items.items():
            unit_price = self.pricing_rules.get_unit_price(
                item,
                units
            )
            result += unit_price * units

        return result


if __name__ == "__main__":  # pragma: no cover
    def new_checkout(items):
        pricing_rules = PricingRules('price_list.json')
        checkout = Checkout(pricing_rules)
        [checkout.scan(item) for item in items]
        return checkout.total()

    print('\nCheckout demo!')
    print("*" * 40, '\n')

    items = ['VOUCHER', 'TSHIRT', 'PANTS']
    print('Items: %s' % ' '.join(items))
    print('Total: %s\n' % new_checkout(items))

    items = ['VOUCHER', 'TSHIRT', 'VOUCHER']
    print('Items: %s' % ' '.join(items))
    print('Total: %s\n' % new_checkout(items))

    items = ['TSHIRT', 'TSHIRT', 'TSHIRT', 'VOUCHER', 'TSHIRT']
    print('Items: %s' % ' '.join(items))
    print('Total: %s\n' % new_checkout(items))

    items = ['VOUCHER', 'TSHIRT', 'VOUCHER',
             'VOUCHER', 'PANTS', 'TSHIRT', 'TSHIRT']
    print('Items: %s' % ' '.join(items))
    print('Total: %s\n' % new_checkout(items))
