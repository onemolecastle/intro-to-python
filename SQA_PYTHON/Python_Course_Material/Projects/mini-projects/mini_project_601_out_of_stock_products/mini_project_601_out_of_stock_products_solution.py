"""
PROJECT ID: 601

Create a script that will get list of products that are 'out of stock' using the WooCommerce API. 
Get products that are out of stock in the E-commerce site.
* The script should use the 'woocommerce' Python library
* The scrip should output a CSV file with 2 columns, 'product_id' & 'product_name'


Prerequisits:
    * API Key/Secret with Read access. (You must use site you created on your local or request API Key to http://demostore.supersqa.com/)
    * Your site (the site) must have some products that are out of stock. 
       If no products exist then create some products that are out of stock using the API.
       Work on "project id = 605" to create products that are out of stock

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

from woocommerce import API
import csv
import os

class OutOfStockProductsManager:
    """
    This class will get the products that are out of stock from the WooCommerce API.
    """
    def __init__(self):
        """
        This method will initialize the WooCommerce API and the list of products.
        """
        self.current_path = os.path.dirname(os.path.realpath(__file__))
        print(f"Getting WooCommerce credentials from environment variable")
        url = os.getenv("WC_URL")
        consumer_key = os.getenv("WC_CONSUMER_KEY")
        consumer_secret = os.getenv("WC_CONSUMER_SECRET")

        if not all([url, consumer_key, consumer_secret]):
            raise Exception(f"Environment variables 'WC_URL', 'WC_CONSUMER_KEY' and 'WC_CONSUMER_SECRET' must be set.")
        
        print(f"Executing for site: {url}")
        
        self.wcapi = API(
            url=url,
            consumer_key=consumer_key,
            consumer_secret=consumer_secret,
            version="wc/v3"
        )
       
        self.all_products = self.get_all_products()
        
    def get_all_products(self):
        """
        This method will get all the products in the WooCommerce API.

        Returns:
        list: The list of products.
        """

        print("Getting list of products")
        
        response = self.wcapi.get("products")
        products:list = response.json()
        page_count = response.headers["X-WP-TotalPages"]
        for page in range(2, int(page_count)+1):
            response = self.wcapi.get("products", params={"page": page})
            products.extend(response.json())

        print(f"Total number of products fetched: {len(products)}")

        return products

    def get_out_of_stock_products(self):
        """
        This method will get the products that are out of stock and output them to a CSV file.
        """
        
        out_of_stock_products = []
        for product in self.all_products:
            if product["stock_status"] != "instock":
                product_id = product["id"]
                product_name = product["name"]
                out_of_stock_products.append({"PRODUCT ID": product_id, "PRODUCT NAME": product_name})
        
        print(f"Total number of products out-of-stock: {len(out_of_stock_products)}")

        self.save_out_of_stock_products(out_of_stock_products)

    def save_out_of_stock_products(self, out_of_stock_products):
        """
        This method will save the out of stock products to a CSV file.

        Args:
        out_of_stock_products: list: The list of out of stock products.
        """

        out_put_file_name = "out_of_stock_products.csv"
        csv_file = os.path.join(self.current_path, out_put_file_name)
        print(f"Saving {len(out_of_stock_products)} out of stock products to a file. Output file: {csv_file}")

        with open(csv_file, mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=["PRODUCT ID", "PRODUCT NAME"])
            writer.writeheader()
            writer.writerows(out_of_stock_products)

if __name__ == "__main__":
    print(f"Starting script to get all products that are out of stock.")
    out_of_stock_products_manager = OutOfStockProductsManager()
    out_of_stock_products_manager.get_out_of_stock_products()