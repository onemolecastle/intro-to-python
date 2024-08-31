"""
PROJECT ID: 602

Create a script that will create a CSV file with all product that have prices missing.
Use the WooCommerce API for your ecom site (or demostore.supersqa.com if you have API Keys).
The product api has several prices in the fields. One of them is 'regular_price'.
Check every product and list all products that do not have price available.

* The script should output a CSV with 2 columns, 'product_id' and 'product_name' and 'type' (type is the price type can be 'regular_price', 'sale_price', 'price')
* Use the 'woocommerce' python library"


Prerequisits:
    * API Key/Secret with Read access. (You must use site you created on your local or request API Key to http://demostore.supersqa.com/)
    * Your site (the site) must have some products that are missing the price. If no products exist then create some products that have the 'regular_price' missing.


Helpful Info:
    * If you do not have your website created yet you can follow these instructions to create your site:
        1. Create Real E-Commerce Site for QA Testing: Installing WordPress - (Part 1 of 3) (https://www.youtube.com/watch?v=KhLGXIxeJLI&t=468s&ab_channel=SuperSQA)
        2. Create Real E-Commerce Site for QA Testing: Configuring The Site - (Part 2 of 3) (https://www.youtube.com/watch?v=w47JR3aoTNw&ab_channel=SuperSQA)
        3. Create Real E-Commerce Site for QA Testing: Verify The API The Frontend Checkout - (Part 3 of 3) (https://www.youtube.com/watch?v=qwCY8UEWqqM&ab_channel=SuperSQA)
Notes:
    * Creadentials should be stored in a .env file in the 'CREDENTIALS' folder.
    * The .env file should contain the following keys:
        * WC_URL
        * WC_CONSUMER_KEY
        * WC_CONSUMER_SECRET
"""



class MissingPriceProductsManager:
    """
    This class will get the products that are out of stock from the WooCommerce API.
    """
    def __init__(self):
        """
        This method will initialize the WooCommerce API and the list of products.
        """
        # <Your code here>
    
    def get_all_products(self):
        """
        This method will get all the products from the WooCommerce API.

        Returns:
        list: The list of products.
        """
        # <Your code here>
    
    def get_missing_price_products(self):
        """
        This method will get the products that are out of stock.

        Returns:
        list: The list of products that are out of stock.
        """
        # <Your code here>
    
    def write_missing_price_products_to_csv(self):
        """
        This method will write the missing price products to a csv file.
        """
        # <Your code here>