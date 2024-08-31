# Checkpoint exercise - after Loops - "Marketplace" example.


# Online Marketplace Data Structure
marketplace = {
    'products': [
        {'id': 1, 'name': "Laptop", 'category_id': 1, 'price': 1000, 'stock': 20},
        {'id': 2, 'name': "Mobile Phone", 'category_id': 2, 'price': 500, 'stock': 30},
        {'id': 3, 'name': "Washing Machine", 'category_id': 3, 'price': 700, 'stock': 10},
    ],
    'categories': [
        {'id': 1, 'name': "Electronics"},
        {'id': 2, 'name': "Mobiles"},
        {'id': 3, 'name': "Home Appliances"},
    ],
    'orders': [
        {'id': 1, 'product_id': 1, 'quantity': 2, 'total_price': 2000},
        {'id': 2, 'product_id': 2, 'quantity': 1, 'total_price': 500},
        {'id': 3, 'product_id': 1, 'quantity': 1, 'total_price': 1000},
    ]
}

# Exercise 1: Print all product names in the marketplace
for product in marketplace['products']:
    print(product['name'])

# Exercise 2: List all categories and the number of products in each category
category_count = {}
for product in marketplace['products']:
    cat_id = product['category_id']
    if cat_id not in category_count:
        category_count[cat_id] = 0
    category_count[cat_id] += 1

for category in marketplace['categories']:
    print(f"{category['name']}: {category_count.get(category['id'], 0)} products")

# Exercise 3: Calculate the total revenue from all orders
total_revenue = sum(order['total_price'] for order in marketplace['orders'])
print(f"Total Revenue: ${total_revenue}")

# Exercise 4: Find the most popular product based on the number of orders
from collections import Counter
popular_product = Counter(order['product_id'] for order in marketplace['orders'])
most_popular_id = popular_product.most_common(1)[0][0]
most_popular_product = next(product for product in marketplace['products'] if product['id'] == most_popular_id)
print(f"Most popular product is: {most_popular_product['name']}")

# Exercise 5: Update the stock of 'Laptop' by decreasing it by 5
for product in marketplace['products']:
    if product['name'] == 'Laptop':
        product['stock'] -= 5

# Exercise 6: Remove any product with a stock less than 15
marketplace['products'] = [product for product in marketplace['products'] if product['stock'] >= 15]

# Exercise 7: Print the details of orders with a total price higher than $1000
high_value_orders = [order for order in marketplace['orders'] if order['total_price'] > 1000]
print(f"High-value orders: {high_value_orders}")

# Exercise 8: Add a new category and a new product in that category
new_category = {'id': 4, 'name': "Clothing"}
new_product = {'id': 4, 'name': "T-Shirt", 'category_id': 4, 'price': 25, 'stock': 50}
marketplace['categories'].append(new_category)
marketplace['products'].append(new_product)

# Exercise 9: Calculate the average price of all products
avg_price = sum(product['price'] for product in marketplace['products']) / len(marketplace['products'])
print(f"Average price: ${avg_price}")

# Exercise 10: List all orders for the product with id 1
orders_for_product_1 = [order for order in marketplace['orders'] if order['product_id'] == 1]
print(f"Orders for product with id 1: {orders_for_product_1}")
