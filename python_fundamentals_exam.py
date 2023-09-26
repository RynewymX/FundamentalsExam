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

print(intro + first_name)

length = float(input("What is the length of your rectangle?: "))
width = float(input("What is the width of your rectangle?: "))
def calculate_area(length, width):
    area = length * width
    print(f"The area of your rectangle is {area} square feet.")

calculate_area(length, width)
calculate_area(age, temperature)