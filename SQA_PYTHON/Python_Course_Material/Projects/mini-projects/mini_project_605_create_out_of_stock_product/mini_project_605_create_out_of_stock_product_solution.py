""""
Project ID: 605

** Challenge **
Create a script that will generate a given number of products that are out of stock.

** Use Case **
There is a previous project (project id = 601) that is to list all products that are out of stock. 
But the site might not have any products that are out of stock. So in that case we need to prepare data for the
project. This script can be run to create out of stock products (data) to be used in project 601.


** Details **

You are tasked with creating a script that generates a specified number of out-of-stock products in a WooCommerce store. 
The script should use the woocommerce library to interact with the WooCommerce API and create products with random names. 
The number of products to be created should be provided as a command line argument.

Requirements:

1. WooCommerce API Setup:
   - Ensure you have the woocommerce library installed. You can install it using [`pip install woocommerce`].
   - Replace url, consumer_key, and consumer_secret with your WooCommerce store's details.

2. Script Functionality:
   - The script should generate random product names.
   - Each product should be created with the following attributes:
     - `name`: Randomly generated name.
     - `type`: "simple".
     - `regular_price`: <generate random price>.
     - `description`: Empty string.
     - `short_description`: Empty string.
     - `stock_quantity`: 0.
     - `manage_stock`: True.
   - The script should accept the number of products to be created as a command line argument.
   - The script should print the name and ID of each created product.

Prerequisits:
    * API Key/Secret with "Write" access. (You must use site you created on your local since 'write' api can not be provided to the public site)
   
   
** Example Usage **

Save the script as `create_out_of_stock_products.py` and run it from the terminal:

$ python create_out_of_stock_products.py 10

This command will create 10 out-of-stock products in your WooCommerce store.

"""

import random
import string
import sys
from woocommerce import API



# Initialize WooCommerce API
# Sicne this requires 'write' access you have to use your own site.
wcapi = API(
    url="http://yourstore.com",  
    consumer_key="ck_your_consumer_key",
    consumer_secret="cs_your_consumer_secret",
    version="wc/v3"
)

def generate_random_product_name():
    """
    This function generates a random product name.

    Returns:
    str: The random product name.
    """
    rand_string = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))
    print(f"Generated a random string: {rand_string}")
    return rand_string

def create_out_of_stock_product():
    """
    This function creates an out-of-stock product in the WooCommerce store.
    """
    print(f"Creating a random product that is out of stock.")
    product_name = generate_random_product_name()
    data = {
        "name": product_name,
        "type": "simple",
        "regular_price": str(random.randint(5, 50)),
        "description": "This is a test product created using the WooCommerce API.",
        "short_description": "Test product",
        "manage_stock": True,
        "stock_quantity": 0
    }
    response = wcapi.post("products", data)
    
    assert response.status_code == 201, \
        f"Create product API call failed. \n Status code = {response.status_code} \n, Response body = {response.json()}"
    
    return response.json()

def main():
    """
    This function will create out of stock products in the WooCommerce store.
    """
    if len(sys.argv) != 2: # check that a command line argument is provided
        print("Usage: python create_out_of_stock_products.py <number_of_products>")
        sys.exit(1)

    try:
        num_products = int(sys.argv[1])
    except ValueError:
        print("Please provide a valid number for the number of products.")
        sys.exit(1)

    for i in range(num_products):
        print(f"Creating product {i} of {num_products}")
        product = create_out_of_stock_product()
        print(f"Created product: {product['name']} with Product ID: {product['id']}")

if __name__ == "__main__":
    main()
