# Prompt the user to enter five numbers
print("Enter five numbers:")
numbers = []
for i in range(5):
    num = float(input("Number {}: ".format(i+1)))
    numbers.append(num)

# Calculate the sum of the numbers
total = sum(numbers)

# Display the sum
print("The sum of the numbers is : " + str(total))