# Program to convert a decimal number to binary using a nested loop

def decimal_to_binary(n):
    # Find the highest power of 2 less than or equal to n
    binary = ""
    powers = []
    temp = n
    while temp > 0:
        power = 0
        while (2 ** power) <= temp:
            power += 1
        power -= 1
        powers.append(power)
        temp -= 2 ** power

    # Build the binary string using nested loop
    for i in range(max(powers), -1, -1):
        found = False
        for p in powers:
            if p == i:
                binary += "1"
                found = True
                break
        if not found:
            binary += "0"
    return binary

# Example usage
num = int(input("Enter a decimal number: "))
print(f"Binary representation: {decimal_to_binary(num)}")