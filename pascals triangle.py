num_rows = int(input("enter the rows:"))
for i in range(num_rows):
    for j in range(num_rows - i):
        print(" ", end="")
    
    coefficient = 1
    for j in range(i + 1):  # Use a different variable for the inner loop to avoid conflict
        print(coefficient, end=" ")
        coefficient = coefficient * (i - j) // (j + 1)
    
    print()

