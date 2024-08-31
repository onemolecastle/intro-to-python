# Checkpoint exercise - after Loops - "Products" example.

# Mixed Product Data Structure
products = [
    {
        "id": 1,
        "name": "Laptop",
        "categories": ["Electronics", "Computers"],
        "price": 1000,
        "specs": {
            "RAM": "16GB",
            "Storage": "512GB SSD"
        },
        "in_stock": True
    },
    {
        "id": 2,
        "name": "Coffee Maker",
        "categories": ["Home Appliances"],
        "price": 100,
        "specs": {
            "Capacity": "12 Cups",
            "Auto Shut-Off": "Yes"
        },
        "in_stock": False
    },
    {
        "id": 3,
        "name": "Smartphone",
        "categories": ["Electronics", "Mobiles"],
        "price": 700,
        "specs": {
            "Screen Size": "6.1 inches",
            "Battery Life": "24 hours"
        },
        "in_stock": True
    }
]

# Exercise 1: Print the names and categories of each product
for product in products:
    print(f"Name: {product['name']}, Categories: {', '.join(product['categories'])}")

# Exercise 2: Calculate the average price of in-stock products
total_price = 0
count = 0
for product in products:
    if product['in_stock']:
        total_price += product['price']
        count += 1
average_price = total_price / count
print(f"Average Price of In-Stock Products: ${average_price}")

# Exercise 3: List products with more than one category
multi_cat_products = [product['name'] for product in products if len(product['categories']) > 1]
print(f"Products with multiple categories: {multi_cat_products}")

# Exercise 4: Print the specs of each in-stock product
for product in products:
    if product['in_stock']:
        print(f"{product['name']} Specs: {product['specs']}")

# Exercise 5: Find the most expensive in-stock product
most_expensive = max([product for product in products if product['in_stock']], key=lambda x: x['price'])
print(f"Most Expensive In-Stock Product: {most_expensive['name']}")

# Exercise 6: Count the number of in-stock products that have "Auto Shut-Off" feature
auto_shut_off_count = len([product for product in products if product['in_stock'] and product['specs'].get('Auto Shut-Off', 'No') == 'Yes'])
print(f"Number of in-stock products with Auto Shut-Off feature: {auto_shut_off_count}")

# Exercise 7: Update the price of all in-stock products by 10%
for product in products:
    if product['in_stock']:
        product['price'] *= 1.1

# Exercise 8: Print the names of products costing more than $200
expensive_products = [product['name'] for product in products if product['price'] > 200]
print(f"Products costing more than $200: {expensive_products}")

# Exercise 9: List products that belong to the 'Electronics' category
electronics = [product['name'] for product in products if 'Electronics' in product['categories']]
print(f"Electronics Products: {electronics}")

# Exercise 10: Calculate the average screen size of in-stock smartphones
smartphones = [product for product in products if product['in_stock'] and 'Mobiles' in product['categories']]
screen_sizes = [float(product['specs']['Screen Size'].split()[0]) for product in smartphones]
average_screen_size = sum(screen_sizes) / len(screen_sizes) if screen_sizes else 0
print(f"Average Screen Size of In-Stock Smartphones: {average_screen_size} inches")
