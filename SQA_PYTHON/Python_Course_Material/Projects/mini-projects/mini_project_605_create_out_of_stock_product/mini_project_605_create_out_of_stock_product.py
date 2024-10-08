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


from woocommerce import API

# Initialize WooCommerce API
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
    # <Your code goes here>

def create_out_of_stock_product():
    """
    This function will create a single out of stock product in the WooCommerce store.
    
    Returns:
    dict: The response from the API.
    """
    # <Your code goes here>

def main():
    """
    This function will create out of stock products in the WooCommerce store.
    """
    # <Your code goes here>
if __name__ == "__main__":
    main()
