print("Enter Marks Obrained in 5 subject:")
mark1 = int(input())
mark2 = int(input())
mark3 = int(input())
mark4 = int(input())
mark5 = int(input())
tot = mark1 + mark2 + mark3 + mark4 + mark5
print("Total Marks Obtained: ", tot)
avg = tot / 5
print("Average Marks Obtained: ", avg)
if avg >= 90:
    print("Grade: A")
elif avg >= 80:
    print("Grade: B")
elif avg >= 80:
    print("Grade: c")


