medical_cause = input("do you have a medical cause for not taking the exam? (yes/no)")
atten = int(input("Enter the attendance of the student: "))
if medical_cause == 'Y':
    print("You are allowed")
else:
    if atten >= 75:
        print("You are allowed to take the exam")
    else:
        print("Not allowed")