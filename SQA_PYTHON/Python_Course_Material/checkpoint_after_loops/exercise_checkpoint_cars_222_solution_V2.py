# Checkpoint exercise - after Loops - "Cars" example.

# Cars data structure
cars = [
    {
        "make": "Toyota",
        "model": "Camry",
        "year": 2019,
        "mileage": 45000,
        "color": "Silver",
        "price": 15000,
        "is_available": True
    },
    {
        "make": "Honda",
        "model": "Accord",
        "year": 2020,
        "mileage": 30000,
        "color": "Blue",
        "price": 18000,
        "is_available": False
    },
    {
        "make": "Ford",
        "model": "Mustang",
        "year": 2018,
        "mileage": 25000,
        "color": "Red",
        "price": 25000,
        "is_available": True
    },
    {
        "make": "Chevrolet",
        "model": "Camaro",
        "year": 2021,
        "mileage": 5000,
        "color": "Yellow",
        "price": 30000,
        "is_available": True
    },
    {
        "make": "Nissan",
        "model": "Altima",
        "year": 2017,
        "mileage": 60000,
        "color": "Black",
        "price": 12000,
        "is_available": False
    }
]

# Exercise 1: Print the make and model of each car
for car in cars:
    print(car["make"], car["model"])

# Exercise 2: Calculate the average mileage of the available cars
available_mileage_total = 0
available_car_count = 0

for car in cars:
    if car["is_available"]:
        available_mileage_total += car["mileage"]
        available_car_count += 1

average_mileage = available_mileage_total / available_car_count
print("Average Mileage:", average_mileage)

# Exercise 3: Find the most expensive car
most_expensive_car = None

for car in cars:
    if most_expensive_car is None or car["price"] > most_expensive_car["price"]:
        most_expensive_car = car

print("Most Expensive Car:", most_expensive_car["make"], most_expensive_car["model"])

# Exercise 4: Check if any car has a mileage greater than 50,000
has_high_mileage = False

for car in cars:
    if car["mileage"] > 50000:
        has_high_mileage = True
        break

print("Any car with mileage greater than 50,000?", has_high_mileage)

# Exercise 5: Calculate the total price of all cars
total_price = 0

for car in cars:
    total_price += car["price"]

print("Total Price of all cars:", total_price)

# Exercise 6: Count the number of available cars
available_car_count = 0

for car in cars:
    if car["is_available"]:
        available_car_count += 1

print("Number of available cars:", available_car_count)

# Exercise 7: Update the price of all cars by 10% if the year is earlier than 2020
for car in cars:
    if car["year"] < 2020:
        car["price"] = int(car["price"] * 1.1)

# Exercise 8: Print the details of cars with prices greater than $20,000
expensive_cars = []

for car in cars:
    if car["price"] > 20000:
        expensive_cars.append(car)

for car in expensive_cars:
    print(car)

# Exercise 9: Find the oldest car
oldest_car = None

for car in cars:
    if oldest_car is None or car["year"] < oldest_car["year"]:
        oldest_car = car

print("Oldest Car:", oldest_car["make"], oldest_car["model"])
