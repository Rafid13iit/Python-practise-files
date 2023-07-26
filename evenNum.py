# Take input from the user for the list of numbers
numbers = input("Enter a list of numbers, separated by spaces: ").split()

# Convert the input string into a list of integers
numbers = [int(num) for num in numbers]

# Print even numbers
print("Even numbers from the list:")
for num in numbers:
    if num % 2 == 0:
        print(num)

