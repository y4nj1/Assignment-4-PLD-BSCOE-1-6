# Create a program that will ask how many apples and oranges you want to buy.
# Display the total amount you need to pay if apple price is 20 pesos and orange is 25.
# Display the output in the following format.
# The total amount is ________.

def showPrices():
    _PriceA = 20
    _PriceO = 25
    print(f"The price of an apple is {_PriceA} pesos.")
    print(f"The price of an orange is {_PriceO} pesos.")
    return _PriceA, _PriceO

def getQuantities():
    _AmountA = int(input("How many apples will you buy? "))
    _AmountO = int(input("How many oranges will you buy? "))
    return _AmountA, _AmountO

def totalPrice(PriceA, PriceO, AmountA, AmountO):
    _PriceApple = PriceA * AmountA
    _PriceOrange = PriceO * AmountO
    _PriceTotal = _PriceApple + _PriceOrange
    return _PriceTotal

def display(solve):
    print(f"The total amount is {solve} pesos.")
# steps
# 1. show the price of an apple and an orange
PriceA, PriceO = showPrices()
# 2. ask how many apples and oranges will they buy
AmountA, AmountO = getQuantities()
# 3. solve for the total price
solve = totalPrice(PriceA, PriceO, AmountA, AmountO)
# 4. display the total price
display(solve)