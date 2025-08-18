try:
    number = int(input("Please enter a number: "))
    print("the number entered is: ", number)
except ValueError as ex:
    print("Exeption: ", ex)