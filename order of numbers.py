# Input: Choose a number greater than 0
while start <= 0:
    print("Please enter a number greater than 0.")
    start = int(input("Choose a number greater than 0: "))

# Input: Choose a number less than 101
end = int(input("Choose a number less than 101: "))
while end >= 101:
    print("Please enter a number less than 101.")
    end = int(input("Choose a number less than 101: "))

print(f"Numbers from {start} to {end}:")

if start < end:
    for i in range(start, end + 1):
        print(i)
else:
    for i in range(start, end - 1, -1):
        print(i)



