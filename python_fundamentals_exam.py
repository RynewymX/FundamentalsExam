import numpy as np

intro = "Hello World"
print(intro)

first_name = input("What is your first name?: ")
print(first_name)

age = int(16)
temperature = float(59.0)
too_hot = False
print(type(age))
print(type(temperature))
print(type(too_hot))

print(age + temperature)
print(age - temperature)
print(age * temperature)
print(age / temperature)
print(age ** temperature)

print(f"{intro}, {first_name}!")

length = float(input("What is the length of your rectangle?: "))
width = float(input("What is the width of your rectangle?: "))
def calculate_area(length, width):
    area = length * width
    print(f"The area of your rectangle is {area} square feet.")

calculate_area(length, width)
calculate_area(age, temperature)

num1 = float(input("Give me a number: "))
if num1 > 0:
    print("Your number is positive.")
elif num1 < 0:
    print("Your number is negative.")
else:
    print("Your number is 0.")

numList = [4, 9, 16, 25, 36]
print(numList)
for item in numList:
    print(np.sqrt(item))
while age == 16:
    print(numList[0] ** 3)
    print(numList[1] ** 3)
    print(numList[2] ** 3)
    print(numList[3] ** 3)
    print(numList[4] ** 3)
    break
# why would you ever use a while loop for this it makes no sense just use a for loop????