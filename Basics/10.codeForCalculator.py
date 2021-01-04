# Wrote a code to perform calculation based on getting input from user 

# Method 1

num1 = int(input("Enter First Number"))
num2 = int(input("Enter Second Number"))
print("""
Opertions 
1.add
2.sub
3.mult
4.div
""")
operation = int(input("What operation do you want to perform"))

if operation == 1:
    print(num1 + num2)
elif operation == 2:
    print(num1 - num2)
elif operation == 3:
    print(num1 * num2)
elif operation == 4:
    print(num1 // num2)
else:
    print("Please Enter Valid operation")


# Method 2


def add(a,b):
    return a + b


def sub(a, b):
    return a - b


def mult(a, b):
    return a * b


def div(a, b):
    return a // b


print("""
1. Addition
2. Subtraction
3. Multiplication
4. Division
""")
choice = int(input('Enter Your Choice'))
number1 = int(input('Enter first Number'))
number2 = int(input('Enter Second Number'))

if choice == 1:
    print(add(number1, number2))
elif choice == 2:
    print(sub(number1, number2))
elif choice == 3:
    print(mult(number1, number2))
elif choice == 4:
    print(div(number1, number2))
else:
    print("Enter Valid Operation")