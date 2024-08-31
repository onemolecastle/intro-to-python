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
if False:
    for i in cars:
        print(f"Make = {i['make']}")
        print(f"Model = {i['model']}")
        print('------')



# Exercise 2: Calculate the average mileage of the available cars
# avg = total_amount/number_of_elements
if False:
    total_milage = 0
    number_of_cars = 0
    for i in cars:
        # if i['is_available'] == True: # this does same thing as next line
        if i['is_available']:
            # number_of_cars = number_of_cars + 1  # this does same thing as next line
            number_of_cars += 1
            current_car_milage = i['mileage']
            # total_milage = total_milage + current_car_milage
            total_milage += current_car_milage


    avg = total_milage/number_of_cars
    print(f"The average milage of available cars is: {avg}")


# Exercise 3: Find the most expensive car
if False:
    expensive_car = None
    for i in cars:
        # if expensive_car == None:
        if not expensive_car:
            expensive_car = i
        else:
            if i['price'] > expensive_car['price']:
                expensive_car = i
    print(f"The most expensive car is: {expensive_car['make']}, {expensive_car['model']}")


# Exercise 4: Check if any car has a mileage greater than 50,000
if False:
    for i in cars:
        if i['mileage'] > 50000:
            print(f"Car with over 50k miles = {i['make']}, {i['model']}")



# Exercise 5: Calculate the total price of all cars
if False:
    total_price = 0
    for i in cars:
        # total_price = total_price + i['price']
        total_price += i['price']

    print(f"The total price of all cars is: {total_price}")

# Exercise 6: Count the number of available cars
if False:
    # solution 1
    total_available_cars = 0
    for i in cars:
        if i['is_available']:  # Truthiness
            total_available_cars += 1

    print(f"Total number of available cars = {total_available_cars}")

    # solution 2
    available_cars = []
    for i in cars:
        if i['is_available']:  # Truthiness
            available_cars.append(i)
    print(f"Total number of available cars = {len(available_cars)}")



# Exercise 7: Update the price of all cars by 10% if the year is earlier than 2020
if False:
    cars_with_updated_price = []
    for i in cars:
        if i['year'] < 2020:
            current_price = i['price']
            new_price = current_price * 1.1
            new_price_int = int(new_price)
            i['price'] = new_price_int
            cars_with_updated_price.append(i)
        else:
            cars_with_updated_price.append(i)

    print(cars_with_updated_price)


# Exercise 8: Print the details of cars with prices greater than $20,000
if False:
    price_cutoff = 20000
    print(f"Here is list of cars with price over {price_cutoff}")
    for i in cars:
        if i['price'] > price_cutoff:
            print(f"Make: {i['make']}, Model: {i['model']}, Year: {i['year']}")


# Exercise 9: Find the oldest car
oldest_car = None
for car in cars:
    year = car['year']
    if not oldest_car:
        oldest_car = car
    elif year < oldest_car['year']:
        oldest_car = car
print(f"Oldest car is: {oldest_car['make']}, {oldest_car['model']}")