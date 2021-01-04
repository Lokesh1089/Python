# List

fruits = ["Apple", "Mango", "Orange", "Kiwi", "Banana"]

print(fruits)
print(fruits[2])
print(fruits[1])
print(fruits[:3])
print(fruits[2:6])

fruits[1] = "Cherry"
fruits.append("Apple")
fruits.append("Graphs")
print(fruits)
print(len(fruits))
print(fruits.reverse())

prices = [180, 85, 120, 225, 49]
print(prices)
print(prices.sort())
prices.sort(reverse=True)
print(prices)

fruits_nd_prices = fruits + prices
print(fruits_nd_prices)
print(type(fruits))

# Tuples

Shapes = ('Rectangle', 'Square', 'Circle', 'Sphere')
print(Shapes)
print(Shapes[2])
print(Shapes[1:4])
print(Shapes[3])
print(type(Shapes))

# Set
Names = {'Rajesh', 'Aravind', 'Bharath', 'Chezhiyan'}
print(Names)
print(type(Names))

# Dictionary

my_data = {
    "name": "Ajay",
    "age": "23"
}
print(my_data)
print(my_data.get("age"))
print(my_data.get("name"))

my_data["age"] = "22"
my_data["name"] = "Varun Kumar"
print(my_data)

