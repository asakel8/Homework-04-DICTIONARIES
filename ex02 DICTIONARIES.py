beverages = {
    "espresso": 2.0,
    "dopio": 2.4,
    "lungo": 3.0,
    "cappuccino": 3.2,
    "latte": 3.4,
    "flat white": 3.8,
    "americano": 2.8,
    "cold brew": 4.0
}

drink = input("What beverage would you like? ").lower()

if drink in beverages:
    print("The price is $", beverages[drink])
else:
    print("Sorry, this beverage is not available.")