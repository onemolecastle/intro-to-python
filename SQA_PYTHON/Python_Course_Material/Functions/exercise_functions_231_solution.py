"""
Convert Temperature

Write two functions that convert temperature between Celsius and Fahrenheit.

The first function should be called celsius_to_fahrenheit and take one argument, celsius,
which is a temperature in degrees Celsius. The function should return the equivalent temperature in degrees Fahrenheit.

The second function should be called fahrenheit_to_celsius and take one argument, fahrenheit,
which is a temperature in degrees Fahrenheit. The function should return the equivalent temperature in degrees Celsius.

The functions should return the converted value with 2 decimal points.

The formula to convert celsius to fahrenheit -> fahrenheit = (celsius * 9/5) + 32
The formula to convert fahrenheit to celsius -> celsius = (fahrenheit - 32) * 5/9

Test you functions:
    - 25 degree celsius converts to 77.0 fahrenheit
    - 72 degree fahrenheit converts to 22.22 celsius
"""


def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius

celsius = 25
fahrenheit = celsius_to_fahrenheit(celsius)
print(f"{celsius} degrees Celsius is equal to {fahrenheit} degrees Fahrenheit.")

fahrenheit = 72
celsius = fahrenheit_to_celsius(fahrenheit)
print(f"{fahrenheit} degrees Fahrenheit is equal to {celsius} degrees Celsius.")
