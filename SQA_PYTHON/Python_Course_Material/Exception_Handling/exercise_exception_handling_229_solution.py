"""
Given a list of products print name of all products that have price under 25.
If product does not have a price print a message indicating the product does not have a price then skip it.

"""

products = [
    {'id': 1, 'name': 't-shirt', 'price': 12.99, 'created_date': '2022-01-01', 'is_on_sale': False, 'sale_price': None},
    {'id': 2, 'name': 'shoes', 'price': 22.45, 'created_date': '2022-01-01', 'is_on_sale': False, 'sale_price': None},
    {'id': 3, 'name': 'dress-shirt', 'price': 43.00, 'created_date': '2022-01-01', 'is_on_sale': False, 'sale_price': None},
    {'id': 4, 'name': 'socks', 'price': 14.99, 'created_date': '2022-01-01', 'is_on_sale': True, 'sale_price': 7.99},
    {'id': 5, 'name': 'trousers', 'price': 32.50, 'created_date': '2022-01-01', 'is_on_sale': False, 'sale_price': None},
    {'id': 5, 'name': 'trousers', 'created_date': '2022-01-01', 'is_on_sale': False, 'sale_price': None},
    {'id': 6, 'name': 'jacket', 'price': 150.00, 'created_date': '2022-01-01', 'is_on_sale': False, 'sale_price': None},
]


#Ex1. Given list of products, print name of products that have price under 25

for i in products:
    try:
        if i['price'] < 25:
            print(i['name'])
    except:
        print("Found a product with no price. Logging in foo.log")
        # with open('foo.log', 'a') as f:
        #     f.write(f"no price for product: {i}")



