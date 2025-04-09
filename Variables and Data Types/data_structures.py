# Create a list, tuple, and dictionary containing at least three elements each. Print these data structures and their types.


#list
fruits = ["banana","apple","orange"]

for fruit in fruits:
    print(f"Fruit: {fruit}")

for index, fruit in enumerate(fruits):
    print(f"Index: {index}, Fruit: {fruit}")

#Tuples
coordinates = (1,2,3)
x,y,z = coordinates
print(f"Location: ({x}; {y}; {z})")

#dictionary
person = {"name":"Alice", "age":25, "country": "UK"}
print(f"Name: {person['name']} , Age: {person['age']} , Country: {person['country']}")