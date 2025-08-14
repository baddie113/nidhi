n = int(input("Enter the value of n: "))
o = int(input("Enter the value you want to reach: "))
print ("numbers from {0} to {1} are: ".format(n,o))

for i in range(n,o):
    if i%2 != 0:
        print(i)