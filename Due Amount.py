y = 2.5

print("Your bill amount: 2.5 (you don't have the exact amount, please enter more than 3$)")

x = float(input("enter your amount: "))

if x < 3:
    print("PLEASE CHOOSE A AMOUNT MORE THAN 3$")
else:
    print("Your change:")
    print(x - y)