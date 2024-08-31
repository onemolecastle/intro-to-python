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

# Exercise 2: List all categories and the number of products in each category

# Exercise 3: Calculate the total revenue from all orders

# Exercise 4: Find the most popular product based on the number of orders

# Exercise 5: Update the stock of 'Laptop' by decreasing it by 5

# Exercise 6: Remove any product with a stock less than 15

# Exercise 7: Print the details of orders with a total price higher than $1000

# Exercise 8: Add a new category and a new product in that category

# Exercise 9: Calculate the average price of all products

# Exercise 10: List all orders for the product with id 1
