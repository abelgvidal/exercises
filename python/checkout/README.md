# Checkout Kata Python

- [Instructions](#instructions)
- [How to use](#how-to-use-this-solution)

## Instructions

A physical store which sells 3 products:

``` 
Code         | Name                |  Price
-------------------------------------------------
VOUCHER      | Voucher         |   5.00€
TSHIRT       | Summer T-Shirt  |  20.00€
PANTS        | Summer Pants    |   7.50€
```

The different departments have agreed these discounts:

 * A 2-for-1 special on `VOUCHER` items.

 * If you buy 3 or more `TSHIRTS` the price per unit should be 19.00€.
  
 * Items can be scanned in any order, and the cashier should return the total amount to be paid.
 
The interface for the checkout process has these specifications:
 * The Checkout constructor receives a pricing_rules object
 * The Checkout object has a scan method that receives one item at a time.

```python
pricing_rules = PricingRules('price_list.json')
co = Checkout(pricing_rules)
co.scan("VOUCHER")
co.scan("VOUCHER")
co.scan("TSHIRT")
price = co.total()
```

Examples:

    Items: VOUCHER, TSHIRT, PANTS
    Total: 32.50€

    Items: VOUCHER, TSHIRT, VOUCHER
    Total: 25.00€

    Items: TSHIRT, TSHIRT, TSHIRT, VOUCHER, TSHIRT
    Total: 81.00€

    Items: VOUCHER, TSHIRT, VOUCHER, VOUCHER, PANTS, TSHIRT, TSHIRT
    Total: 74.50€

## How to use

This implementation uses [Python 3.6.1](https://www.python.org/)

For your convenience a Dockerfile and a Makefile is included so you don't have to install this version of python and its dependencies. You only need docker running.

To run the application in the shell use 

`make build`

and then run it  

`make run`

or to run tests

`make test`

and to see test coverage

`make coverage`

If you don't use docker, you'll have to install Python >=3.6.1 and create a virtual enviroment `pip install -r requirements` before running Checkout module.
