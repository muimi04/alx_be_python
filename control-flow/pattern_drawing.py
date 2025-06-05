# pattern_drawing.py

# Prompt the user for the size of the pattern
size = int(input("Enter the size of the pattern: "))

# Initialize row counter
row = 0

# Use a while loop for rows
while row < size:
    # Use a for loop to print asterisks in the row
    for col in range(size):
        print("*", end="")
    # Print a newline to move to the next row
    print()
    # Move to the next row
    row += 1
    
