"""
PROJECT ID: 601

Create a script that will get list of products that are 'out of stock' using the WooCommerce API. 
Get products that are out of stock in the E-commerce site.
* The script should use the 'woocommerce' Python library
* The scrip should output a CSV file with 2 columns, 'product_id' & 'product_name'


Prerequisits:
    * API Key/Secret with Read access. (You must use site you created on your local or request API Key to http://demostore.supersqa.com/)
    * Your site (the site) must have some products that are out of stock. If no products exist then create some products that are out of stock using the API.

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



class OutOfStockProductsManager:
    """
    This class will get the products that are out of stock from the WooCommerce API.
    """
    def __init__(self):
        """
        This method will initialize the WooCommerce API and the list of products.
        """
        # <Your code here>
    
    def get_all_products(self,):
        """
        This method will get all the products from the WooCommerce API.

        Returns:
        list: The list of products.
        """
        # <Your code here>
    
    def get_out_of_stock_products(self):
        """
        This method will get the products that are out of stock.

        Returns:
        list: The list of products that are out of stock.
        """
        # <Your code here>
    
    def write_out_of_stock_products_to_csv(self):
        """
        This method will write the out of stock products to a csv file.
        """
        # <Your code here>