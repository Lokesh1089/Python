age = 10

if age > 18:
    print("You can Vote")
elif age == 18:
    print("Please Apply for voter id")
else:
    print("You are not eligible")


User_name, Password = "rajesh", "raj1234"

if User_name == "raj" and Password == "raj123":
    print("You are logged in Successfully !")
elif User_name != "raj" and Password == "raj123":
    print("Please check your userName")
elif User_name == "raj" and Password != "raj123":
    print("Please check your Password")
else:
    print("Invalid Log in credential")

a, b = 10, 15
if a == 10 or b == 15:
    print("Correct")
    if b == 15:
        print("Fifteen")
else:
    print("Incorrect")

