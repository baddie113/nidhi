def check_age(age_input):
    try:
        age = int(age_input)
        if age < 0 or age > 150:
            print("Error: Invalid age entered.")
        else:
            print("The age entered is correct.")
            if age % 2 == 0:
                print("The age is even.")
            else:
                print("The age is odd.")
    except ValueError:
        print("Error: Please enter a valid number for age.")
user_input = input("Enter your age: ")
check_age(user_input)