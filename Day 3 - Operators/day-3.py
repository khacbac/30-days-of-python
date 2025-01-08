print(True)
print(False)
print(3 / 2) # division
print(3 // 2) # floor division
print(3 ** 2) # exponentiation
print(3 % 2) # modulus
print('Addition: ', 1 + 2)        # 3
print('Subtraction: ', 2 - 1)     # 1
print('Multiplication: ', 2 * 3)  # 6
print ('Division: ', 4 / 2)       # 2.0  Division in Python gives floating number
print('Division: ', 6 / 2)        # 3.0         
print('Division: ', 7 / 2)        # 3.5
print('Division without the remainder: ', 7 // 2)   # 3,  gives without the floating number or without the remaining
print ('Division without the remainder: ',7 // 3)   # 2
print('Modulus: ', 3 % 2)         # 1, Gives the remainder
print('Exponentiation: ', 2 ** 3) # 9 it means 2 * 2 * 2
# Floating numbers
print("\n\n--> Floating numbers")
print('Floating Point Number, PI', 3.14)
print('Floating Point Number, gravity', 9.81)
# Complex numbers
print("\n\n--> Complex numbers")
print('Complex number: ', 1 + 1j)
print('Multiplying complex numbers: ',(1 + 1j) * (1 - 1j))
# Calculating area of a circle
print("\n\n--> Calculating area of a circle")
radius = 10                                 # radius of a circle
area_of_circle = 3.14 * radius ** 2         # two * sign means exponent or power
print('Area of a circle:', area_of_circle)
# Calculating area of a rectangle
print("\n\n--> Calculating area of a rectangle")
length = 10
width = 20
area_of_rectangle = length * width
print('Area of rectangle:', area_of_rectangle)

# Calculating a weight of an object
print("\n\n--> Calculating a weight of an object")
mass = 75
gravity = 9.81
weight = mass * gravity
print(weight, 'N')                         # Adding unit to the weight

# Calculate the density of a liquid
print("\n\n--> Calculate the density of a liquid")
mass = 75 # in Kg
volume = 0.075 # in cubic meter
density = mass / volume # 1000 Kg/m^3
print("density", density, "Kg/m^3")

# Comparison Operators
print("\n\n--> Comparison Operators")
print(3 > 2)     # True, because 3 is greater than 2
print(3 >= 2)    # True, because 3 is greater than 2
print(3 < 2)     # False,  because 3 is greater than 2
print(2 < 3)     # True, because 2 is less than 3
print(2 <= 3)    # True, because 2 is less than 3
print(3 == 2)    # False, because 3 is not equal to 2
print(3 != 2)    # True, because 3 is not equal to 2
print(len('mango') == len('avocado'))  # False
print(len('mango') != len('avocado'))  # True
print(len('mango') < len('avocado'))   # True
print(len('milk') != len('meat'))      # False
print(len('milk') == len('meat'))      # True
print(len('tomato') == len('potato'))  # True
print(len('python') > len('dragon'))   # False


# Comparing something gives either a True or False
print("\n\n--> Comparing something gives either a True or False")
print('True == True: ', True == True)
print('True == False: ', True == False)
print('False == False:', False == False)

print('1 is 1', 1 is 1)                   # True - because the data values are the same
print('1 is not 2', 1 is not 2)           # True - because 1 is not 2
print('A in Asabeneh', 'A' in 'Asabeneh') # True - A found in the string
print('B in Asabeneh', 'B' in 'Asabeneh') # False - there is no uppercase B
print('coding' in 'coding for all') # True - because coding for all has the word coding
print('a in an:', 'a' in 'an')      # True
print('4 is 2 ** 2:', 4 is 2 ** 2)   # True

# Logical Operators
print("\n\n--> Logical Operators")
print(3 > 2 and 4 > 3) # True - because both statements are true
print(3 > 2 and 4 < 3) # False - because the second statement is false
print(3 < 2 and 4 < 3) # False - because both statements are false
print('True and True: ', True and True)
print(3 > 2 or 4 > 3)  # True - because both statements are true
print(3 > 2 or 4 < 3)  # True - because one of the statements is true
print(3 < 2 or 4 < 3)  # False - because both statements are false
print('True or False:', True or False)
print(not 3 > 2)     # False - because 3 > 2 is true, then not True gives False
print(not True)      # False - Negation, the not operator turns true to false
print(not False)     # True
print(not not True)  # True
print(not not False) # False

# Exercises - Day 3
print("\n\n--> Exercises - Day 3")
# Declare your age as integer variable
age = 25
# Declare your height as a float variable
height = 1.75
# Declare a variable that store a complex number
complex_number = 1 + 1j
# Write a script that prompts the user to enter base and height of the triangle and calculate an area of this triangle (area = 0.5 x b x h).
base = float(input("Enter the base of the triangle: "))
height = float(input("Enter the height of the triangle: "))
area = 0.5 * base * height
print("The area of the triangle is:", area)
# Write a script that prompts the user to enter side a, side b, and side c of the triangle. Calculate the perimeter of the triangle (perimeter = a + b + c).
a = float(input("Enter the side a of the triangle: "))
b = float(input("Enter the side b of the triangle: "))
c = float(input("Enter the side c of the triangle: "))
perimeter = a + b + c
print("The perimeter of the triangle is:", perimeter)
# Writ a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?
# Enter hours: 40
# Enter rate per hour: 28
# Your weekly earning is 1120
hours = float(input("Enter the hours: "))
rate = float(input("Enter the rate per hour: "))
pay = hours * rate
print("Your weekly earning is:", pay)
# Write a Python script that displays the following table
# 1 1 1 1 1
# 2 1 2 4 8
# 3 1 3 9 27
# 4 1 4 16 64
# 5 1 5 25 125
n = int(input("Enter the number: "))
for i in range(1, n + 1):
    print(i, i, i**2, i**3, i**4)