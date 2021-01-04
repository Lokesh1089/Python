# Loops

colours = 'Blue'

for colour in colours:
    print(colour)


stationary = {'Pen', 'Pencil', 'Rubber', 'Scale'}

for things in stationary:
    print(things)


for i in "Hi, bro":
    if i == ',':
        print(", is present")
    else:
        print(", is not present")

days = {"Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"}
for day in days:
    if day == "Wednesday":
        print("Wednesday is present")
        break
    else:
        print("Wednesday is not present")


for dayn in days:
    if dayn == "Wednesday":
        continue
    # print("Wednesday is present")
    else:
        print("Wednesday is not present")


# Range

for numbers in range(5):
    print(numbers)
# With start & end Value
for num in range(2, 6):
    print(num)

# With interval
for number in range(10, 50, 10):
    print(number)

for nums in range(25, 100, 15):
    print(nums)

# for loop with else
for num1 in range(6):
    print(num1)
else:
    print("All numbers are printed")

# Nested for loop
for num2 in range(5, 10):
    print(num2)
    for num3 in range(2):
        print(num3)
    else:
        print("Mission Accomplished")

# While Loop

i = 1
while i < 5:
    print(i)
    i += 1

k = 5
while k <= 7:
    print(k)
    k += 1
else:
    print("While loop completed")

# Lambda

add = lambda nums2: nums2 + 10
print(add(15))

minus = lambda n: n - 10
print(minus(40))