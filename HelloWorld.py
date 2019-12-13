print('Hello World')
a = 3
course_name = "Code with Mosh"
print(len(course_name))
print(course_name[0])
print(course_name[-1])  # last character in a string
print(course_name[0:3])
first_name = "Fidel"
last_name = "Rosell"
# formatted strings
full_name = F"{first_name} {last_name}"
print(full_name)

# Working with numbers
# Math operatios:
# + * - /(float) //(integer) ** power --> (10 ** 3 = 1000) % remaining
# import math --> python 3 math in google

x = input("x: ")
v = int(x) + 9
print(" # " + str(v))

# Falsy: 0, "", None

# primitive types --> numbers, bool and strings.

# for loops
for number in range(3, 10, 2):
    print("I am eating ", number + 1, " apples", (number + 1) * ".")

# for else
success = False
for number in range(4):
    print(" Attempting")
    if success:
        print("Leaving For")
        break
else:
    print(" ELSE For")

even = 0
for number in range(1, 10):
    result = number % 2
    if result == 0:
        print(number)
        even += 1
else:
    print(" There are ", even, " numbers")

# complex type: range  --> type(range(4))

# while
number = 100
while number > 0:
    print(number)
    number //= 2
