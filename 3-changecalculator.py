# Create a program which you will enter the amount of money you have, it will also ask for the price of an apple.
# Display the maximum number of apples that you can buy and the remaining money that you will have.
# Display the output in the following format.
# You can buy ____ apples and your change is ____ pesos.

def getInitInfo():
    _AmountMoney = int(input("Please enter your current money balance: "))
    _PriceApple = int(input("Please enter the price of an apple: "))
    return _AmountMoney, _PriceApple

def ShowResult(AmountMoney, PriceApple):
    _MaxApples = AmountMoney // PriceApple
    _Change = AmountMoney % PriceApple
    return _MaxApples, _Change

def Display(MaxApples, Change):
    print(f"You can buy {MaxApples} apples and your change is {Change} pesos.")

# steps
# 1. Ask for the amount of money and the price of an apple
AmountMoney, PriceApple = getInitInfo()
# 2. Solve for the number of apples and change
MaxApples, Change = ShowResult(AmountMoney, PriceApple)
# 3. Display the maximum number of apples along with its corresponding change
Display(MaxApples, Change)