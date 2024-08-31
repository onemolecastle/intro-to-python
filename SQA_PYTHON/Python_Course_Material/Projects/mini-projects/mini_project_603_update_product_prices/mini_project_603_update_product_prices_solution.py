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

from woocommerce import API
import csv
import os

class UpdateProductPrices:
    """
    This class will get the products that are out of stock from the WooCommerce API.
    """
    def __init__(self, price_update_percent):
        """
        This method will initialize the WooCommerce API and the list of products.
        """
        self.price_update_percent = price_update_percent
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

        self.products = []
        self.all_products = self.get_all_products()
        self.update_prices()
        
    def get_all_products(self, ):
        """
        This method will get all the products in the WooCommerce API.

        Returns:
        list: The list of products.
        """
        response = self.wcapi.get("products")
        products:list = response.json()
        page_count = response.headers["X-WP-TotalPages"]
        for page in range(2, int(page_count)+1):
            print(f"Getting page # {page} of {page_count}")
            response = self.wcapi.get("products", params={"page": page})
            products.extend(response.json())

        print(f"Total number of products fetched: {len(products)}")
        return products

    def update_prices(self):
        """
        This method will update the prices of the products by 10%.

        Args:
        : The WooCommerce API object.
        """
        print(f"Starting to update prices of {len(self.all_products)} products")
        skipped_products = []
        for prod in self.all_products:
            product_id = prod["id"]
            old_price = prod["regular_price"]
            
            if old_price == "": # Skip products that do not have a price
                skipped_products.append({"PRODUCT ID": product_id, "PRODUCT NAME": prod["name"]})
                continue
            
            multiplier = 1 + (self.price_update_percent / 100)
            new_price = round(float(old_price) * multiplier, 2) # Increase the price by 10%
            response = self.wcapi.put(f"products/{product_id}", {"regular_price": str(new_price)})
            if response.status_code == 200:
                self.update_products_list(product_id, prod["name"], old_price, new_price)
                print(f"Updated product id {product_id}, old_price={old_price}, new_price={new_price}")
            else:
                print(f"Product {product_id} could not be updated.")
        
        print(f"Total skipped products: {len(skipped_products)}")
        
        self.save_skipped_products(skipped_products)
    
    def update_products_list(self, product_id, product_name, old_price, new_price):
        """
        This method will update the products list with the product id and product name.
        
        Args:
        product_id (int): The product id.
        product_name (str): The product name.
        old_price (str): The old price.
        new_price (str): The new price.
        """
        self.products.append({
            "PRODUCT ID": product_id,
            "PRODUCT NAME": product_name,
            "OLD PRICE": old_price,
            "NEW PRICE": new_price
        })
    
    def save_skipped_products(self, skipped_products):
        """
        This method will save the skipped products to a CSV file.
        
        Args:
        skipped_products: list: The list of skipped products.
        """
        
        csv_file = os.path.join(self.current_path, "skipped_products.csv")
        
        print(f"Saving skipped products to: {csv_file}")
        
        with open(csv_file, mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=["PRODUCT ID", "PRODUCT NAME"])
            writer.writeheader()
            writer.writerows(skipped_products)
    
    def save_updated_prices(self):
        """
        This method will save the updated prices to a CSV file.
        """
        
        csv_file = os.path.join(self.current_path, "updated_prices.csv")

        print(f"Saving updated products list to: {csv_file}")
        
        with open(csv_file, mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=["PRODUCT ID", "PRODUCT NAME", "OLD PRICE", "NEW PRICE"])
            writer.writeheader()
            writer.writerows(self.products)
        
if __name__ == "__main__":

    percent_to_update_by = 10
    print(f"Starting script to update product prices. Updating prices by {percent_to_update_by}%")

    update_product_prices = UpdateProductPrices(percent_to_update_by)
    update_product_prices.save_updated_prices()