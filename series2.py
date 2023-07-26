# Prompt the user to enter the value of n
n = int(input("Enter the value of n: "))

# Initialize a variable to store the sum
total = 0

# Prompt the user to enter n numbers and calculate the sum
for i in range(n):
    num = float(input("Enter number {}: ".format(i+1)))
    total += num

# Display the sum
print("The sum of the {} numbers is: {}".format(n, total))