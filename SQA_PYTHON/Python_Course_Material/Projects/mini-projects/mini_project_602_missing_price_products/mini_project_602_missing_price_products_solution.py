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

from woocommerce import API
import csv
import os

class MissingPriceProductsManager:
    """
    This class will get the products that are out of stock from the WooCommerce API.
    """
    def __init__(self):
        """
        This method will initialize the WooCommerce API and the list of products.
        """
        self.current_path = os.path.dirname(os.path.realpath(__file__))
        
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
       
        self.products = self.get_all_products()
        
    def get_all_products(self):
        """
        This method will get all the products in the WooCommerce API.

        Returns:
        list: The list of products.
        """

        print("Getting list of all products.")
        print(f"Getting the frist page")

        response = self.wcapi.get("products")
        products:list = response.json()
        page_count = response.headers["X-WP-TotalPages"]
        for page in range(2, int(page_count)+1):
            print(f"Getting page # {page} of {page_count}")
            response = self.wcapi.get("products", params={"page": page})
            products.extend(response.json())
        
        print(f"Total number of products fetched: {len(products)}")

        return products
    
    def get_missing_price_products(self):
        """
        This method will get the products that are missing the price and output them to a CSV file.
        """
        price_types = ["regular_price", "sale_price", "price"] # The price types to check for.
        missing_price_products = []
        for product in self.products: 
            for price_type in price_types:
                if not product.get(price_type):
                    missing_price_products.append((product["id"], product["name"], price_type))
        
        print(f"Total number of product missing prices: {len(missing_price_products)}")

        self.save_missing_price_products(missing_price_products)
        
    def save_missing_price_products(self, missing_price_products):
        """
        This method will save the missing price products to a CSV file.
        
        Args:
        missing_price_products: list: The list of missing price products.
        """
        csv_file_path = os.path.join(self.current_path, "missing_price_products.csv")
        
        print(f"Saving output to: {csv_file_path}")
        
        with open(csv_file_path, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["PRODUCT ID", "PRODUCT NAME", "TYPE"])
            writer.writerows(missing_price_products)

if __name__ == "__main__":
    print(f"Running script to get all products that are missing price")
    missing_price_products_manager = MissingPriceProductsManager()
    missing_price_products_manager.get_missing_price_products()