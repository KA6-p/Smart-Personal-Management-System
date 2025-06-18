from math import e
import random
import string

def calculator():
    print("\n--- Calculator---")
    try:
        expression = input("Enter a mathematical expression: ")
        result = eval(expression)
        print(f"Result: {result}")
    except:
        print(f"Error: {e}")

def unit_convertor():
    print("\n --- Unit Converter ---")
    print("1- Kilometers to meters")
    print("2- Metres to Kilometers")
    print("3- Kilograms to grams")
    print("4- Grams to Kilograms")
    print("5- Farheniet to Celsius")
    print("6- Celsius to Farheniet")
    option = int(input("Choose an option(1-6): "))
    if option == 1:
        km = float(input("Enter data in km: "))
        metres = km * 100
        print(f"{km}km is equal to {metres}metres") 
    elif option == 2:
        m = float(input("Enter data in m: "))
        km= m/100
        print(f"{m}metre is equal to {km}km")
    elif option == 3:
        kg = float(input("Enter data in kg: "))
        g = kg * 1000
        print(f"{kg}kg is equal to {g}grams")
    elif option == 4:
        g= float(input("Enter data in grams: "))
        kg= g/1000
        print(f"{g}grams is equal to {kg}kgs")
    elif option == 5:
        f = float(input("Enter temperature in Fahrenhiet: "))
        c = 5/9 * (f-32)
        print(f"{f} degrees in Fahrenhiet equal to {c}degrees in celsius")
    elif option == 6:
        c = float(input("Enter temperature in Celsius: "))
        f = (9/5) * c + 32
        print(f"{c} degrees in celsius equal to {f} degrees in Fahrenhiet")
    else:
        print("Invalid Choice!")

def random_password_generator():
    print("\n--- Random Password Generator ---")
    try:
        length = int(input("Enter the desired password length: "))
        if length < 1:
            print("Password must be atleast 1")
            return
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for _ in range(length))
        print(f"Generated Password: {password}")
    except ValueError:
        print("Please enter a valid number")    
