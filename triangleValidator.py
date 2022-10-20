# Triangle Validator

# For a triangle to be valid, the sum of measures of two sides must always be greater than the measure of the third side.

# For a triangle to be a equilateral, all its sides must be equal.
# For a triangle to be a isoceles, two sides must be equals and one different.
# For a triangle to be scalene, all sides must be different.

side1 = float(input("First side: "))
side2 = float(input("Second side: "))
side3 = float(input("Third side: "))

if (side1 < side2 + side3 and side2 < side1 + side3 and side3 < side1 + side2):
    print("\nCan be a Triangle!\n")

    if (side1 == side2 == side3):
        print("Equilateral")
    elif (side1 != side2 != side3 != side1):
        print("Scalene")
    else:
        print("Isoceles")
else: 
    print("This sides cannot be a Triangle!")