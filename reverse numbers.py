num = int(input("Type the number you want to see reversed: ")) 
original_num = num  # Save the original number
rev = 0 

while num > 0:
    x = num % 10 
    rev = rev * 10 + x 
    num = num // 10

print("Reversed number is:", rev)

if original_num == rev:
    print("This is a palindrome!")
else:
    print("This is not a palindrome.")