# All the exercises below are based on this data

online_store = {
    "storeName": "Everything Online",
    "address": {
        "street": "456 Digital Lane",
        "city": "Netville",
        "state": "Cyberspace",
        "zipCode": "101010"
    },
    "categories": ["Electronics", "Books", "Home & Garden", "Toys"],
    "products": [
        {"id": 101, "name": "Smartphone", "category": "Electronics", "price": 299.99, "ratings": [5, 4, 5, 4, 4]},
        {"id": 102, "name": "Laptop", "category": "Electronics", "price": 899.99, "ratings": [5, 5, 4, 4, 5]},
        {"id": 103, "name": "Coffee Maker", "category": "Home & Garden", "price": 74.99, "ratings": [4, 4, 3, 4, 5]},
        {"id": 104, "name": "E-Reader", "category": "Electronics", "price": 129.99, "ratings": [5, 4, 4, 5, 5]},
        {"id": 105, "name": "Gardening Set", "category": "Home & Garden", "price": 59.99, "ratings": [4, 4, 5, 5, 3]}
    ],
    "employees": [
        {"name": "Alice", "role": "Manager", "email": "alice@everythingonline.com"},
        {"name": "Bob", "role": "Sales Associate", "email": "bob@everythingonline.com"},
        {"name": "Charlie", "role": "Customer Service", "email": "charlie@everythingonline.com"}
    ],
    "contact": {
        "phone": "800-123-4567",
        "email": "support@everythingonline.com",
        "socialMedia": {
            "twitter": "@EverythingOnline",
            "facebook": "EverythingOnlineFB"
        }
    }
}

# Challenge 1: Store Name
store_name = online_store["storeName"]
print(store_name)

# Challenge 2: Number of Categories
num_categories = len(online_store["categories"])
print(num_categories)

# Challenge 3: City Location
store_city = online_store["address"]["city"]
print(store_city)

# Challenge 4: First Product Name
first_product_name = online_store["products"][0]["name"]
print(first_product_name)

# Challenge 5: Price of 'Coffee Maker'
coffee_maker_price = online_store["products"][2]["price"]  # Assumes a fixed position
print(coffee_maker_price)

# Challenge 6: Zip Code
zip_code = online_store["address"]["zipCode"]
print(zip_code)

# Challenge 7: Contact Email
contact_email = online_store["contact"]["email"]
print(contact_email)

# Challenge 10: Social Media Handles
twitter_handle = online_store["contact"]["socialMedia"]["twitter"]
facebook_handle = online_store["contact"]["socialMedia"]["facebook"]
print(twitter_handle)
print(facebook_handle)

# Challenge 11: Charlie's Role
charlie_role = online_store["employees"][2]["role"]  # Assumes a fixed position
print(charlie_role)

# Challenge 12: Employee Count
employee_count = len(online_store["employees"])
print(employee_count)

# Challenge 15: Street Address
street_address = online_store["address"]["street"]
print(street_address)

# Challenge 16: 'Smartphone' Ratings Count
smartphone_ratings_count = len(online_store["products"][0]["ratings"])
print(smartphone_ratings_count)
