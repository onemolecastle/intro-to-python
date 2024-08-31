"""
PROJECT ID: 603

Write a script that will update all prices on the ecom site by 10%.
The script should get list of all available products and increase the price by 10%.
Use the WooCommerce API to get products and to update the prices.

* Must use a 'Class' in your script.
* Use the WooCommerce API and the 'woocommerce' Python library.
* The script should output a csv file with 3 columns that has the product_id, old_price, new_price
* If a product does not have a price it should skip it
* The script should output another file with list of product ids there were skipped."
* So 2 files are expected to be outputed


Prerequisits:
    * API Key/Secret with READ/WRITE access. (You must use site you created on your local or request API Key to http://demostore.supersqa.com/)
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


class UpdateProductPrices:
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
        
    def update_product_prices(self):
        """
        This method will update the prices of the products by 10%.
        """
        # <Your code here>
    
    def write_updated_prices_to_csv(self):
        """
        This method will write the updated prices to a csv file.
        """
        # <Your code here>
    
    def write_skipped_products_to_csv(self):
        """
        This method will write the skipped products to a csv file.
        """
        # <Your code here>