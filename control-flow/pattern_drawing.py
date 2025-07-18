
size = int(input("Enter the size of the pattern: "))
row = 0
while row < size:
    for col in range(size):
        print("*", end="")  # Print star without newline
    print()  # Move to the next line after each row
    row += 1  # Move to the next row
